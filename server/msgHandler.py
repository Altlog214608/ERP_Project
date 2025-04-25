import datetime
import json
import os
import traceback

from dotenv import load_dotenv

from dbManager import DBManager
from usage import Usage
from userManager import UserManager, Room

dbm = DBManager('localhost', 'root', '0000', 3306)
# dbm = DBManager('192.168.0.29', 'root', '0000', 3306)
um = UserManager(dbm)
load_dotenv()
endpoint = os.getenv("endpoint")
en_key = os.getenv("en_key")
de_key = os.getenv("de_key")
us = Usage(endpoint=endpoint, de_key=de_key)


class MsgProcessor:
    def __init__(self, func):
        self.func = func

    def __call__(self, **kwargs):
        try:
            return self.func(**kwargs)
        except Exception as e:
            print(traceback.format_exc())
            print("Error in MsgProcessor:" + str(e))
            return {"sign": 0, "data": {}}

class MsgHandler:
# 채팅 메소드
    @staticmethod
    @MsgProcessor
    def f85010(**kwargs):
        """
        직원 정보 검색 (사원코드, 사원이름, 부서, 직급 등)
        """
        # 기본 SQL 쿼리: employee 테이블에서 여러 컬럼들을 선택합니다.
        query = """
                       SELECT employee_code, name, name_eng, name_hanja, e_mail, zip_code, address, detail_address,
                              phone_number, date_of_employment, employment_status, employment_type, department,
                              job_grade, work_place, basic_salary, allowance, bonus, account
                       FROM employee
                       """
        conditions = []  # WHERE절에 추가할 조건들을 담을 리스트
        params = []  # SQL 쿼리의 파라미터를 담을 리스트

        # 사원코드가 제공되면 해당 사원코드로 필터링
        if kwargs.get("사원코드"):
            conditions.append("employee_code = %s")
            params.append(kwargs["사원코드"])

        # 사원이름이 제공되면 이름에 해당 문자열이 포함된 직원 검색 (LIKE 사용)
        if kwargs.get("사원이름"):
            conditions.append("name LIKE %s")
            params.append(f"%{kwargs['사원이름']}%")

        # 부서 정보가 제공되고 "전체"가 아닌 경우 부서 조건 추가
        if kwargs.get("부서") and kwargs["부서"] != "전체":
            conditions.append("department = %s")
            params.append(kwargs["부서"])

        # 직급 정보가 제공되고 "전체"가 아닌 경우 직급 조건 추가
        if kwargs.get("직급") and kwargs["직급"] != "전체":
            conditions.append("job_grade = %s")
            params.append(kwargs["직급"])

        # 조건이 하나 이상 있다면 WHERE절 추가
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        # SQL 디버깅용 출력
        print(f"[DEBUG] 실행될 SQL: {query} | 매개변수: {params}")

        # 쿼리 실행 (dbm.query는 DB 실행 후 결과 튜플 리스트를 반환)
        result = dbm.query(query, tuple(params))
        print("DB 조회 결과:", result)  # 디버깅용 출력

        # 결과가 없으면 sign 0, 빈 리스트 반환
        if not result:
            return {"sign": 0, "data": []}

        # 반환될 딕셔너리의 키(컬럼명)를 정의
        column_names = [
            "사원코드", "사원명", "영문명", "한자", "이메일", "우편번호", "주소", "상세주소", "전화번호",
            "입사일자", "근무상태", "고용형태", "소속부서", "직급", "근무지", "기본급여", "수당", "상여금", "계좌"
        ]

        # DB 결과의 각 row를 딕셔너리로 변환 (zip으로 컬럼명과 값을 매핑)
        data = [dict(zip(column_names, row)) for row in result]

        # 입사일자가 datetime 객체라면 문자열로 변환
        for row in data:
            if hasattr(row.get("입사일자"), "strftime"):
                row["입사일자"] = row["입사일자"].strftime("%Y-%m-%d")
        return {"sign": 1, "data": data}

    # DB에 등록된 사원코드를 확인하고, 이름 등 로그인 정보를 가져옵니다.
    @staticmethod
    @MsgProcessor
    def f85011(**kwargs):
        employee_code = kwargs.get("employee_code")
        if not employee_code:
            return {"sign": 0, "data": "사원코드가 없습니다."}
        # 여기서는 sock 정보는 kwargs에 포함되지 않은 것으로 가정합니다.
        return um.login(kwargs.get("request_id"), employee_code)

    # 실제로 채팅방을 생성한 후, 마지막 메시지 등을 조회하여 반환
    @staticmethod
    @MsgProcessor
    def f85012(**kwargs):
        # room_name과 members를 kwargs에서 추출
        room_name = kwargs.get("room_name")
        members = kwargs.get("members")
        if not room_name:
            return {"sign": 0, "data": "채팅방 이름이 필요합니다."}
        # members가 있으면 JSON 문자열로 변환, 없으면 빈 리스트 문자열 "[]"
        members_json = json.dumps(members) if members else "[]"
        # 채팅방 생성 쿼리: chat_rooms 테이블에 room_name과 members를 저장
        query = "INSERT INTO chat_rooms (room_name, members) VALUES (%s, %s)"
        dbm.query(query, (room_name, members_json))
        # 마지막으로 생성된 chat_room의 ID를 조회합니다.
        result = dbm.query("SELECT LAST_INSERT_ID()")
        room_id = result[0][0] if result and len(result) > 0 else None

        room_info = {
            "room_id": room_id,
            "room_name": room_name,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_message": "",
            "members": members_json
        }
        # 인메모리 방 관리에 새 방을 추가 (Room 객체 생성)
        new_room = Room(room_id, room_name, members=json.loads(members_json))
        um.rooms[room_id] = new_room
        return {"sign": 1, "data": [room_info]}

    # 메세지 보내기 및 저장 (채팅 메시지를 DB에 저장하고, 해당 채팅방에 브로드캐스트합니다.)
    @staticmethod
    @MsgProcessor
    def f75013(**kwargs):
        room_id = kwargs.get("room_id")
        sender_id = kwargs.get("sender_id")
        sender_name = kwargs.get("sender_name")
        message = kwargs.get("message")
        if not room_id or not sender_id or not message:
            return {"sign": 0, "data": "필수 인자가 부족합니다."}
        query = """
                     INSERT INTO chat_messages (room_id, sender_id, sender_name, message)
                     VALUES (%s, %s, %s, %s)
                   """
        dbm.query(query, (room_id, sender_id, sender_name, message))
        broadcast_msg = {
            "room_id": room_id,
            "sender_id": sender_id,
            "sender_name": sender_name,
            "message": message,
            "send_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        # 브로드캐스트: 연결된 사용자들에게 메시지 전송
        um.broadcast_room(room_id, {"code": 85013, "sign": 1, "data": broadcast_msg})
        return {"sign": 1, "data": {"code": 85013, "data": broadcast_msg}}

    # 채팅방 목록을 조회하여 반환합니다.
    @staticmethod
    @MsgProcessor
    def f85014(**kwargs):
        # chat_rooms 테이블에서 채팅방 정보와 각 채팅방의 마지막 메시지, 그리고 멤버 정보를 조회
        query = """
                     SELECT cr.room_id, cr.room_name, cr.created_at,
                            (SELECT cm.message FROM chat_messages cm 
                             WHERE cm.room_id = cr.room_id 
                             ORDER BY cm.send_time DESC LIMIT 1) AS last_message,
                            cr.members
                     FROM chat_rooms cr
                     ORDER BY cr.created_at DESC
                 """
        result = dbm.query(query)
        if not result:
            return {"sign": 0, "data": []}
        # 조회된 결과를 딕셔너리 리스트로 변환
        # 컬럼 순서는: room_id, room_name, created_at, last_message, members
        columns = ["room_id", "room_name", "created_at", "last_message", "members"]
        data_list = [dict(zip(columns, row)) for row in result]
        # created_at이 datetime 객체라면 문자열로 변환
        for rec in data_list:
            if rec.get("created_at") and hasattr(rec["created_at"], "strftime"):
                rec["created_at"] = rec["created_at"].strftime("%Y-%m-%d %H:%M:%S")
        return {"sign": 1, "data": data_list}

    # 채팅방 참여 (해당 사원이 특정 채팅방에 참여하도록 처리)
    @staticmethod
    @MsgProcessor
    def f85015(**kwargs):
        room_id = kwargs.get("room_id")
        employee_code = kwargs.get("employee_code")
        if not room_id or not employee_code:
            return {"sign": 0, "data": "필수 인자가 부족합니다."}
        return um.join_room(kwargs.get("request_id"), employee_code, room_id)

    @staticmethod
    @MsgProcessor
    def f85016(**kwargs):
        """
        채팅 내역 조회 기능:
        - 입력: 특정 채팅방의 room_id
        - 처리: chat_messages 테이블에서 해당 room_id의 모든 메시지를 send_time 오름차순으로 조회
        - 반환: 각 메시지에 대해 sender_id, sender_name, message, send_time(문자열) 정보를 담은 딕셔너리들의 리스트
        """
        room_id = kwargs.get("room_id")
        if not room_id:
            return {"sign": 0, "data": "room_id가 필요합니다."}

        query = """
               SELECT sender_id, sender_name, message, send_time
               FROM chat_messages
               WHERE room_id = %s
               ORDER BY send_time ASC
           """
        result = dbm.query(query, (room_id,))
        if not result:
            # 메시지가 없는 경우 빈 리스트 반환
            return {"sign": 1, "data": []}

        data_list = []
        for row in result:
            sender_id, sender_name, message, send_time = row
            # send_time이 datetime 객체인 경우 문자열로 변환
            if hasattr(send_time, "strftime"):
                send_time = send_time.strftime("%Y-%m-%d %H:%M:%S")
            data_list.append({
                "sender_id": sender_id,
                "sender_name": sender_name,
                "message": message,
                "send_time": send_time
            })

        return {"sign": 1, "data": data_list}

    @staticmethod
    @MsgProcessor
    def f85017(**kwargs):
        """
        채팅방 나가기 기능:
        """
        room_id = kwargs.get("room_id")
        employee_code = kwargs.get("employee_code")
        if not room_id or not employee_code:
            return {"sign": 0, "data": "방정보 부족."}

        # 해당 채팅방의 현재 members 값을 조회
        query = "SELECT members FROM chat_rooms WHERE room_id = %s"
        result = dbm.query(query, (room_id,))
        if not result:
            return {"sign": 0, "data": "채팅방을 찾을 수 없습니다."}

        members_json = result[0][0]
        try:
            members = json.loads(members_json)
        except Exception as e:
            print(traceback.format_exc())
            members = []

        # 만약 해당 사용자가 members 목록에 있다면 제거
        if employee_code in members:
            members.remove(employee_code)
        else:
            return {"sign": 0, "data": f"{employee_code}는 해당 채팅방에 참여중이지 않습니다."}

        updated_members_json = json.dumps(members)
        update_query = "UPDATE chat_rooms SET members = %s WHERE room_id = %s"
        dbm.query(update_query, (updated_members_json, room_id))
        return {"sign": 1, "data": f"{employee_code}가 채팅방에서 나갔습니다."}

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    @staticmethod
    @MsgProcessor
    def f10101(**kwargs):
        query = """
                UPDATE companyfile
                SET  fiscal_year = %s, business_registration_number = %s, corporation_registration_number = %s,  representative_foreign = %s, representative_resident_number = %s,
                zip_code = %s, address = %s,   detailed_address  = %s, business_Type = %s, category = %s, phone_Number = %s, fax_Number = %s, establishment_date = %s ,closed_date = %s
                is_active = %s
    
                WHERE coperationNumber = %s
                 """
        values = ( kwargs.get("회계년도"), kwargs.get("사업wk 등록번호"), kwargs.get("법인 등록번호"),kwargs.get("대표자 외국인 여부"), kwargs.get("대표자 주민번호"),
                  kwargs.get("우편번호"), kwargs.get("주소"), kwargs.get("상세 주소"), kwargs.get("업태"), kwargs.get("종목"),kwargs.get("전화 번호"), kwargs.get("팩스 번호"),
                  kwargs.get("설립년도"),kwargs.get("폐업년도"), kwargs.get("사용 여부"), kwargs.get("사업장 등록번호"))

        result = dbm.query(query ,values)

        if result is not None:
            return {
                'sign': 1,
                'data': []
            }

        else:
            return {
                'sign': 0,
                'data': []
            }

    #     # 저장
    @staticmethod
    @MsgProcessor
    def f10102(**kwargs):
        query = '''
        INSERT INTO companyinformation (fiscal_year, business_registration_number, corporation_registration_number,
        representative_foreign, representative_resident_number, zip_code, address,
        detailed_address, business_type, category, phone_number, fax_number,
        establishment_date, closed_date, is_active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''

        representative_foreign_value = kwargs.get('대표자 외국인 여부', ' ').strip()
        representative_foreign = 1 if representative_foreign_value == '유' else 0

        establishment_date = kwargs.get('설립 날짜', '').strip() or '1900-01-01'
        closed_date = kwargs.get('폐업 날짜', '').strip() or '9999-12-31'

        is_active_value = kwargs.get('사용 여부', '').strip()
        is_active = 0 if is_active_value == "운영" else 1 if is_active_value == "폐업" else None

        values = (
            kwargs.get('회계년도', ' '), kwargs.get('사업장 등록번호', ' '), kwargs.get('법인 등록번호', ' '),
            representative_foreign,
            kwargs.get('대표자 주민번호', ' '), kwargs.get('우편 번호', ' '),
            kwargs.get('주 소', ' '), kwargs.get('상세 주소', ' '), kwargs.get('업 태', ' '),
            kwargs.get('종목', ''), kwargs.get('전화 번호', ' '), kwargs.get('팩스 번호', ' '),
            establishment_date, closed_date, is_active)

        try:
            result = dbm.query(query, values)

            if result:
                return {'sign': 1, 'data': result}

            else:
                return {'sign': 0, 'data': "쿼리 실패"}



        except Exception as e:
            print("쿼리 실행 중 오류 발생:", str(e))
            return {'sign': 0, 'data': f"오류 발생: {str(e)}"}

    @staticmethod
    @MsgProcessor
    def f10103(**kwargs):
    # 등록번호 : corporation_registration_number 123-12-12345
    # 회사이름 :
    # 대표자이름 :
    # 주소 : address
        result = {'sign':1,'data':{"등록번호":"123-12-99999","주소":"대전 서구 계룡로 491번길 86","회사이름":"대전인더스트리","대표자":"성진하"}}
        return result


    @staticmethod
    @MsgProcessor
    def f10201(**kwargs):
        """
              직원 정보 검색 (사원코드, 사원이름, 부서, 직급 등)
              - 검색 조건이 있는 경우 필터링하여 조회
              - 조건이 없으면 전체 조회
        """
        query = """
                    SELECT employee_code, name, name_eng, name_hanja, e_mail, zip_code, address, detail_address,
                           phone_number, date_of_employment, employment_status, employment_type, department,
                           job_grade, work_place, basic_salary, allowance, bonus, account, pic
                    FROM employee
                    """

        conditions = []
        params = []

        if kwargs.get("사원코드"):
            conditions.append("employee_code = %s")
            params.append(kwargs["사원코드"])

        if kwargs.get("사원이름"):
            conditions.append("name LIKE %s")
            params.append(f"%{kwargs['사원이름']}%")

        if kwargs.get("부서") and kwargs["부서"] != "전체":
            conditions.append("department = %s")
            params.append(kwargs["부서"])

        if kwargs.get("직급") and kwargs["직급"] != "전체":
            conditions.append("job_grade = %s")
            params.append(kwargs["직급"])

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        print(f"[DEBUG] 실행될 SQL: {query} | 매개변수: {params}")

        result = dbm.query(query, tuple(params))
        print("DB 조회 결과:", result)

        if not result:
            return {"sign": 0, "data": []}

        # 컬럼 이름 매칭 (pic 필드 포함)
        column_names = [
            "사원코드", "사원명", "영문명", "한자", "이메일", "우편번호", "주소", "상세주소", "전화번호",
            "입사일자", "근무상태", "고용형태", "소속부서", "직급", "근무지", "기본급여", "수당", "상여금", "계좌", "pic"
        ]

        data = [dict(zip(column_names, row)) for row in result]

        for row in data:
            # 날짜 형식 처리: datetime 객체이면 문자열로 변환
            if hasattr(row.get("입사일자"), "strftime"):
                row["입사일자"] = row["입사일자"].strftime("%Y-%m-%d")
            # pic 필드가 bytes 타입이면 utf-8 문자열로 디코딩
            pic_value = row.get("pic")
            if pic_value is not None and isinstance(pic_value, bytes):
                row["pic"] = pic_value.decode("utf-8")

        return {"sign": 1, "data": data}

    @staticmethod
    @MsgProcessor
    def f10202(**kwargs):
        result = {
            "sign": 1,
            "data": "신규 버튼 눌렀구나"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f10203(**kwargs):
        """
        직원 정보 수정 (UPDATE)
        """
        query = """
       UPDATE employee
       SET name = %s, name_eng = %s, name_hanja = %s, e_mail = %s,
           zip_code = %s, address = %s, detail_address = %s, phone_number = %s,
           date_of_employment = %s, employment_status = %s, employment_type = %s,
           department = %s, job_grade = %s, work_place = %s,
           basic_salary = %s, allowance = %s, bonus = %s, account = %s, pic = %s
       WHERE employee_code = %s
       """
        import codecs
        print(type(kwargs.get("pic", "").encode('utf-8')))

        params = (
            kwargs.get("사원명"), kwargs.get("영문명"), kwargs.get("한자"), kwargs.get("이메일"),
            kwargs.get("우편번호"), kwargs.get("주소"), kwargs.get("상세주소"), kwargs.get("전화번호"),
            kwargs.get("입사일자"), kwargs.get("근무상태"), kwargs.get("고용형태"), kwargs.get("소속부서"),
            kwargs.get("직급"), kwargs.get("근무지"), kwargs.get("기본급여"), kwargs.get("수당"), kwargs.get("상여금"),
            kwargs.get("계좌"),codecs.encode(kwargs.get("pic", "").encode('utf-8'), "base64"), kwargs.get("사원코드")
        )

        result = dbm.query(query, params)

        if result is not None:
            print("직원 정보 수정 완료")
            return {"sign": 1,
                    "data": "잘 수정된듯"}
        else:
            # print("뭔가 오류발생", e)
            return {"sign": 0,
                    "data": []}

    @staticmethod
    @MsgProcessor
    def f10204(**kwargs):
        """
        직원 정보 저장 (10204)
        """
        query = """
                  INSERT INTO employee (employee_code, name, name_eng, name_hanja, e_mail, zip_code, address, detail_address,
                  phone_number, date_of_employment, employment_status, employment_type, department, job_grade, work_place,
                  basic_salary, allowance, bonus, account, pic)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                  """
        import codecs
        params = (
            kwargs.get("사원코드", ""), kwargs.get("사원명", ""), kwargs.get("영문명", ""), kwargs.get("한자", ""),
            kwargs.get("이메일", ""), kwargs.get("우편번호", ""), kwargs.get("주소", ""), kwargs.get("상세주소", ""),
            kwargs.get("전화번호", ""),
            kwargs.get("입사일자", ""), kwargs.get("근무상태", ""), kwargs.get("고용형태", ""), kwargs.get("소속부서", ""),
            kwargs.get("직급", ""),
            kwargs.get("근무지", ""), kwargs.get("기본급여", ""), kwargs.get("수당", ""), kwargs.get("상여금", ""),
            kwargs.get("계좌", ""),  # kwargs.get("사진", ""),
            # kwargs.get("사진", ""),
            codecs.encode(kwargs.get("pic", "").encode('utf-8'), "base64")

        )

        result = dbm.query(query, params)

        if result is not None:
            print("직원 정보 수정 완료")
            return {"sign": 1,
                    "data": "잘 저장된듯"}
        else:
            # print("뭔가 오류발생", e)
            return {"sign": 0,
                    "data": []}

    # -------------------- 급여명세서 --------------------

    @staticmethod
    @MsgProcessor
    def f10301(**kwargs):
        """
        급여명세서 조회
        """
        query = """
           SELECT
               COALESCE(sd.pay_stub_id, 0) AS pay_stub_id,
               e.employee_code,
               e.name,
               e.department,
               COALESCE(sd.basic_salary, e.basic_salary) AS 기본급,
               COALESCE(sd.allowance, e.allowance) AS 수당,
               COALESCE(sd.bonus, e.bonus) AS 상여금,
               COALESCE(sd.additional_allowance, 0) AS 추가수당,
               COALESCE(sd.annual_leave_allowance, 0) AS 연차수당,
               COALESCE(sd.total_salary, e.basic_salary + e.allowance + e.bonus) AS 총지급액,
               COALESCE(sd.income_tax, 0) AS 소득세,
               COALESCE(sd.final_payment, e.basic_salary + e.allowance + e.bonus) AS 최종지급액,
               sd.pay_out_date,
               e.employment_status
           FROM employee e
           LEFT JOIN salary_details sd
                  ON e.employee_code = sd.employee_code
       """
        conditions = []
        params = []
        if kwargs.get("사원코드"):
            conditions.append("e.employee_code = %s")
            params.append(kwargs["사원코드"])
        if kwargs.get("사원이름"):
            conditions.append("e.name LIKE %s")
            params.append(f"%{kwargs['사원이름']}%")
        if kwargs.get("부서") and kwargs["부서"] != "전체":
            conditions.append("e.department = %s")
            params.append(kwargs["부서"])
        if kwargs.get("직급") and kwargs["직급"] != "전체":
            conditions.append("e.job_grade = %s")
            params.append(kwargs["직급"])
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        result = dbm.query(query, tuple(params))
        if not result:
            return {"sign": 0, "data": []}
        columns = ["pay_stub_id", "사원코드", "사원명", "부서", "기본급", "수당", "상여금",
                   "추가수당", "연차수당", "총지급액", "소득세", "최종지급액", "pay_out_date", "현재상태"]
        data_list = [dict(zip(columns, row)) for row in result]
        for rec in data_list:
            if rec.get("pay_out_date") and hasattr(rec["pay_out_date"], "strftime"):
                rec["pay_out_date"] = rec["pay_out_date"].strftime("%Y-%m-%d")
        return {"sign": 1, "data": data_list}

    @staticmethod
    @MsgProcessor
    def f10302(**kwargs):
        """
        급여명세서 저장
        """
        emp_code = kwargs.get("사원코드")
        if not emp_code:
            return {"sign": 0, "data": "사원코드가 없습니다."}
        pay_date = kwargs.get("날짜")
        try:
            basic_salary = int(kwargs.get("기본급", 0))
            allowance = int(kwargs.get("수당", 0))
            bonus = int(kwargs.get("상여금", 0))
            additional_allowance = int(kwargs.get("추가수당", 0))
            annual_leave_allowance = int(kwargs.get("연차수당", 0))
            total_salary = int(
                kwargs.get("총지급액", basic_salary + allowance + bonus + additional_allowance + annual_leave_allowance))
            income_tax = int(kwargs.get("소득세", total_salary * 0.033))
            final_payment = int(kwargs.get("최종지급액", total_salary - income_tax))
        except Exception as e:
            return {"sign": 0, "data": f"숫자 변환 오류: {str(e)}"}

        pay_stub_id = kwargs.get("pay_stub_id")
        if pay_stub_id:
            # UPDATE
            query = """
               UPDATE salary_details
                  SET pay_out_date=%s, basic_salary=%s, allowance=%s, bonus=%s,
                      additional_allowance=%s, annual_leave_allowance=%s,
                      total_salary=%s, income_tax=%s, final_payment=%s
                WHERE pay_stub_id=%s
           """
            params = (pay_date, basic_salary, allowance, bonus, additional_allowance,
                      annual_leave_allowance, total_salary, income_tax, final_payment, pay_stub_id)
            dbm.query(query, params)
            return {"sign": 1, "data": "급여명세 수정 성공"}
        else:
            # INSERT
            query = """
               INSERT INTO salary_details (
                   employee_code, pay_out_date, basic_salary, allowance, bonus,
                   additional_allowance, annual_leave_allowance, total_salary,
                   income_tax, final_payment
               ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
           """
            params = (emp_code, pay_date, basic_salary, allowance, bonus, additional_allowance,
                      annual_leave_allowance, total_salary, income_tax, final_payment)
            dbm.query(query, params)
            result = dbm.query("SELECT LAST_INSERT_ID()")
            new_id = result[0][0] if result and len(result) > 0 else None
            return {"sign": 1, "data": f"급여명세 저장 성공, ID: {new_id}"}

    @staticmethod
    @MsgProcessor
    def f10303(**kwargs):
        """
        급여명세서 삭제
        """
        pay_stub_id = kwargs.get("pay_stub_id")
        if not pay_stub_id:
            return {"sign": 0, "data": "삭제할 ID가 없습니다."}
        query = "DELETE FROM salary_details WHERE pay_stub_id = %s"
        dbm.query(query, (pay_stub_id,))
        return {"sign": 1, "data": f"급여명세서 ID {pay_stub_id} 삭제 성공"}

    @staticmethod
    @MsgProcessor
    def f10304(**kwargs):
        return {"sign": 1, "data": "결재 요청 완료"}

    # 퇴직금 조회---------------------------------------------------------------------------
    @staticmethod
    @MsgProcessor
    def f10401(**kwargs):
        """
        퇴직금 정보 조회
        """
        query = """
          SELECT employee_code, name, department, job_grade,
                 basic_salary, allowance, bonus
            FROM employee
       """
        conditions = []
        params = []
        if kwargs.get("사원코드"):
            conditions.append("employee_code = %s")
            params.append(kwargs["사원코드"])
        if kwargs.get("사원이름"):
            conditions.append("name LIKE %s")
            params.append(f"%{kwargs['사원이름']}%")
        if kwargs.get("부서") and kwargs["부서"] != "전체":
            conditions.append("department = %s")
            params.append(kwargs["부서"])
        if kwargs.get("직급") and kwargs["직급"] != "전체":
            conditions.append("job_grade = %s")
            params.append(kwargs["직급"])
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        result = dbm.query(query, tuple(params))
        if not result:
            return {"sign": 0, "data": []}

        data = []
        for row in result:
            data.append({
                "사원코드": row[0],
                "사원이름": row[1],
                "부서": row[2],
                "직급": row[3],
                "basic_salary": row[4],
                "allowance": row[5],
                "bonus": row[6]
            })
        return {"sign": 1, "data": data}

    # 결재신청
    @staticmethod
    @MsgProcessor
    def f10402(**kwargs):
        result = {
            "sign": 1,
            "data": "10402"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f10403(**kwargs):
        result = {
            "sign": 1,
            "data": "10403"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f10404(**kwargs):
        result = {
            "sign": 1,
            "data": "10404"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f10405(**kwargs):
        result = {
            "sign": 1,
            "data": "10405"
        }
        return result

    @staticmethod
    @MsgProcessor
    # 서버용 조회 함수
    def f10501(**kwargs):
        # dbm = dbManager.DBManager(host="192.168.0.29", user="root", password="0000", port=3306)

        base_query = """
           SELECT e.employee_code, e.name, e.department, a.work_start_time, a.work_end_time, a.late, 
                  a.early_leave, a.overtime, a.leave_used, a.attendance_status
                  FROM erp_db.employee e
                 LEFT JOIN erp_db.attendance a ON e.employee_code = a.employee_code
             """

        # 조건으로 사용할 유효한 컬럼 목록
        valid_columns = {"employee_code", "name", "department"}

        # 조건이 있는 경우 WHERE 절 추가
        valid_conditions = [f"{key} LIKE '%%{value}%%'" for key, value in kwargs.items()
                            if key in valid_columns and value]

        # 조건이 없으면 전체 조회, 조건이 있으면 필터링 조회
        query = base_query if not valid_conditions else f"{base_query} WHERE {' AND '.join(valid_conditions)}"

        data = dbm.query(query) or []

        if not data:
            return {"sign": 0, "data": "조회 결과 없음"}

        # 날짜 데이터를 문자열로 변환
        formatted_data = [
            [str(item) if isinstance(item, (datetime.date, datetime.time, datetime.timedelta)) else item for item in
             row]
            for row in data
        ]

        if not formatted_data:
            return {"sign": 0, "data": "포맷팅된 데이터 없음"}

        else:
            return {"sign": 1, "data": formatted_data}

    @staticmethod
    @MsgProcessor
    def f10502(**kwargs):
        result = {
            "sign": 1,
            "data": "10502"
        }
        return result

    @staticmethod
    @MsgProcessor
    # 서버용 조회 함수
    def f10601(**kwargs):
        # dbm = dbManager.DBManager(host="192.168.0.29", user="root", password="0000", port=3306)
        base_query = "SELECT employee_code,name,department,'date',work_start_time,work_end_time,overtime,Approval_status,pay FROM overtime"
        valid_columns = {"employee_code", "name", "department", "'date'", "start_time", "end_time"}

        valid_conditions = [
            f"COALESCE({key}, '') LIKE '%{value}%'"
            for key, value in kwargs.items()
            if key in valid_columns and value
        ]

        query = base_query if not valid_conditions else f"{base_query} WHERE {' AND '.join(valid_conditions)}"

        data = dbm.query(query) or []

        # 전체 출력 조건 추가
        if not data:
            data = dbm.query(base_query) or []

        formatted_data = [
            [str(item) if isinstance(item, datetime.date) else item for item in row]
            for row in data
        ]

        return {"sign": 1, "data": formatted_data} if formatted_data else {"sign": 0, "data": "쿼리 실패"}

    @staticmethod
    @MsgProcessor
    def f10602(**kwargs):
        result = {
            "sign": 1,
            "data": "10602"
        }
        return result

    @staticmethod
    @MsgProcessor
    # 서버용 조회 함수
    def f10701(**kwargs):
        #     dbm = dbManager.DBManager(host="192.168.0.29", user="root", password="0000", port=3306)
        # 사원 코드 , 이름 , 부서 , 직급 검색 조건 ---> 검색 결과는 사원 코드 ,이름 ,부서, 초과근무날짜, 시작시간 ,종료 시간 ,승인 여부, 수당지급

        base_query = """
                SELECT employee_code, name, department, position, join_date, 
                total_leave, used_leave, approval_status 
                FROM annual_leave_management
              """

        # 검색 조건으로 사용할 유효한 컬럼 목록
        valid_columns = {"employee_code", "name", "department"}

        # 입력된 kwargs에서 유효한 검색 조건 필터링
        valid_conditions = [
            f"COALESCE({key}, '') LIKE '%%{value}%%'" for key, value in kwargs.items()
            if key in valid_columns and value]

        # 조건이 있으면 WHERE 절 추가
        query = base_query if not valid_conditions else f"{base_query} WHERE {' AND '.join(valid_conditions)}"

        # SQL 실행
        data = dbm.query(query) or []

        # 전체 출력 조건 추가
        if not data:
            data = dbm.query(base_query) or []

        # 날짜 데이터를 문자열로 변환
        formatted_data = [
            [str(item) if isinstance(item, (datetime.date, datetime.time, datetime.timedelta)) else item for item in
             row]
            for row in data]

        return {"sign": 1, "data": formatted_data} if formatted_data else {"sign": 0, "data": "쿼리 실패"}

    @staticmethod
    @MsgProcessor
    def f10702(**kwargs):
        result ={
            'sign' : 1,
            'data': '10702'
        }
        return result

    @staticmethod
    @MsgProcessor
    def f20101(**kwargs):
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
            # print(f'Index: {i}, Value: {value}')
        query = f"SELECT * FROM sop where (sop_Code like '%%{valueList[0]}%%' and writter like '%%{valueList[1]}%%' and written_date like '%%{valueList[2]}%%' and order_code like '%%{valueList[3]}%%' and material_code like '%%{valueList[4]}%%' and material_name like '%%{valueList[5]}%%') "
        result = dbm.query(query, [])
        print("result", result)

        if query:
            return {"sign": 1, 'data': result}
        elif not query:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20102(**kwargs):
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"insert into sop values('{valueList[0]}', '{valueList[1]}','{valueList[2]}','{valueList[3]}','{valueList[4]}','{valueList[5]}','{valueList[6]}')"
        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        elif not query:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20103(**kwargs):  # 프레임3 수정
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
            # print(f'Index: {i}, Value: {value}
        for i in valueList[0]:
            # print('i :', i) #i : ['sop33', '', '수정', '', '', '', '']
            # print('i[0]',i[0])
            query = f"update sop set sop_code = '{i[0]}' ,bom_code = '{i[1]}',order_code = '{i[2]}',material_code = '{i[3]}',material_name = '{i[4]}',writter = '{i[5]}',written_date = '{i[6]}' where sop_code = '{i[0]}' "  # valueList[2][k][0]
            result = dbm.query(query, [])

            print("result", result)

            if query:
                return {"sign": 1, 'data': result}
            elif not query:
                return {"sign": 0, 'data': None}
            # for j in i:
            # for k in valueList[1]:

    @staticmethod
    @MsgProcessor
    def f20104(**kwargs):
        valueList = []

        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"insert into sop_f values('{valueList[0]}', '{valueList[1]}','{valueList[2]}','{valueList[3]}')"
        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        elif not query:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20105(**kwargs):  # 프레임1 수정
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
            # print(f'Index: {i}, Value: {value}')
        # print('valueList[0]', valueList[1][0])
        # print('valueList[2][valueList[0]][0]', valueList[2][valueList[1][0]][0],)
        print(valueList[2], 1111111111)

        for i in valueList[0]:
            query = f"update sop_f set sop_code = '{i[0]}' ,work_name = '{i[1]}',working = '{i[2]}',photo = '{i[3]}' where (work_name = '{valueList[2][valueList[1][0]][1]}' )"  # valueList[2][k][0]
        result = dbm.query(query, [])
        print("result", result)

        if query:
            return {"sign": 1, 'data': result}
        elif not query:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20106(**kwargs):  # 문서더블클릭
        valueList = []

        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"SELECT * FROM sop_f WHERE sop_code = '{valueList[0]}' "
        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        elif not query:
            return {"sign": 0, 'data': None}


    @staticmethod
    @MsgProcessor
    def f20107(**kwargs):  # 문서더블클릭
        valueList = []

        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"SELECT order_code, product_code, product_name FROM order_form WHERE order_code = '{valueList[0]}' "
        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        elif not query:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20201(**kwargs):
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"SELECT * FROM bom where (bom_Code like '%%{valueList[0]}%%' and sop_code like '%%{valueList[1]}%%' and written_date like '%%{valueList[2]}%%' and order_code like '%%{valueList[3]}%%' and material_code like '%%{valueList[4]}%%' and material_name like '%%{valueList[5]}%%') "

        result = dbm.query(query, [])
        d = [list(row) for row in result]

        if result:
            return {"sign": 1, 'data': result}
        else:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20202(**kwargs):
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"insert into bom values('{valueList[0]}', '{valueList[1]}','{valueList[2]}','{valueList[3]}','{valueList[4]}','{valueList[5]}')"
        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        else:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20203(**kwargs):  # 프레임3 수정
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
            # print(f'Index: {i}, Value: {value}
        for i in valueList[0]:
            # print('i :', i) #i : ['sop33', '', '수정', '', '', '', '']
            # print('i[0]',i[0])
            query = f"update bom set bom_code = '{i[0]}' ,sop_code = '{i[1]}',written_date = '{i[2]}',order_code = '{i[3]}',material_code = '{i[4]}',material_name = '{i[5]}' where bom_code = '{i[0]}' "  # valueList[2][k][0]
            result = dbm.query(query, [])

            print("result", result)

            if query:
                return {"sign": 1, 'data': result}
            elif not query:
                return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20204(**kwargs):  # frame3의 저장
        valueList = []

        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"insert into bom_f values('{valueList[0]}', '{valueList[1]}','{valueList[2]}','{valueList[3]}','{valueList[4]}','{valueList[5]}')"
        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        else:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20205(**kwargs):  # 프레임1 수정 #함수 추가#########
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
            # print(f'Index: {i}, Value: {value}')
        # print('valueList[0]', valueList[1][0])
        # print('valueList[2][valueList[0]][0]', valueList[2][valueList[1][0]][0],)
        # print(valueList[2][valueList[1][0]][0], 0)
        # print(valueList[2][valueList[1][0]][1], 1)
        # print(valueList[2][valueList[1][0]][2], 2)
        # print(valueList[2][valueList[1][0]][3], 3)
        # print(valueList[2][valueList[1][0]][4], 4)
        # print(valueList[2][valueList[1][0]][5], 5)

        # for i in valueList[0]:
        #     print('iiiiiiiii',i)
        #
        for i in valueList[0]:
            query = f"UPDATE bom_f SET bom_code = '{i[0]}' , material_code = '{i[1]}' , material_name = '{i[2]}' , quantity = '{i[3]}' , unit = '{i[4]}' , purchase_price = '{i[5]}' WHERE (bom_code = '{valueList[2][valueList[1][0]][0]}' AND material_code = '{valueList[2][valueList[1][0]][1]}' AND material_name = '{valueList[2][valueList[1][0]][2]}' AND quantity = '{valueList[2][valueList[1][0]][3]}' AND unit = '{valueList[2][valueList[1][0]][4]}' )"  # valueList[2][k][0]
            # query = f"select * from bom_f"
            # query = f"UPDATE bom_f SET bom_code = '{valueList[0]}' , material_code = '{valueList[1]}' , material_name = '{valueList[2]}' , quantity = '{valueList[3]}' , unit = '{valueList[4]}' , purchase_price = '{valueList[5]}' WHERE (bom_code = '{valueList[7]}' AND material_code = '{valueList[8]}' AND material_name = '{valueList[9]}' AND quantity = '{valueList[10]}' AND unit = '{valueList[11]}' AND purchase_price = '{valueList[12]}')"  # valueList[2][k][0]

            result = dbm.query(query, [])
            print("result", result)

            if query:
                return {"sign": 1, 'data': result}
            elif not query:
                return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20206(**kwargs):
        valueList = []

        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"SELECT * FROM bom_f WHERE bom_code = '{valueList[0]}' "
        # query = f"SELECT * FROM bom_f"
        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        else:
            return {"sign": 0, 'data': None}


    @staticmethod
    @MsgProcessor
    def f20207(**kwargs):
        valueList = []

        for i, value in enumerate(kwargs.values()):
            print(i, value)
            valueList.append(value)
        query = f"SELECT order_code, product_code, product_name FROM order_form WHERE order_code = '{valueList[0]}' "
        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        elif not query:
            return {"sign": 0, 'data': None}


    @staticmethod
    @MsgProcessor
    def f20301(**kwargs):
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"SELECT * FROM mo where (mo_code like '%%{valueList[0]}%%' and sop_code like '%%{valueList[1]}%%' and bom_code like '%%{valueList[2]}%%' and order_code like '%%{valueList[3]}%%' and material_code like '%%{valueList[4]}%%' and material_name like '%%{valueList[5]}%%') "

        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        else:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20302(**kwargs):
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"INSERT INTO mo values('{valueList[0]}','{valueList[1]}','{valueList[2]}','{valueList[3]}','{valueList[4]}','{valueList[5]}','{valueList[6]}','{valueList[7]}','{valueList[8]}') "

        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        else:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20303(**kwargs):
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"SELECT * FROM sop WHERE sop_code = '{valueList[0]}'"

        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        else:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20304(**kwargs):
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
        query = f"SELECT sop_code FROM sop"

        result = dbm.query(query, [])
        print("result", result)
        if query:
            return {"sign": 1, 'data': result}
        else:
            return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20305(**kwargs):  # 프레임3 수정
        valueList = []
        for i, value in enumerate(kwargs.values()):
            valueList.append(value)
            # print(f'Index: {i}, Value: {value}
        for i in valueList[0]:
            # print('i :', i) #i : ['sop33', '', '수정', '', '', '', '']
            print('i[0]', i[0])
            query = f"update mo set mo_code = '{i[0]}' ,sop_code = '{i[1]}',bom_code = '{i[2]}',quantity = '{i[3]}',state = '{i[4]}',material_code = '{i[5]}',material_name = '{i[6]}', order_code = '{i[7]}', due_date = '{i[8]}' WHERE mo_code = '{i[0]}' "  # valueList[2][k][0]
            result = dbm.query(query, [])

            print("result", result)

            if query:
                return {"sign": 1, 'data': result}
            elif not query:
                return {"sign": 0, 'data': None}

    @staticmethod
    @MsgProcessor
    def f20404(**kwargs):  # 저장버튼
        db = dbm
        # 빈 문자열을 None으로 변환
        price = kwargs.get("price") if kwargs.get("price") != "" else None
        selling_price = kwargs.get("sellingPrice") if kwargs.get("sellingPrice") != "" else None
        purchase_price = kwargs.get("purchasePrice") if kwargs.get("purchasePrice") != "" else None
        weight = kwargs.get("weight") if kwargs.get("weight") != "" else None

        if kwargs.get("check") == 'M':
            # materialCode가 존재하면 UPDATE 쿼리 실행
            query = """
                           UPDATE erp_db.materialtable
                           SET materialName = %s, materialType = %s, price = %s, sellingPrice = %s,
                               purchasePrice = %s, unit = %s, weight = %s, correspondentCode = %s,
                               correspondentName = %s, Date_up = %s, department = %s, manager = %s
                           WHERE materialCode = %s
                       """
            params = [
                kwargs.get("materialName"), kwargs.get("materialType"), price,
                selling_price, purchase_price, kwargs.get("unit"), weight,
                kwargs.get("correspondentCode"), kwargs.get("correspondentName"),
                kwargs.get("Date_up"), kwargs.get("department"), kwargs.get("manager"),
                kwargs.get("materialCode")
            ]
            result = db.query(query, tuple(params))
            if result is not None:
                return {'sign': 1, "data": []}
            if result is None:
                return {'sign': 0, "data": []}

        if kwargs.get("check") == 'C':
            # materialCode가 없으면 INSERT 쿼리 실행
            query = """
                           INSERT INTO erp_db.materialtable (materialCode, materialName, materialType, price, sellingPrice,
                                                purchasePrice, unit, weight, correspondentCode, correspondentName,
                                                Date_up, department, manager)
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                       """
            params = [
                kwargs.get("materialCode"), kwargs.get("materialName"), kwargs.get("materialType"),
                price, selling_price, purchase_price, kwargs.get("unit"), weight,
                kwargs.get("correspondentCode"), kwargs.get("correspondentName"),
                kwargs.get("Date_up"), kwargs.get("department"), kwargs.get("manager")
            ]
            result = db.query(query, tuple(params))  # result가 실패면 NOne

            # if문 써서 저장 잘 됐으면 "sign":1로 안됐으면 0으로 해야함
            if result is not None:
                return {'sign': 1, "data": []}
            if result is None:
                return {'sign': 0, "data": []}

    @staticmethod
    @MsgProcessor
    def f20402(**kwargs):  # 조회버튼
        db = dbm
        base_query = "SELECT materialCode, materialName, materialType, price, sellingPrice, purchasePrice, unit, weight, correspondentCode, correspondentName, Date_up, department, manager FROM erp_db.materialtable"
        test = []
        for key, value in kwargs.items():
            if key == "aa" or value == "전체":
                continue
            if key == "Date_up":
                f"Date_up between {kwargs.get("aa")} and {value}"
            elif value != "":
                test.append(f"{key} LIKE '%%{value}%%'")
        if test:
            query = f"{base_query} WHERE {' AND '.join(test)}"
            print(query)
        else:
            query = base_query

        result = db.query(query, [])  # 만약에 잘들어가면 reult에 데이터가 들어갈거고 안되면 None들어감
        material_data = []
        print("결과입니당", result)
        if result:
            material_data = [list(row) for row in result]

        if result is not None:
            return {'sign': 1, "data": material_data}
        if result is None:
            return {'sign': 0, "data": []}

    def f20401(**kwargs): #조회버튼
        base_query = "SELECT * FROM materialtable"
        test = []
        for key, value in kwargs.items():
            if key == "aa":
                continue
            if key == "Date_up":
                f"Date_up between {kwargs.get("aa")} and {value}"
            elif value != "":
                test.append(f"{key} = '{value}'")

        if test:
            query = f"{base_query} WHERE {' AND '.join(test)}"
            print(query)
        else:
            query = base_query

        result = dbm.query(query, [])
        print("result", result)
        material_data = [list(row) for row in result]
        # self.root.send_(json.dumps(material_data, ensure_ascii=False))

        if query:
            return {'sign': 1, "data": material_data}
        else:
            return {'sign': 0, "data": []}

    @staticmethod
    @MsgProcessor
    def f20405(**kwargs):
        query = "SELECT Customer_name, Customer_code FROM customer_management"
        result = dbm.query(query, [])
        search_data = result
        material_data = [list(row) for row in search_data]

        if result is not None:
            return {'sign': 1, "data": material_data}
        if result is None:
            return {'sign': 0, "data": []}


###############################구매요청서############################
    @staticmethod
    @MsgProcessor
    def f20501(**kwargs):
        DataBase = dbm
        condition = ''

        def select_data(condition):
            selected_data = DataBase.query(f"""
            SELECT p.po_num, p.manufactoring_code,
                   p.manager, e.name, p.department,
                   p.created_by, p.created_on, p.changed_by, p.changed_on,
                   p.del_flag
              FROM erp_db.purchasing_order as p LEFT OUTER JOIN erp_db.employee as e
                ON p.manager = e.employee_code
             WHERE {condition}
               AND p.stat = 'H';
            """)  # HEADER인 데이터만 가져오기

            #날짜필드 변환
            selected_data = [list(i) for i in selected_data]
            for i, v in enumerate(selected_data):
                for j, w in enumerate(v):
                    if type(w) is datetime.datetime:
                        selected_data[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

            return selected_data

        for key, value in kwargs.items():
            if key == 'po_num':
                if '%' in value:
                    condition += f"p.po_num like '{value}' and "
                else:
                    condition += f"p.po_num='{value}' and "

            elif key == 'created_on':
                condition += f"DATE(p.created_on)>='{value.split('~')[0]}' and DATE(p.created_on)<='{value.split('~')[1]}'"

            elif key == 'vendor':
                if '%' in value:
                    condition += f" and p.vendor like '{value}'"
                else:
                    condition += f" and p.vendor='{value}'"

            elif key == 'department':
                if '%' in value:
                    condition += f" and p.department like '{value}'"
                else:
                    condition += f" and p.department='{value}'"

            elif key == 'manager':
                if '%' in value:
                    condition += f" and p.manager like '{value}'"
                else:
                    condition += f" and p.manager='{value}'"

        print('condition:', condition)
        test_data = select_data(condition)
        # 실패:0, 성공:1
        if test_data != None:
            return {"sign": 1, "data": test_data}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20511(**kwargs):
        DataBase = dbm
        condition = ''

        def select_data(condition):
            selected_data = DataBase.query(f"""
                    SELECT po.po_num, m.materialType, po.mat_code, m.materialName,
                           po.vendor, v.Customer_name,
                           po.quantity, po.measure, po.amount, po.measure, po.plant,
                           p.plant_name, po.manufactoring_code,
                           po.created_by, po.created_on, po.changed_by, po.changed_on, po.del_flag
                      FROM erp_db.purchasing_order AS po LEFT OUTER JOIN erp_db.materialtable AS m
                        ON po.mat_code = m.materialCode LEFT OUTER JOIN erp_db.plant AS p
                        ON po.plant = p.plant_code      LEFT OUTER JOIN erp_db.Customer_management as v
                        ON po.vendor = v.ID
                     WHERE {condition}
                     ORDER BY po.po_num;
                    """)

            selected_data = [list(i) for i in selected_data]
            for i, v in enumerate(selected_data):
                for j, w in enumerate(v):
                    if type(w) is datetime.datetime:
                        selected_data[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

            return selected_data

        for key, value in kwargs.items():
            # 백업 후, req라는 데이터가 들어오므로, req는 빼준다.
            if key != 'req':
                cond = str(value).replace('[', '(')
                cond = cond.replace(']', ')')
                condition += f"po_num IN {cond}"

        test_data = select_data(condition)
        # 실패:0, 성공:1
        if test_data != None:
            return {"sign": 1, "data": test_data}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20521(**kwargs):
        DataBase = dbm
        condition = ''

        # 생산지시서코드로 BOM코드 가져오기
        for key, value in kwargs.items():
            # 백업 후, req라는 데이터가 들어오므로, req는 빼준다.
            if key != 'req':
                selected_data = DataBase.query(f"""select m.materialType, b.material_code, m.materialName, m.correspondentCode,
                                                    c.Customer_name, b.quantity, m.unit, m.price
                                              from erp_db.bom_f as b left outer join erp_db.materialtable as m
                                                on b.material_code=m.materialCode
                                                                     left outer join erp_db.customer_management as c
                                                on m.correspondentCode = c.ID
                                            where b.bom_code=(select bom_code from erp_db.mo where mo_code='{value}');""")
        print(selected_data)

        if selected_data != None:
            return {"sign": 1, "data": selected_data}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20531(**kwargs):
        DataBase = dbm
        max_code = int(DataBase.query(f"SELECT max(po_num) FROM erp_db.purchasing_order;")[0][0][2:6]) + 1

        if max_code != None:
            return {"sign": 1, "data": max_code}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20502(**kwargs):
        DataBase = dbm
        condition = ''

        def insert_data(condition):
            selected_data = DataBase.query(f"INSERT INTO `erp_db`.`purchasing_order` VALUES ({condition});")
            return selected_data

        for key, value in kwargs.items():
            # 백업 후, req라는 데이터가 들어오므로, req는 빼준다.
            if key != 'req':
                if value != None:
                    condition += f"'{value}'"
                else:
                    condition += "NULL"

                if key != 'stat':
                    condition += ','

        print('condition', condition)
        result = insert_data(condition)
        # 실패:0, 성공:1
        if result != None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20503(**kwargs):
        DataBase = dbm
        condition = ''

        def delete_data(condition):
            selected_data = DataBase.query(f"UPDATE `erp_db`.`purchasing_order` SET `del_flag`='X' WHERE ({condition});")
            return selected_data

        def select_data():
            selected_data = DataBase.query(f"SELECT * FROM erp_db.purchasing_order")
            selected_data = [list(i) for i in selected_data]
            for i, v in enumerate(selected_data):
                for j, w in enumerate(v):
                    if type(w) is datetime.datetime:
                        selected_data[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")
            return selected_data

        for key, value in kwargs.items():
            # 백업 후, req라는 데이터가 들어오므로, req는 빼준다.
            if key != 'req':
                if type(kwargs['po_num']) is str:
                    condition = f"po_num='{value}'"
                else:
                    condition = f"po_num IN {value}"

        result = delete_data(condition)
        test_data = select_data()
        # 실패:0, 성공:1
        if result != None:
            return {"sign": 1, "data": test_data}
        else:
            return {"sign": 0, "data": None}
###########################################################

    @staticmethod
    @MsgProcessor
    def f20601(**kwargs):
        result = {
            "sign": 1,
            "data": "20601"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f20602(**kwargs):
        result = {
            "sign": 1,
            "data": "20602"
        }
        return result

##창고조회############################################
    @staticmethod
    @MsgProcessor
    def f20651(**kwargs):
        DataBase = dbm
        condition = ''

        def select_data(condition):
            selected_data = DataBase.query(f"SELECT * FROM erp_db.plant WHERE {condition};")
            selected_data = [list(i) for i in selected_data]
            for i, v in enumerate(selected_data):
                for j, w in enumerate(v):
                    if type(w) is datetime.datetime:
                        selected_data[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

            return selected_data

        for key, value in kwargs.items():
            if key == 'plant_code':
                condition += f"plant_code='{value}' and "

            elif key == 'created_on':
                condition += f"DATE(created_on)>='{value.split('~')[0]}' and DATE(created_on)<='{value.split('~')[1]}'"

            elif key == 'plant_name':
                if '%' in value:
                    condition += f" and plant_name like '{value}'"
                else:
                    condition += f" and plant_name='{value}'"

            elif key == 'created_by':
                if '%' in value:
                    condition += f" and created_by like '{value}'"
                else:
                    condition += f" and created_by='{value}'"


        print('condition:', condition)
        test_data = select_data(condition)
        # 실패:0, 성공:1
        if test_data != None:
            return {"sign": 1, "data": test_data}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20652(**kwargs):
        DataBase = dbm
        condition = ''

        def select_data():
            selected_data = DataBase.query(f"SELECT * FROM erp_db.plant;")
            selected_data = [list(i) for i in selected_data]
            for i, v in enumerate(selected_data):
                for j, w in enumerate(v):
                    if type(w) is datetime.datetime:
                        selected_data[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")


            return selected_data

        def insert_data(condition):
            selected_data = DataBase.query(f"INSERT INTO `erp_db`.`plant` VALUES ({condition});")
            return selected_data

        for key, value in kwargs.items():
            if value != None:
                condition += f"'{value}'"
            else:
                condition += "NULL"

            if key != 'del_flag':
                condition += ','

        result = insert_data(condition)
        test_data = select_data()
        # 실패:0, 성공:1
        if result != None:
            return {"sign": 1, "data": test_data}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20653(**kwargs):
        DataBase = dbm
        condition = ''

        def update_data(condition, key):
            selected_data = DataBase.query(f"""
                                   UPDATE `erp_db`.`plant`
                                   SET {condition}
                                   WHERE plant_code = '{key}';""")
            return selected_data

        def select_data():
            selected_data = DataBase.query(f"SELECT * FROM erp_db.plant;")

            selected_data = [list(i) for i in selected_data]
            for i, v in enumerate(selected_data):
                for j, w in enumerate(v):
                    if type(w) is datetime.datetime:
                        selected_data[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

            return selected_data

        for key, value in kwargs.items():
            if key != 'changed_on':
                if value == None:
                    condition += (f"{key}=null,")
                else:
                    condition += (f"{key}='{value}',")
            else:
                condition += (f"{key}='{value}'")

        result = update_data(condition, kwargs['plant_code'])
        test_data = select_data()
        # 실패:0, 성공:1
        if result != None:
            return {"sign": 1, "data": test_data}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20654(**kwargs):
        DataBase = dbm
        condition = ''

        def delete_data(condition):
            selected_data = DataBase.query(f"UPDATE `erp_db`.`plant` SET `del_flag`='X' WHERE ({condition});")
            return selected_data

        def select_data():
            selected_data = DataBase.query(f"SELECT * FROM erp_db.plant")
            selected_data = [list(i) for i in selected_data]
            for i, v in enumerate(selected_data):
                for j, w in enumerate(v):
                    if type(w) is datetime.datetime:
                        selected_data[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")
            return selected_data

        for key, value in kwargs.items():
            if type(kwargs['plant_code']) is str:
                condition = f"plant_code='{value}'"
            else:
                condition = f"plant_code IN {value}"

        result = delete_data(condition)
        test_data = select_data()
        # 실패:0, 성공:1
        if result != None:
            return {"sign": 1, "data": test_data}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20655(**kwargs):
        DataBase = dbm
        condition = ''

        max_code = int((DataBase.query('select max(plant_code) from erp_db.plant;'))[0][0][1:4]) + 1

        # 실패:0, 성공:1
        if max_code != None:
            return {"sign": 1, "data": max_code}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20656(**kwargs):
        DataBase = dbm
        selected_data = DataBase.query(f"SELECT plant_code FROM erp_db.plant;")

        if selected_data != None:
            return {"sign": 1, "data": selected_data}
        else:
            return {"sign": 0, "data": None}



##창고조회############################################

    @staticmethod
    @MsgProcessor
    def f20605(**kwargs):  # 창고 기록 조회
        base_query = "SELECT material_code, material_name, material_type, plant_name, plant_code, plant_location, quantity, price, unit FROM plant_material"
        conditions = []
        params = []
        for key, value in kwargs.items():
            if value:  # 값이 비어 있지 않은 경우에만 조건 추가
                conditions.append(f"{key} LIKE %s")
                params.append(f"%{value}%")

        if conditions:
            query = f"{base_query} WHERE {' AND '.join(conditions)}"
        else:
            query = base_query  # 조건이 없으면 전체 조회

        print(f"SQL Query: {query}, Params: {params}")
        result = dbm.query(query, params)

        if result:
            material_data = [list(row) for row in result]  # 검색된 데이터를 리스트로 변환
            return {'sign': 1, "data": material_data}
        else:
            return {'sign': 0, "data": []}

    @staticmethod
    @MsgProcessor
    def f20606(**kwargs):  # 입고기록 조회일경우
        query = """
                                  SELECT receiving.material_code, receiving.material_name, receiving.receiving_classification,
                                         plant.plant_name, plant.plant_code, plant.location,
                                         receiving.quantity,receiving.price, receiving.unit
                                  FROM receiving
                                  JOIN plant ON receiving.plant_code = plant.plant_code
                              """
        result = dbm.query(query, [])  # 만약 성공이면 데이터가 아니면 None이 result에 들어옴
        print("result", result)
        if result is not None:
            material_data = [list(row) for row in result]  # 성공했으면 result를 리스트 형태로 변화
            return {'sign': 1, "data": material_data}
        else:
            return {'sign': 0, "data": []}


    @staticmethod
    @MsgProcessor
    def f20608(**kwargs):
        if kwargs.get("check") == 'M':
            query = """
                         UPDATE erp_db.plant_material
                         SET material_name = %s, material_type = %s, plant_name = %s, plant_code = %s,
                             plant_location = %s, quantity = %s, price = %s, unit = %s
                         WHERE material_code = %s
                     """
            params = [
                kwargs.get("material_name"), kwargs.get("material_type"),
                kwargs.get("plant_name"), kwargs.get("plant_code"),
                kwargs.get("plant_location"), kwargs.get("quantity"),
                int(kwargs.get("price")),
                kwargs.get("unit"),
                kwargs.get("material_code"),
            ]
            print(f"🛠 UPDATE params 확인: {params}")

            result = dbm.query(query, tuple(params))

            if result is not None:
                return {'sign': 1, "data": []}
            else:
                return {'sign': 0, "data": []}

        if kwargs.get("check") == 'C':
            query = """
                         INSERT INTO erp_db.plant_material (material_code, material_name, material_type, plant_name, plant_code,
                             plant_location, quantity, price, unit)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                     """
            params = [
                kwargs.get("material_code"), kwargs.get("material_name"), kwargs.get("material_type"),
                kwargs.get("plant_name"), kwargs.get("plant_code"),
                kwargs.get("plant_location"), kwargs.get("quantity"),
                int(kwargs.get("price")),
                kwargs.get("unit"),
            ]
            print(f"🛠 INSERT params 확인: {params}")

            result = dbm.query(query, tuple(params))

            if result is not None:
                return {'sign': 1, "data": []}
            else:
                return {'sign': 0, "data": []}

    @staticmethod
    @MsgProcessor
    def f20701(**kwargs):  # 발주번호 외 나머지 조회시
        result = None
        data_dict = kwargs

        for key, value in data_dict.items():
            if key == "0" or value == 0:
                result = dbm.query(f"SELECT * FROM shipping;")
            else:
                result = dbm.query(f"SELECT * FROM shipping where {key} = '{value}';")

        if result:
            result_dict = {"sign": 1, "data": list(result)}
        else:
            result_dict = {"sign": 0, "data": None}

        return result_dict

    @staticmethod
    @MsgProcessor
    def f20703(**kwargs):  # 저장시 값 db 추가
        save_dict = kwargs
        data_list = list(save_dict.values())

        insert_query = """
                INSERT INTO shipping (shipping_code, order_code, material_classification, quantity, unit, selling_price, vat_price, total_price, material_code, material_name, sales_order_number, purchase_order_code, client_code, client_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        dbm.transaction([(insert_query, tuple(data_list))])

        result = {"sign": 1, "data": None}
        return result

    @staticmethod
    @MsgProcessor
    def f20704(**kwargs):  # 값 수정
        send_data = kwargs

        update_cases = {}
        shipping_codes = set()

        for key, (shipping_code, column, value) in send_data.items():
            if column not in update_cases:
                update_cases[column] = []
            update_cases[column].append(f"WHEN shipping_code = '{shipping_code}' THEN '{value}'")
            shipping_codes.add(f"'{shipping_code}'")  # WHERE 절에 들어갈 shipping_code 값들

        if not shipping_codes:
            return {"sign": 0, "data": None}

        update_sql = "UPDATE shipping SET \n"
        update_sql += ",\n".join([
            f"{column} = CASE \n" + "\n".join(conditions) + "\nEND"
            for column, conditions in update_cases.items()
        ])
        update_sql += f"\nWHERE shipping_code IN ({', '.join(shipping_codes)});"
        result = dbm.query(update_sql)
        print("결과", result)
        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20705(**kwargs):  # 전체 데이터 가져오기
        result = None
        for key, value in kwargs.items():
            result = dbm.query(f"SELECT {value} FROM {key}")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20706(**kwargs):  # 서브테이블 전체 데이터 가져오기
        result = None
        for key, value in kwargs.items():
            result = dbm.query(f"SELECT {value} FROM {key}")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20707(**kwargs):  # 메인테이블 컬럼 가져오기
        result = dbm.query(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = '{kwargs.get("tablename")}' ORDER BY ORDINAL_POSITION;")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20708(**kwargs):  # 서브테이블 컬럼 가져오기
        result = dbm.query(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = '{kwargs.get("tablename")}' ORDER BY ORDINAL_POSITION;")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20709(**kwargs):  # 서브 테이블 데이터 가져오기
        result_dict = {}
        data_dict = kwargs
        result = None
        for key, value in data_dict.items():
            result = dbm.query(f"SELECT * FROM mo where {key} = '{value}';")

        if result:
            result_dict = {"sign": 1, "data": list(result)}
        else:
            result_dict = {"sign": 0, "data": None}

        return result_dict

    @staticmethod
    @MsgProcessor
    def f20710(**kwargs):  # materialtable 컬럼 가져오기
        result = dbm.query(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = 'materialtable' ORDER BY ORDINAL_POSITION;")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20711(**kwargs):  # materialtable 테이블 데이터 가져오기
        result = None
        result_list = []

        result = dbm.query(f"SELECT * FROM materialtable")

        for i in result:
            result_list.append(list(i))

        for i, v in enumerate(result_list):
            for j, w in enumerate(v):
                if type(w) is datetime.datetime:
                    result_list[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

        if result_list is not None:
            return {"sign": 1, "data": result_list}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20801(**kwargs):  # 발주번호 외 나머지 조회시
        result_dict = {}
        result = None
        data_dict = kwargs

        for key, value in data_dict.items():
            if key == "0" or value == 0:
                result = dbm.query(f"SELECT * FROM receiving;")
            else:
                result = dbm.query(f"SELECT * FROM receiving where {key} = '{value}';")

        if result is not None:
            result_dict = {"sign": 1, "data": list(result)}
        else:
            result_dict = {"sign": 0, "data": None}

        return result_dict

    @staticmethod
    @MsgProcessor
    def f20803(**kwargs):  # 저장시 값 db 추가
        save_dict = kwargs
        data_list = list(save_dict.values())

        insert_query = """
           INSERT INTO receiving (receiving_code, order_code, receiving_classification, client_code, client_name, quantity, unit, material_code, material_name, receiving_responsibility, purchase_order_code, plant_code, price)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
       """
        result = dbm.transaction([(insert_query, tuple(data_list))])

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20804(**kwargs):  # 값 수정
        send_data = kwargs

        update_cases = {}
        receiving_codes = set()

        for key, (receiving_code, column, value) in send_data.items():
            if column == "plant_code":
                return {"sign": 1, "data": None}
            if column not in update_cases:
                update_cases[column] = []
            update_cases[column].append(f"WHEN receiving_code = '{receiving_code}' THEN '{value}'")
            receiving_codes.add(f"'{receiving_code}'")

        if not receiving_codes:
            return {"sign": 0, "data": None}

        update_sql = "UPDATE receiving SET \n"
        update_sql += ",\n".join([
            f"{column} = CASE \n" + "\n".join(conditions) + "\nEND"
            for column, conditions in update_cases.items()
        ])
        update_sql += f"\nWHERE receiving_code IN ({', '.join(receiving_codes)});"
        result = dbm.query(update_sql)
        print("결과", result)
        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}


    @staticmethod
    @MsgProcessor
    def f20805(**kwargs):  # 전체 데이터 가져오기
        result = None
        for key, value in kwargs.items():
            result = dbm.query(f"SELECT {value} FROM {key}")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20806(**kwargs):  # mo 서브테이블 전체 데이터 가져오기
        result = None
        for key, value in kwargs.items():
            result = dbm.query(f"SELECT {value} FROM {key}")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20807(**kwargs):  # 메인테이블 컬럼 가져오기
        result = dbm.query(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = '{kwargs["tablename"]}' ORDER BY ORDINAL_POSITION;")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20808(**kwargs):  # mo 서브테이블 컬럼 가져오기
        result = dbm.query(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = '{kwargs["tablename"]}' ORDER BY ORDINAL_POSITION;")

        if result is not None:
            return {"code": 20808, "sign": 1, "data": result}
        else:
            return {"code": 20808, "sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20809(**kwargs):  # mo 서브 테이블 조건 조회 데이터 가져오기
        result = None
        data_dict = kwargs

        for key, value in data_dict.items():
            result = dbm.query(f"SELECT * FROM mo where {key} = '{value}';")

        if result is not None:
            result_dict = {"sign": 1, "data": list(result)}
        else:
            result_dict = {"sign": 0, "data": None}

        return result_dict

    @staticmethod
    @MsgProcessor
    def f20810(**kwargs):  # purchasing_order 서브 테이블 조건 조회 데이터 가져오기
        result_dict = {}
        data_dict = kwargs

        result = None
        result_list = []

        for key, value in data_dict.items():
            result = dbm.query(f"SELECT * FROM purchasing_order where {key} = '{value}';")

        for i in result:
            result_list.append(list(i))

        for i, v in enumerate(result_list):
            for j, w in enumerate(v):
                if type(w) is datetime.datetime:
                    result_list[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

        if result is not None:
            result_dict = {"sign": 1, "data": result_list}
        else:
            result_dict = {"sign": 0, "data": None}

        return result_dict

    @staticmethod
    @MsgProcessor
    def f20811(**kwargs):  # purchasing 서브테이블 전체 데이터 가져오기
        result = None
        result_list = []
        for key, value in kwargs.items():
            result = dbm.query(f"SELECT {value} FROM {key}")

        for i in result:
            result_list.append(list(i))

        for i, v in enumerate(result_list):
            for j, w in enumerate(v):
                if type(w) is datetime.datetime:
                    result_list[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

        if result_list is not None:
            return {"sign": 1, "data": result_list}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20812(**kwargs): #purchasing 서브테이블 컬럼 가져오기
        result = dbm.query(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = '{kwargs["tablename"]}' ORDER BY ORDINAL_POSITION;")

        for i, v in enumerate(result):
            for j, w in enumerate(v):
                if type(w) is datetime.datetime:
                    result[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20813(**kwargs):  # materialtable 컬럼 가져오기
        result = dbm.query(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = 'materialtable' ORDER BY ORDINAL_POSITION;")

        if result is not None:
            return {"sign": 1, "data": result}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20814(**kwargs):  # materialtable 테이블 데이터 가져오기
        result = None
        result_list = []

        result = dbm.query(f"SELECT * FROM materialtable")

        for i in result:
            result_list.append(list(i))

        for i, v in enumerate(result_list):
            for j, w in enumerate(v):
                if type(w) is datetime.datetime:
                    result_list[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")

        if result_list is not None:
            return {"sign": 1, "data": result_list}
        else:
            return {"sign": 0, "data": None}


    @staticmethod
    @MsgProcessor
    def f20815(**kwargs):  # purchasing_order에 plant 값 바꾸기
        result = None

        for po_num, plant in kwargs.items():
            result = dbm.query(f"UPDATE purchasing_order SET plant = '{plant}' WHERE po_num = '{po_num}'")

        if result is not None:
            return {"sign": 1, "data": []}
        else:
            return {"sign": 0, "data": None}


    @staticmethod
    @MsgProcessor
    def f20816(**kwargs):  # receiving 에 plant_code 값 바꾸기
        result = None

        for receiving_code, plant in kwargs.items():
            result = dbm.query(f"UPDATE receiving SET plant_code = '{plant}' WHERE receiving_code = '{receiving_code}'")

        if result is not None:
            return {"sign": 1, "data": []}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f20901(**kwargs):
        result = {
            "sign": 1,
            "data": "20901"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f30101(**kwargs):
        # aa = kwargs.get("거")
        result = dbm.query(
            f"INSERT INTO Customer_management VALUES (NULL, '{kwargs.get("Customer_name")}', '{kwargs.get("business_number")}', '{kwargs.get("Customer_code")}', '{kwargs.get("Type_business")}', '{kwargs.get("business_adress1")} {kwargs.get("business_adress2")}', '{kwargs.get("ContactPerson_name")}', '{kwargs.get("Country")}', '{kwargs.get("ContactPerson_phone")}', '{kwargs.get("e_mail")}', '{kwargs.get("Memo")}');")

        if result is not None:
            result = {"sign": 1, "data": result}
        else:
            result = {"sign": 0, "data": None}

        return result

    @staticmethod
    @MsgProcessor
    def f30102(**kwargs):
        if kwargs:
            data = dbm.query(
                f"SELECT Customer_name, business_number, Customer_code, Type_business, business_adress, ContactPerson_name, ContactPerson_phone, e_mail from Customer_management WHERE Customer_name LIKE '%{kwargs.get("Customer_name")}%'")
        else:
            data = dbm.query(
                'select Customer_code, Customer_name, business_number, ContactPerson_name from Customer_management;')
        # result=dbm.query(f"SELECT Customer_name, business_number, Customer_code, Type_business, business_adress, ContactPerson_name, ContactPerson_phone, e_mail from Customer_management WHERE Customer_name LIKE '%{kwargs.get("Customer_name")}%' or business_number LIKE '%{kwargs.get("business_number")}%' or Customer_code LIKE '%{kwargs.get("Customer_code")}%' or Country LIKE '%{kwargs.get("Country")}%'")
        print("결과 : ", data)
        if data is not None:
            result = {"sign": 1, "data": data}
        else:
            result = {"sign": 0, "data": None}

        return result

    @staticmethod
    @MsgProcessor
    def f30103(**kwargs):
        result = {
            "sign": 1,
            "data": "30103"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f30104(**kwargs):
        result = {
            "sign": 1,
            "data": "30104"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f30201(**kwargs): #history
        input_value = kwargs.get("input", "")
        select_value = kwargs.get("select_value", 1)

        column1 = {
            1: "Customer_management.Customer_name",
            2: "Customer_management.business_number",
            3: "Customer_management.Customer_code"
        }

        column = column1.get(select_value, "Customer_management.Customer_name")

        query = f"SELECT order_form.creation_date, Customer_management.Customer_name, Customer_management.business_number, Customer_management.Customer_code, Customer_management.Type_business, Customer_management.Country, order_form.product_name, order_form.transaction_quantity,order_form.unit_price, order_form.total_price FROM Customer_management INNER JOIN order_form ON Customer_management.Customer_code = order_form.Customer_code WHERE {column} LIKE %s AND order_form.creation_date BETWEEN '{kwargs.get("date1")}' AND '{kwargs.get("date2")}'"

        result = dbm.query(query, (f"%%{input_value}%%",))

        result = [[str(j) for j in list(i)] for i in result]

        if result is not None:
            result = {"sign": 1, "data": result}
        else :
            result = {"sign": 0, "data": None}

        return result

    # 발주서 조회
    @staticmethod
    @MsgProcessor
    def f30301(**kwargs):
      # DB 연결
      # 조회할 컬럼
      columns = [
        'o.creation_date', 'o.order_code', 'o.internal_external', 'o.creator_name', 'o.administrator_name',
        'o.product_code', 'o.product_name', 'o.unit_price', 'o.transaction_quantity', 'o.total_price',
        'o.order_vat',
        'o.Customer_code', 'c.Customer_name', 'c.Type_business', 'c.ContactPerson_name', 'o.delivery_date',
        'o.modified_date'
      ]

      # 기본 쿼리
      sql_query = f'''
            SELECT {", ".join(columns)}
            FROM erp_db.order_form o
            INNER JOIN erp_db.customer_management c
            ON o.Customer_code = c.Customer_code
        '''

      conditions = []  # 조건 리스트 초기화
      start_value, end_value = None, None  # 날짜 변수 초기화

      for key, value in kwargs.items():
        print("select:", key, value)
        if value is not None:
          column_name = key  # 기본적으로 key를 column_name으로 설정

          # 시작 날짜 처리 (start와 관련된 처리)
          if "start" in key:
            start_value = value
            column_name = key.replace('_start', '')  # '_start'를 제거하여 실제 컬럼명 추출
            if start_value:
              current_date = datetime.datetime.now().strftime('%Y-%m-%d')
              if start_value != current_date:  # 오늘 날짜가 아니면 조건 추가
                conditions.append(f"o.{column_name} >= '{start_value} 00:00:00'")

          # 종료 날짜 처리 (end와 관련된 처리)
          elif "end" in key:
            end_value = value
            column_name = key.replace('_end', '')  # '_end'를 제거하여 실제 컬럼명 추출
            if end_value:
              if start_value == end_value:
                # start와 end 값이 같으면 조건을 추가하지 않음
                continue
              conditions.append(f"o.{column_name} <= '{end_value} 23:59:59'")

          # 일반적인 값 비교 처리
          elif isinstance(value, str):  # 문자열일 때 LIKE 조건
            conditions.append(f"o.{column_name} LIKE '%{value}%'")
          else:  # 문자열이 아닐 때 (정확한 값 비교)
            conditions.append(f"o.{column_name} = '{value}'")

      # WHERE 절이 존재할 경우 조건
      if conditions:
        sql_query += " WHERE " + " AND ".join(conditions)

      # 최종 SQL 쿼리
      print("쿼리:", sql_query)
      result = dbm.query(sql_query)
      print(result)

      if result is not None:
        # datetime 문자열
        result = [
          tuple(item.strftime('%Y.%m.%d') if isinstance(item, datetime.datetime) else item for item in row)
          for row in result  # row에 값 넣고 item의 값을 하나씩 빼서 처리
        ]
        sign = 1
      else:
        print("오류:", result)
        sign = 0

      # 결과 반환
      recv = {
        "sign": sign,
        "data": result if result else []  # 결과가 없으면 빈 리스트 반환
      }
      print(recv)

      return recv


    # 발주서 생성
    @staticmethod
    @MsgProcessor
    def f30302(**kwargs):
      # DB 연결
      # 컬럼 목록
      columns = [
        'order_code', 'product_code', 'product_name', 'internal_external', 'creator_name', 'creator_position',
        'creator_phone', 'creator_email', 'administrator_name', 'administrator_position',
        'administrator_phone', 'administrator_email', 'unit_price', 'transaction_quantity', 'total_price',
        'order_vat', 'Customer_code', 'sledding', 'delivery_date', 'creation_date'
      ]

      values = []
      columns_to_insert = []
      print("kwargs :", kwargs.get('args'))

      Customer_code = kwargs.get("Customer_code")
      print(Customer_code)

      # Customer_code 유효성 검사
      if Customer_code:
        check_query = f"SELECT COUNT(*) FROM erp_db.customer_management WHERE Customer_code = '{Customer_code}'"
        check_result = dbm.query(check_query)

        if check_result and check_result[0][0] == 0:
          print(f"Customer_code '{Customer_code}'가 존재하지 않습니다.")
          return {"sign": 0, "data": {}}

      # kwargs에서 컬럼 값들을 처리
      for key, value in kwargs.items():
        if key in columns and value is not None:
          columns_to_insert.append(key)
          if value is None:
            values.append("NULL")
          elif isinstance(value, (int, float)):
            values.append(str(value))
          elif isinstance(value, str):
            values.append(f"'{value}'")
          else:
            print(f"예상치 못한 값: {key} = {value}")
            values.append("NULL")

      sql_query = f"""
            INSERT INTO erp_db.order_form ({', '.join(columns_to_insert)})
            VALUES ({', '.join(values)})
        """

      print("쿼리:", sql_query)
      result = dbm.query(sql_query)
      print(result)

      sign = 1 if result is not None else 0

      recv = {
        "sign": sign,
        "data": {}
      }

      print(recv)
      return recv

    #발주서 수정
    @staticmethod
    @MsgProcessor
    def f30303(**kwargs):
      # 초기화
      values = []
      Customer_code = kwargs.get("Customer_code")
      print(Customer_code)

      # Customer_code 유효성 검사
      if Customer_code:
        check_query = f"SELECT COUNT(*) FROM erp_db.customer_management WHERE Customer_code = '{Customer_code}'"
        check_result = dbm.query(check_query)

        if check_result and check_result[0][0] == 0:
          print(f"Customer_code '{Customer_code}'가 존재하지 않습니다.")
          return {"sign": 0, "data": {}}

      for key, value in kwargs.items():
        if value not in [None, '']:  # 값이 None이 아니고 빈 문자열이 아닐 때만 처리
          values.append(f"{key} = '{value}'")
      sql_query = f"UPDATE erp_db.order_form SET "
      sql_query += ", ".join(values)
      sql_query += f" WHERE order_code = '{kwargs['order_code']}'"
      result = dbm.query(sql_query)
      # 쿼리 실행
      if result is not None:
        sign = 1
      else:
        print("오류:", result)
        sign = 0
      # 결과 반환
      recv = {"sign": sign, "data": []}
      return recv

    #발주서 삭제
    @staticmethod
    @MsgProcessor
    def f30304(**kwargs):
      order_code = kwargs.get("order_code")  # 발주 코드 가져오기
      if not order_code:  # order_code가 없으면 오류
        print("sign: 0", "message: 발주 코드가 없습니다.")

      # DELETE 쿼리 (발주 코드 리스트 조건)
      sql_query = f"DELETE FROM order_form WHERE order_code IN ('{order_code}')"
      result = dbm.query(sql_query)
      print(result)
      if result:
        sign = 0
      else:
        sign = 1
      # 결과 반환
      recv = {"sign": sign, "data": []}
      print("recv:", recv)
      return recv

    @staticmethod
    @MsgProcessor
    def f30401(**kwargs):
        # 조회할 컬럼
        columns = [
            'order_form.order_code', 'order_form.internal_external', 'order_form.creator_name',
            'order_form.creator_position',
            'order_form.creator_phone', 'order_form.creator_email', 'order_form.administrator_name',
            'order_form.administrator_position',
            'order_form.administrator_phone', 'order_form.administrator_email', 'order_form.product_code',
            'order_form.product_name',
            'order_form.unit_price', 'order_form.transaction_quantity', 'order_form.total_price',
            'order_form.order_vat',
            '(order_form.unit_price * order_form.transaction_quantity) - order_form.order_vat AS NetProfit',
            # 순이익 계산
            'order_form.Customer_code', 'customer_management.business_number', 'customer_management.Customer_name',
            'customer_management.Type_business',
            'customer_management.business_adress', 'customer_management.ContactPerson_name',
            'customer_management.ContactPerson_phone', 'customer_management.e_mail',
            'order_form.delivery_date', 'order_form.creation_date', 'order_form.modified_date'
        ]

        # 기본 쿼리 (order_form 테이블과 customer_management 테이블을 JOIN)
        sql_query = f"""
        SELECT
            {", ".join(columns)}
            FROM erp_db.order_form
            INNER JOIN erp_db.customer_management
            ON order_form.Customer_code = customer_management.Customer_code
        """

        conditions = []  # 조건 리스트 초기화
        start_value, end_value = None, None  # 날짜 변수 초기화

        # kwargs에서 조건 처리
        for key, value in kwargs.items():
            print("select:", key, value)
            if value:  # None 또는 빈 문자열을 제외하고 처리
                column_name = key  # 기본적으로 key를 column_name으로 설정

                # 시작 날짜 처리 (start와 관련된 처리)
                if "start" in key:
                    start_value = value
                    column_name = key.replace('_start', '')  # '_start'를 제거하여 실제 컬럼명 추출
                    if start_value:
                        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                        if start_value != current_date:  # 오늘 날짜가 아니면 조건 추가
                            conditions.append(f"{column_name} >= '{start_value} 00:00:00'")

                # 종료 날짜 처리 (end와 관련된 처리)
                elif "end" in key:
                    end_value = value
                    column_name = key.replace('_end', '')  # '_end'를 제거하여 실제 컬럼명 추출
                    if end_value:
                        if start_value == end_value:
                            # start와 end 값이 같으면 조건을 추가하지 않음
                            continue
                        conditions.append(f"{column_name} <= '{end_value} 23:59:59'")

                # 일반적인 값 비교 처리
                elif isinstance(value, str):  # 문자열일 때 LIKE 조건
                    conditions.append(f"{column_name} LIKE '%{value}%'")
                else:  # 문자열이 아닐 때 (정확한 값 비교)
                    conditions.append(f"{column_name} = '{value}'")

        # WHERE 절이 존재할 경우 조건 추가
        if conditions:
            sql_query += " WHERE " + " AND ".join(conditions)

        # 최종 SQL 쿼리
        print("쿼리:", sql_query)
        result = dbm.query(sql_query)
        print(result)

        if result is not None:
            # datetime 문자열 형식 변경
            result = [
                tuple(item.strftime('%Y.%m.%d') if isinstance(item, datetime.datetime) else item for item in row)
                for row in result  # row에 값 넣고 item의 값을 하나씩 빼서 처리
            ]
            sign = 1
        else:
            print("오류:", result)
            sign = 0

        # 결과 반환
        recv = {
            "sign": sign,
            "data": result if result else []  # 결과가 없으면 빈 리스트 반환
        }
        print(recv)

        return recv

    # 전표 조회
    @staticmethod
    @MsgProcessor
    def f40101(**kwargs):
        result = {}
        print("f40101 kwargs :", kwargs)
        condQue = 'select * from accountbook'

        conditions = []
        params = []

        if (kwargs.get("시작일자") and kwargs["시작일자"] != "") and (kwargs.get("종료일자") and kwargs["종료일자"] != ""):
            conditions.append("bk_date between %s and %s")
            params.append(kwargs["시작일자"])
            params.append(kwargs["종료일자"])

        elif (kwargs.get("시작일자") and kwargs["시작일자"] != "") and kwargs.get("종료일자") == "":
            conditions.append("bk_date between %s and '2099-12-31'")
            params.append(kwargs["시작일자"])

        elif kwargs.get("시작일자") == "" and (kwargs.get("종료일자") and kwargs["종료일자"] != ""):
            conditions.append("bk_date between '1900-01-01' and %s")
            params.append(kwargs["종료일자"])

        if kwargs.get("승인상태") and kwargs["승인상태"] != "":
            conditions.append("bk_approval_state = %s")
            params.append(kwargs["승인상태"])

        if kwargs.get("전표유형") and kwargs["전표유형"] != "":
            conditions.append("bk_type = %s")
            params.append(kwargs["전표유형"])

        if kwargs.get("전표번호") and kwargs["전표번호"] != "":
            conditions.append("bk_id = %s")
            params.append(kwargs["전표번호"])

        if kwargs.get("작성자") and kwargs["작성자"] != "":
            conditions.append("bk_creater = %s")
            params.append(kwargs["작성자"])

        # 조건이 있는 경우 WHERE 절 추가
        if conditions:
            condQue += " WHERE " + " AND ".join(conditions)

        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')

            rawData = db.query(condQue, params)
            aData = [list(ele) for ele in list(rawData)]
            for i in range(len(aData)):
                if type(aData[i][1]) is datetime.date:
                    aData[i][1] = str(aData[i][1])
                if type(aData[i][5]) is datetime.date:
                    aData[i][5] = str(aData[i][5])
                if type(aData[i][8]) is datetime.date:
                    aData[i][8] = str(aData[i][8])
            result = {"sign": 1, "data": aData}
        except Exception as e:
            print("f40103 error")
            result = {"sign": 0, "data": {}}
            raise e

        finally:
            return result

    # 전표 승인
    @staticmethod
    @MsgProcessor
    def f40102(**kwargs):
        result = {}
        data = kwargs['data']

        try:
            nowdate = str(datetime.datetime.now())[:10]
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            for key in data:
                db.query(
                    f"update accountbook set bk_approval_state='승인',bk_approval_date='{nowdate}' where bk_id = '{key}';")

            result = {"sign": 1, "data": {}}
        except Exception as e:
            print("f40102 error")
            result = {"sign": 0, "data": {}}
            raise e
        finally:
            return result

    # 전표 저장
    @staticmethod
    @MsgProcessor
    def f40103(**kwargs):
        result = {}
        data = kwargs['data']
        # print(data)

        try:
            nowdate = str(datetime.datetime.now())[:10]
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            keys = []
            for i in range(len(data)):
                keys.append(data[i][4])

            for key in keys:
                db.query(f"DELETE FROM accountbook WHERE bk_id = '{key}' and bk_approval_state = '미결';")

            for i in range(len(data)):
                row = data[i]
                db.query(
                    f"insert into accountbook (bk_id, bk_date, bk_type, bk_description, bk_amount,bk_create_date, bk_creater) values ('{row[4]}','{str(row[0])}','{row[1]}','{row[2]}','{row[3]}','{nowdate}','{row[5]}');")

            result = {"sign": 1, "data": {}}
        except Exception as e:
            print("f40103 error")
            result = {"sign": 0, "data": {}}
            raise e

        finally:
            return result

    # 전표 삭제
    @staticmethod
    @MsgProcessor
    def f40104(**kwargs):
        result = {}
        data = kwargs["data"]
        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            for key in data:
                db.query(f"DELETE FROM accountbook WHERE bk_id = '{key}' and bk_approval_state = '미결';")
            result = {"sign": 1, "data": {}}
        except Exception as e:
            print("f40104 error")
            result = {"sign": 0, "data": {}}
            raise e

        finally:
            return result

    # 전표 분개 조회
    @staticmethod
    @MsgProcessor
    def f40105(**kwargs):
        result = {}
        cond = kwargs['전표번호']
        print("cond :", cond)
        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            rawData = db.query(f'select * from journalizingbook where bk_id = "{cond}";')
            data = [list(ele) for ele in list(rawData)]
            result = {
                "sign": 1,
                "data": data
            }
        except Exception as e:
            print("f40105 error")
            result = {'sign': 0, "data": {}}
            raise e
        finally:
            return result

    # 전표 분개저장
    @staticmethod
    @MsgProcessor
    def f40106(**kwargs):
        result = {}
        # print("jrData :",data)
        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            key = None
            values = [[]]
            for k, v in kwargs.items():
                key = k
                values = v

            # AccountBookFrame.f40107(code=40107, args={"전표번호": key})
            db.query(f"DELETE FROM journalizingbook WHERE bk_id = '{key}';")

            for row in range(len(values)):
                # print(f"dr : {values[row][5]}, cr : {values[row][6]}")
                db.query(
                    f'insert into journalizingbook (jr_type, account_code, account_name, business_code, business_client, jr_dr, jr_cr, jr_description, jr_evidence, bk_id, jr_base) values("{values[row][0]}","{values[row][1]}","{values[row][2]}","{values[row][3]}","{values[row][4]}","{values[row][5]}","{values[row][6]}","{values[row][7]}","{values[row][8]}","{key}","bk");')
            result = {'sign': 1, "data": {}}

        except Exception as e:
            print("f40106 error")
            result = {'sign': 0, "data": {}}
            raise e

        finally:
            return result

    # 전표 분개삭제
    @staticmethod
    @MsgProcessor
    def f40107(**kwargs):
        result = {}
        data = kwargs["data"]
        # print("f40107", data)
        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            for key in data:
                db.query(f"DELETE FROM journalizingbook WHERE bk_id = '{key}';")
            result = {"sign": 1, "data": {}}
        except Exception as e:
            print("f40107 error")
            result = {"sign": 0, "data": {}}
            raise e

        finally:
            return result

    # 세금계산서 조회
    @staticmethod
    @MsgProcessor
    def f40201(**kwargs):
        result = {}
        print("f40201 kwargs :", kwargs)
        condQue = 'select * from taxinvoice'

        conditions = []
        params = []

        if (kwargs.get("시작일자") and kwargs["시작일자"] != "") and (kwargs.get("종료일자") and kwargs["종료일자"] != ""):
            conditions.append("ti_create_date between %s and %s")
            params.append(kwargs["시작일자"])
            params.append(kwargs["종료일자"])

        elif (kwargs.get("시작일자") and kwargs["시작일자"] != "") and kwargs.get("종료일자") == "":
            conditions.append("ti_create_date between %s and '2099-12-31'")
            params.append(kwargs["시작일자"])

        elif kwargs.get("시작일자") == "" and (kwargs.get("종료일자") and kwargs["종료일자"] != ""):
            conditions.append("ti_create_date between '1900-01-01' and %s")
            params.append(kwargs["종료일자"])

        if kwargs.get("작성유형") and kwargs["작성유형"] != "":
            conditions.append("ti_type = %s")
            params.append(kwargs["작성유형"])

        if kwargs.get("발행상태") and kwargs["발행상태"] != "":
            conditions.append("ti_publish_state = %s")
            params.append(kwargs["발행상태"])

        if kwargs.get("작성번호") and kwargs["작성번호"] != "":
            conditions.append("ti_id = %s")
            params.append(kwargs["작성번호"])

        # 조건이 있는 경우 WHERE 절 추가
        if conditions:
            condQue += " WHERE " + " AND ".join(conditions)

        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            rawData = db.query(condQue, params)
            aData = [list(ele) for ele in list(rawData)]
            for i in range(len(aData)):
                if type(aData[i][1]) is datetime.date:
                    aData[i][1] = str(aData[i][1])
            result = {'sign': 1, 'data': aData}
        except Exception as e:
            result = {'sign': 0, 'data': {}}
            print("f40201 error")
            raise e
        finally:
            return result

    # 세금계산서 - 저장
    @staticmethod
    @MsgProcessor
    def f40202(**kwargs):
        result = {}
        data = kwargs['data']
        print("f40202 data", data)

        try:
            db = dbm #.DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            keys = []
            for i in range(len(data)):
                keys.append(data[i][10])

            for k in keys:
                db.query(f'delete from taxinvoice where ti_id = "{k}";')

            for i in range(len(data)):
                row = data[i]
                db.query(
                    f"insert into taxinvoice (ti_id, ti_create_date, ti_type, business_client, business_number, ti_description, ti_ori_amount,ti_tax_rate,ti_vat,ti_amount,ti_publish_state) values ('{row[10]}','{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{int(row[5].replace(",", ""))}','{row[6]}','{int(row[7].replace(",", ""))}','{int(row[8].replace(",", ""))}','{row[9]}');")
            result = {'sign': 1, 'data': {}}
        except Exception as e:
            result = {'sign': 0, 'data': {}}
            print("f40202 error")
            raise e
        finally:
            return result

    # 세금계산서 - 발행
    @staticmethod
    @MsgProcessor
    def f40203(**kwargs):
        result = {}

        data = kwargs['data']
        # print("f40203.data", data)
        key = data["작성번호"]
        print("f40203.key :", key)

        try:
            db = dbm #.DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            db.query(f'update taxinvoice set ti_publish_state = "발행" where ti_id = "{key}";')
            result = {'sign': 1, 'data': {}}
        except Exception as e:
            result = {'sign': 0, 'data': {}}
            print("f40203 error")
            raise e
        finally:
            return result

    # 세금계산서 - 세금계산서삭제
    @staticmethod
    @MsgProcessor
    def f40204(**kwargs):
        result = {}
        data = kwargs["data"]
        print("f40204", data)
        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            for key in data:
                db.query(f'delete from taxinvoice where ti_id = "{key}";')  # and ti_publish_state = "None"
            result = {'sign': 1, 'data': {}}
        except Exception as e:
            print("f40204 error")
            result = {'sign': 0, 'data': {}}
            raise e
        finally:
            return result

    # 세금계산서 - 세금계산서삭제
    @staticmethod
    @MsgProcessor
    def f40204(**kwargs):
        result = {}
        data = kwargs["data"]
        print("f40204", data)
        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            for key in data:
                db.query(f'delete from taxinvoice where ti_id = "{key}";')  # and ti_publish_state = "None"
            result = {'sign': 1, 'data': {}}
        except Exception as e:
            print("f40204 error")
            result = {'sign': 0, 'data': {}}
            raise e
        finally:
            return result

    # 세금계산서 - 분개삭제
    @staticmethod
    @MsgProcessor
    def f40205(**kwargs):
        result = {}
        # print("f40205 data:",kwargs)
        cond = kwargs["세금계산서번호"]
        try:
            db = dbm #.DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            rawData = db.query(f'select * from journalizingbook where ti_id = "{cond}";')
            aData = [list(ele) for ele in list(rawData)]
            result = {'sign': 1, 'data': aData}
        except Exception as e:
            result = {'sign': 0, 'data': {}}
            print("f40201 error")
            raise e
        finally:
            return result

    # 세금계산서 분개 저장
    @staticmethod
    @MsgProcessor
    def f40206(**kwargs):
        result = {}
        # print("f40206 kwargs", kwargs)
        key = None
        values = []
        for k, v in kwargs.items():
            key = k
            values = v

        print(key, " / ", values)
        try:
            db = dbm #.DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            db.query(f'delete from journalizingbook where ti_id = "{key}";')

            for row in range(len(values)):
                db.query(
                    f'insert into journalizingbook (jr_type, account_code, account_name, business_code, business_client, jr_dr, jr_cr, jr_description, jr_evidence,ti_id, jr_base) values ("{values[row][0]}","{values[row][1]}","{values[row][2]}","{values[row][3]}","{values[row][4]}","{values[row][5]}","{values[row][6]}","{values[row][7]}","{values[row][8]}","{key}","ti");')

            result = {'sign': 1, 'data': {}}
        except Exception as e:
            print("f40206 errer")
            result = {'sign': 0, 'data': {}}
            raise e
        finally:
            return result

    # 세금계산서 분개 삭제
    @staticmethod
    @MsgProcessor
    def f40207(**kwargs):
        result = {}
        data = kwargs["data"]
        print("f40207", data)
        try:
            db = dbm #.DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            for key in data:
                db.query(f"DELETE FROM journalizingbook WHERE ti_id = '{key}';")
            result = {"sign": 1, "data": {}}
        except Exception as e:
            print("f40207 error")
            result = {"sign": 0, "data": {}}
            raise e

        finally:
            return result

    @staticmethod
    @MsgProcessor
    def f40301(**kwargs):
        result = {
            "sign": 1,
            "data": "40301"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f40302(**kwargs):
        result = {
            "sign": 1,
            "data": "40302"
        }
        return result

    @staticmethod
    @MsgProcessor
    # #서버 >>클라
    def f40401(**kwargs):

        standard_code1 = kwargs.get("기준일자")

        if standard_code1 is None:
            return {"sign": 0, "data": None}

        start = standard_code1[0]
        end = standard_code1[1]  # '2025-03-25'예시

        # accountsubject 테이블에서 account_name과 account_type 조회
        account_data = dbm.query(
            "SELECT account_name, account_type, account_code FROM accountsubject WHERE account_type IN ('자산','부채','자본')"
        )

        if not account_data:
            return {"sign": 0, "data": None}

        # account_name, account_type딕셔너리
        account_dict = {i: [j, k] for i, j, k in account_data}

        # 승인된 전표 bk_id
        data = dbm.query(
            "SELECT bk_id FROM accountbook WHERE (bk_date BETWEEN %(id1)s AND %(id2)s) AND bk_approval_state = '승인'",
            {"id1": start, "id2": end}
        )

        if not data:
            return {"sign": 0, "data": None}

        bk_id_list = [i[0] for i in data]  # 전표 id리스트

        # taxinvoice 테이블에서 ti_id 조회
        data1 = dbm.query("SELECT ti_id FROM taxinvoice")
        if not data1:
            return {"sign": 0, "data": None}

        ti_id_list = [j[0] for j in data1]  # ti_id 리스트

        # journalizingbook에서 전표 기준(account_name별 차변 대변 합계)
        a = dbm.query(
            "SELECT account_name, SUM(jr_dr), SUM(jr_cr), ANY_VALUE(account_code) FROM journalizingbook "
            "WHERE bk_id IN %(id)s AND account_name IN %(id1)s GROUP BY account_name",
            {"id": tuple(bk_id_list), "id1": tuple(account_dict.keys())}
        )

        # journalizingbook에서 세금계산서 기준(account_name별 차변 대변 합계)
        b = dbm.query(
            "SELECT account_name, SUM(jr_dr), SUM(jr_cr), ANY_VALUE(account_code) FROM journalizingbook "
            "WHERE ti_id IN %(id)s AND account_name IN %(id1)s GROUP BY account_name",
            {"id": tuple(ti_id_list), "id1": tuple(account_dict.keys())}
        )

        # 데이터가 없으면 None 반환
        if not a and not b:
            return {"sign": 0, "data": None}

        result_dict = {}
        data1 = []

        for i in a:
            account_name = i[0]  # account_name
            jr_dr = i[1]  # SUM(jr_dr)
            jr_cr = i[2]  # SUM(jr_cr)
            account_type = account_dict.get(account_name, None)  # 과목별 (name) 자산,부채,자본

            data1.append((account_name, jr_dr, jr_cr, account_type))

        for j in b:
            if data1[0] in data1:
                account_name = j[0]  # account_name
                jr_dr = j[1]  # SUM(jr_dr)
                jr_cr = j[2]  # SUM(jr_cr)
                account_type = account_dict.get(account_name, None)  # 과목별 (name) 자산,부채,자본

                data1.append((account_name, jr_dr, jr_cr, account_type))
        print("값", data1)
        return {"sign": 1, "data": data1}

    @staticmethod
    @MsgProcessor
    def f40402(**kwargs):
        standard_code2 = kwargs.get("insert")
        if standard_code2 is not None:
            data2 = []
            for i in standard_code2:
                b = dbm.query(
                    "INSERT INTO financial_report (subject,dr_cost, cr_cost) VALUES (%(id1)s, %(id2)s, %(id3)s)",
                    {
                        "id1": i[0], "id2": i[1], "id3": i[2]
                    })
                if b is not None:
                    data2.append(b)
            if data2:
                return {"sign": 1, "data": data2}
            else:
                return {"sign": 0, "data": None}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f40501(**kwargs):
        standard_code1 = kwargs.get("기준일자")

        if standard_code1 is None:
            return {"sign": 0, "data": None}

        start, end = standard_code1

        # accountsubject 테이블에서 account_name, account_type, account_code 조회
        account_data = dbm.query(
            "SELECT account_name, account_type, account_code FROM accountsubject WHERE account_type IN ('비용','수익')"
        )

        if not account_data:
            return {"sign": 0, "data": None}

        # account_name을 키로 하는 딕셔너리 생성
        account_dict = {i: [j, k] for i, j, k in account_data}

        # 승인된 전표 bk_id 조회
        data = dbm.query(
            "SELECT bk_id FROM accountbook WHERE (bk_date BETWEEN %(id1)s AND %(id2)s) AND bk_approval_state = '승인'",
            {"id1": start, "id2": end}
        )

        if not data:
            return {"sign": 0, "data": None}

        bk_id_list = [i[0] for i in data]  # 전표 ID 리스트

        # taxinvoice 테이블에서 ti_id 조회
        data1 = dbm.query("SELECT ti_id FROM taxinvoice")

        if not data1:
            return {"sign": 0, "data": None}

        ti_id_list = [j[0] for j in data1]  # ti_id 리스트

        # journalizingbook에서 전표 기준(account_name별 차변 대변 합계)
        a = dbm.query(
            "SELECT account_name, SUM(jr_dr), SUM(jr_cr), ANY_VALUE(account_code) FROM journalizingbook "
            "WHERE bk_id IN %(id)s AND account_name IN %(id1)s GROUP BY account_name",
            {"id": tuple(bk_id_list), "id1": tuple(account_dict.keys())}
        )

        # journalizingbook에서 세금계산서 기준(account_name별 차변 대변 합계)
        b = dbm.query(
            "SELECT account_name, SUM(jr_dr), SUM(jr_cr), ANY_VALUE(account_code) FROM journalizingbook "
            "WHERE ti_id IN %(id)s AND account_name IN %(id1)s GROUP BY account_name",
            {"id": tuple(ti_id_list), "id1": tuple(account_dict.keys())}
        )

        # 데이터가 없으면 None 반환
        if not a and not b:
            return {"sign": 0, "data": None}

        result_dict = {}
        data1 = []

        for i in a:
            account_name = i[0]  # account_name
            jr_dr = i[1]  # SUM(jr_dr)
            jr_cr = i[2]  # SUM(jr_cr)
            account_type = account_dict.get(account_name, None)  # 과목별 (name) 자산,부채,자본

            data1.append((account_name, jr_dr, jr_cr, account_type))

        for j in b:
            if data1[0] in data1:
                account_name = j[0]  # account_name
                jr_dr = j[1]  # SUM(jr_dr)
                jr_cr = j[2]  # SUM(jr_cr)
                account_type = account_dict.get(account_name, None)  # 과목별 (name) 자산,부채,자본

                data1.append((account_name, jr_dr, jr_cr, account_type))
        print("값", data1)
        return {"sign": 1, "data": data1}

    @staticmethod
    @MsgProcessor
    def f40502(**kwargs):
        standard_code2 = kwargs.get("insert")
        if standard_code2 is not None:
            data2 = []
            for i in standard_code2:
                b = dbm.query("INSERT INTO income_report (subject,dr_cost, cr_cost) VALUES (%(id1)s, %(id2)s, %(id3)s)",
                              {
                                  "id1": i[0], "id2": i[1], "id3": i[2]
                              })
                if b is not None:
                    data2.append(b)
            if data2:
                return {"sign": 1, "data": data2}
            else:
                return {"sign": 0, "data": None}
        else:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f40601(**kwargs):
        standard_code1 = kwargs.get("insert")
        query = dbm.query(
            "INSERT INTO analysis_report(analysis_reportcol,estimated_cost,actual_cost) VALUES (%s, %s, %s)",
            (standard_code1[0], standard_code1[1], standard_code1[2]))
        if query is not None:
            return {"sign": 1, "data": query}
        else:
        #elif not query:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f40602(**kwargs):
        standard_code1 = dbm.query("SELECT * FROM analysis_report")

        if standard_code1 is not None:
            return {"sign": 1, "data": standard_code1}
        else:
        #elif not standard_code1:
            return {"sign": 0, "data": None}

    @staticmethod
    @MsgProcessor
    def f40603(**kwargs):
        query = dbm.query(
            "SELECT account_code, account_name FROM journalizingbook")
        if query is not None:
            return {"sign": 1, "data": query}
        else:
        #elif not query:
            return {"sign": 0, "data": None}

    # 계정관리 저장
    @staticmethod
    @MsgProcessor
    def f40701(**kwargs):
        value = [v for v in kwargs.values()]

        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            db.query(
                f"""
                   insert into accountsubject (account_code, account_name, account_type) values ("{value[0]}","{value[1]}","{value[2]}");
                   """
            )
            return {"sign": 1, "data": {}}
        except Exception as e:
            raise e

    # 계정관리 조회
    @staticmethod
    @MsgProcessor
    def f40702(**kwargs):

        # print("Server : f40701(**kwargs)")
        print(f"kwargs : {kwargs}")

        key = [k for k, v in kwargs.items()]
        cond = []
        for k in key:
            if k == "시작코드":
                if kwargs[k] == "":
                    cond.append(0)
                else:
                    cond.append(kwargs[k])
            elif k == "종료코드":
                if kwargs[k] == "":
                    cond.append(99999)
                else:
                    cond.append(kwargs[k])
            elif k == "유형":
                if kwargs[k] == "":
                    selection = '자산', '부채', '자본', '수익', '비용'
                    cond.append(selection)
                else:
                    cond.append(f"('{kwargs[k]}')")

        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query("use erp_db;")
            if cond:
                print(f"cond : {cond}")
                condQue = f"account_code >= {cond[0]} and account_code <= {cond[1]} and account_type in {cond[2]}";
                # print(f"condQue : {condQue}")
                rawData = db.query(
                    f"""
                    select * from accountsubject where {condQue};
                    """
                )
            else:
                rawData = db.query("select * from accountsubject;")
            # print(f"rawData : {list(rawData)}")
            data = [list(ele) for ele in list(rawData)]
            # print(f"data : {data}")
            result = {
                "sign": 1,
                "data": data
            }
            return result
        except Exception as e:
            raise e

    # 계정관리 삭제
    @staticmethod
    @MsgProcessor
    def f40703(**kwargs):
        data = kwargs['data']
        try:
            db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
            db.query('use erp_db;')
            for key in data:
                db.query(f"delete from accountsubject where account_code = '{key}';")
            return {"sign": 1, "data": {}}
        except Exception as e:
            raise e

    @staticmethod
    @MsgProcessor
    def f40704(**kwargs):
        result = {
            "sign": 1,
            "data": "40704"
        }
        return result

    # auth/chat
    @staticmethod
    @MsgProcessor
    def f81001(**kwargs):
        """
        로그인
        "args": {
            "id" : id,
            "pw": pw
        }
        """
        id_ = kwargs.get("id")
        pw = kwargs.get("pw")
        req = kwargs.get("req")
        print(req)
        # sql
        query = dbm.query("SELECT name, department, job_grade, pic from employee where employee_code = %(id)s and pw = %(pw)s", {
            "id": id_,
            "pw": pw
        })

        if not query:
            return {"sign": 0, "data": {}}

        name = query[0][0]
        dept = query[0][1]
        grade = query[0][2]
        pic = query[0][3]
        if pic is not None and isinstance(pic, bytes):
            pic = pic.decode("utf-8")

        # 중복 로그인 확인
        # if not um.login(id_, id_, req):
        #     return {"sign": 0, "data": {}}
        um.login(id_, id_, req)

        result = {
            "sign": 1,
            "data": {
                "id": id_,
                "name": name,
                "dept": dept,
                "grade": grade,
                "pic": pic
            }
        }
        return result

    @staticmethod
    @MsgProcessor
    def f81002(**kwargs):
        """
        로그아웃
        "args": {
            "id" : id
        }
        """
        print("81002")
        id_ = kwargs.get("id")
        # req = kwargs.get("req")

        um.logout(id_)

        result = {
            "sign": 1,
            "data": "70002"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f71003(**kwargs): # msg > um
        """
        메세지
        "args": {
            "from_id": id,
            "type": "user"|"room"|"appr"
            "to_id": id
            "msg" : msg
        }
        """
        req = kwargs.get("req")
        from_id = kwargs.get("from_id")
        type_ = kwargs.get("type")
        to_id = kwargs.get("to_id")

        query = dbm.query("select name from employee where employee_code = %(id)s", {
            "id": from_id
        })
        if query:
            from_name = query[0][0]
        else:
            from_name = "unknown"

        msg = {
            "code": 71003,
            "sign": 1,
            "data": {
                "from_id": from_id,
                "from_name": from_name,
                "type": type_,
                "msg": kwargs.get("msg")
            }
        }

        if type_ == "user":
            um.send_to(to_id, json.dumps(msg, ensure_ascii=False))
        elif type_ == "room":
            um.broadcast_room(to_id, json.dumps(msg, ensure_ascii=False))
        elif type_ == "appr":
            um.send_to(from_id, json.dumps({
                "code": 71005,
                "sign": 1,
                "data": {
                    "id": from_id,
                }
            }, ensure_ascii=False))
            # 받는놈이 온라인이라면 이렇게 보내고
            if (to_id not in um.users) or (um.users[to_id].sock is None):
                # 쿼리실행
                print("받는사람 미접속")
                query = dbm.query("insert into notification values (null, %(id)s, %(msg)s)", {
                    "id": to_id,
                    "msg": json.dumps(msg.get("data"), ensure_ascii=False)
                })
                # 여기서 실패하면 어차피 유실될듯
            else:
                print("받는사람 접속중")
                um.send_to(to_id, json.dumps(msg, ensure_ascii=False))
            # 오프라인이면 db에 올라가야됨
        return {}

    @staticmethod
    @MsgProcessor
    def f81004(**kwargs):
        """
        결재 목적지 id 구하기
        "args": {
            "id": emp id,
        }
        공석일 경우 에러
        """

        id_ = kwargs.get("id")
        query = dbm.query("select department, job_grade from employee where employee_code = %(id)s", {"id": id_})
        if not query:
            raise Exception("from_id not found")

        dept = query[0][0]
        grade = query[0][1]

        if grade == "사장":
            query = dbm.query("select employee_code from employee where department='회계부' order by date_of_employment limit 1")
        elif grade == "부장":
            query = dbm.query("select employee_code from employee where job_grade = '사장' order by date_of_employment limit 1")
        elif grade == "과장":
            query = dbm.query("select employee_code from employee where department=%(dept)s and job_grade = '부장' order by date_of_employment limit 1", {
                "dept": dept
            })
        else:
            to_grade = "과장"
            query = dbm.query("select employee_code from employee where department=%(dept)s and job_grade = '과장' order by date_of_employment limit 1", {
                "dept": dept
            })

        if not query:
            raise Exception("to_id not found")

        to_id = query[0][0]

        result = {
            "sign": 1,
            "data": to_id
        }
        return result

    @staticmethod
    @MsgProcessor
    def f71005(**kwargs):
        """
        결재요청 성공 알림
        """
        pass

    @staticmethod
    @MsgProcessor
    def f81006(**kwargs):
        """
        알림 생성
        "args": {
            "id": id,
            "msg": {}
        }
        """
        id_ = kwargs.get("id")
        msg = kwargs.get("msg")
        query = dbm.query("insert into notification values (null, %(id)s, %(msg)s)", {
            "id": id_,
            "msg": msg
        })

        if not query:
            raise Exception("query failed")

        result = {
            "sign": 1,
            "data": {
                "id": query,
                "msg": msg,
            }
        }
        return result
    
    @staticmethod
    @MsgProcessor
    def f81007(**kwargs):
        """
        알림 제거
        "args": {
            "id": id
        }
        """
        id_ = kwargs.get("id")
        query = dbm.query("delete from notification where id = %(id)s", {"id": id_})

        if query is None:
            raise Exception("query failed")

        result = {
            "sign": 1,
            "data": id_
        }
        return result

    @staticmethod
    @MsgProcessor
    def f81008(**kwargs):
        """
        누적 알림 구하기
        "args": {
            "code": code
        }
        """
        code = kwargs.get("code")
        query = dbm.query("select id, msg from notification where employee_code = %(ec)s", {
            "ec": code
        })

        if query is None:
            raise Exception("query failed")

        result = {
            "sign": 1,
            "data": [{"id": i[0], "msg": i[1]} for i in query]
        }
        return result

    @staticmethod
    @MsgProcessor
    def f71000(**kwargs):
        result = {
            "sign": 1,
            "data": "70001"
        }
        return result

    @staticmethod
    @MsgProcessor
    def f90101(**kwargs):
        standard_code = kwargs.get("작업표준서코드")

        # 쿼리 실행 (결과는 cursor fetchall() 한 결과임)
        data = dbm.query("SELECT SOP_Code, product_code, product_name, writter FROM erp_db.SOP WHERE SOP_Code = %(id)s", {
            "id": standard_code
        })
        
        # 쿼리 실패했을 경우
        # 코드 작성 안해도 raise만 해주면 서버측에서는 {"sign":0, "data":None} 리턴되도록 함
        if data is None:
            raise Exception

        # 현재 data에는 2d tuple이 들어있지만 json dump 하면 list형태로 변환됨
        # []로 인덱스 접근은 그대로
        result = {
            "sign": 1,
            "data": data
        }
        return result

    @staticmethod
    @MsgProcessor
    def f99999(**kwargs):
        result = {"sign": 1, "data": {}}

        data1 = dbm.query("SELECT material_name, sum(price) from receiving GROUP BY material_name")
        # data2 = dbm.query("SELECT material_name, sum(total_price) from shipping GROUP BY material_name")
        params = {
            "serviceKey": de_key, # required
            "pageNo": 1,  # required
            "numOfRows": 10,  # required
            "rlvtYr": 2022,  # ~2022
            "lclgvNm": "대전",
            "returnType": "JSON"  # required
        }
        data2 = ["대전 대덕구", "대전 동구", "대전 서구", "대전 유성구", "대전 중구"]

        data3 = dbm.query("SELECT analysis_reportcol, sum(actual_cost) FROM analysis_report GROUP BY analysis_reportcol ORDER BY sum(actual_cost) DESC LIMIT 5")
        data4 = dbm.query("SELECT analysis_reportcol, sum(estimated_cost), sum(actual_cost) FROM analysis_report GROUP BY analysis_reportcol ORDER BY (sum(actual_cost) - sum(estimated_cost)) LIMIT 5")

        if data1 is not None:
            result["data"]["data1"] = {
                "x": [i[0] for i in data1],
                "y": {
                    "총 비용": [int(i[1])  if i is not None else 0 for i in data1]
                }
            }

        if data2 is not None:
            result["data"]["data2"] = {
                "x": [i for i in data2],
                "y": {
                    "가스": [i["사용량"] for i in us.get("gas", params=params)],
                    "수도": [i["사용량"] for i in us.get("water", params=params)],
                    "전기": [i["사용량"] for i in us.get("elec", params=params)],
                }
            }

        if data3 is not None:
            result["data"]["data3"] = {
                "x": [i[0] for i in data3],
                "y": {
                    "총 비용": [int(i[1]) for i in data3],
                }
            }

        if data4 is not None:
            result["data"]["data4"] = {
                "x": [i[0] for i in data4],
                "y": {
                    "예상 비용": [int(i[1]) for i in data4],
                    "총 비용": [int(i[2]) for i in data4]
                }
            }

        return result

    @ staticmethod
    def process(**kwargs):
        code = kwargs.get("code", -1)
        args = kwargs.get("args", {})
        req = kwargs.get("req", None)

        func = getattr(MsgHandler, f"f{code}", None)
        if (func is None) or (not callable(func)):
            print("★ bad code")
            return {"code": code, "sign": 0, "data": {}}
        #
        # if code not in functions:
        #     print("★ bad code")
        #     return {"code": code, "sign": 0, "data": {}}
        # func = functions[code]
        print("run", code)
        if req is None:
            result = {"code": code, **func(**args)}
        else:
            result = {"code": code, **func(**args, req=req)}
        return result