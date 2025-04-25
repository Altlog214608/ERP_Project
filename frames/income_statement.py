# `account_name` VARCHAR(45) NULL DEFAULT NULL, 과목
# `jr_dr` VARCHAR(14) NULL DEFAULT '0', 차변
# `jr_cr` VARCHAR(14) NULL DEFAULT '0', 대변
# 빈데이터가 왔을때의 처리 ,그냥 조회만 눌렀을때 처리  1,2번 파일
# 두개 코드 합치기 send_data하나만 보내주기

# 전표 테이블에 전표날짜가 설정한 기간안에 전표승인(bk_approval_state)되있는 전표번호를 조회 -> 전표번호로 분개테이블을 조회
# 조회된 분개들을 계정과목별 총 합계를 구함 ( dr 합계(차변), cr합계(대변) )
# 분개 테이블 조회하기 전에 accountbook과 accountsubject를 조인 >
# accountsubject 테이블의 account_type컬럼 값이 자산,부채 자본 값만 가져와서 accountbook 테이블에 붙인다.
# 손익계산서 : 수익 비용


# import pymysql
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tablewidget import TableWidget, ColName
from color import Color
import datetime
# import dbManager
import json
import math


class income_statement(tk.Frame):  # 손익계산서
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        self.cal = None

        self.table_data = [[]]  # 조회 데이터 담을 리스트
        self.select = None  # 날짜

        # self.db_data = None #전표 승인 조회

        # frame 생성
        self.frame1 = tk.Frame(self, width=950, height=700, )  # 왼쪽 위 구역
        self.frame2 = tk.Frame(self, width=350, height=350, )  # 오른쪽 위 구역
        self.frame4 = tk.Frame(self, width=350, height=350, )  # 오른쪽 아래 구역

        # frame 크기 자동 축소 방지 (pack/grid)
        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame4.grid_propagate(False)
        self.frame4.pack_propagate(False)

        # frame 배치
        self.frame1.grid(row=0, column=0, rowspan=2)
        self.frame2.grid(row=0, column=1)
        # self.frame3.grid(row=1, column=0)
        self.frame4.grid(row=1, column=1)

        # 초기 테이블
        self.create_table()

        # frame2에 들어갈 것들
        self.test_label1 = ttk.Label(self.frame2, text="기준일자",width=14)
        self.test_label1.place(x=10, y=12)
        self.test_ent1 = ttk.Entry(self.frame2, width=15)
        self.test_ent1.place(x=110, y=11)
        self.test_btn1 = ttk.Button(self.frame2, text="조회하기", command=self.on_click)
        self.test_btn1.place(x=240, y=10)

        self.test_ent1.bind("<Button-1>", self.on_date_select1)

    def after_init(self):
        pass

    def create_table(self, current_range="당기", prev_range="전기"):
        if hasattr(self, "table"):  # 테이블이 있으면 지우기
            self.table.destroy()

        # 새로운 열 이름 설정 (당기, 전기 옆에 날짜 추가)
        col_name = ColName()
        col_name.add("과목", 0, 0, rowspan=2)
        col_name.add(f"{current_range}", 0, 1, colspan=2)
        col_name.add(f"{prev_range}", 0, 3, colspan=2)
        col_name.add("금액", 1, 1, colspan=2)
        col_name.add("금액", 1, 3, colspan=2)

        # 새 테이블 생성
        self.table = TableWidget(
            self.frame1,
            data=  # 해당하는 당기,전기 데이터 가져오기
            None
            ,
            cols=5,
            new_row=False,
            has_checkbox=False,
            col_name=col_name,  # 업데이트된 열 제목 적용
            col_width=[170, 178.75, 178.75, 178.75, 178.75],
            col_align=["center", "right", "right", "right", "right"],
            editable=[False, False, False, False, False],
            width=950,
            height=700,
            padding=10,

        )
        self.table.grid(row=0, column=0)

    def on_date_select1(self, event):  # 캘린더1
        # if self.cal:
        #     self.cal.destroy() #닫아줌
        self.cal = Calendar(self.frame2, firstweekday="sunday", locale="ko_KR", showweeknumbers=False)  # 일욜시작 앞에 주차 없애기
        self.cal.place(x=110, y=35)
        self.cal.bind("<<CalendarSelected>>", self.select_date1)

    def select_date1(self, event):  # 선택되면 엔트리에 저장
        self.test_ent1.delete(0, tk.END)
        self.test_ent1.insert(0, self.cal.selection_get())  # 날짜 가져옴
        self.cal.destroy()  # 선택하면 창닫기
        # self.cal = None
        # self.test_ent1.bind("<Button-1>",self.on_date_select1)

    def on_click(self):  # 조회하기 버튼
        self.select = self.test_ent1.get().strip()  # 사용자가 선택한 날짜 가져오기

        if not self.select:  # 날짜를 선택하지 않은 경우
            print("no date")
            return  # 함수 종료

        try:
            select_date = datetime.datetime.strptime(self.select, "%Y-%m-%d")
        except ValueError:
            print("date error")  # 날짜 형식이 맞지 않을 경우 처리
            return

        # 당기: 선택년도 1월 1일 ~ 선택 날짜
        current_year = select_date.year
        current_start = datetime.datetime(current_year, 1, 1)
        current_end = select_date

        # 전기: 작년 1월 1일 ~ 선택 날짜
        prev_year = current_year - 1
        prev_start = datetime.datetime(prev_year, 1, 1)
        prev_end = datetime.datetime(prev_year, 12, 31)

        # 날짜 문자열 생성
        current_range = [current_start.strftime('%Y-%m-%d'), current_end.strftime('%Y-%m-%d')]
        prev_range = f"전기[{prev_start.strftime('%Y-%m-%d')} ~ {prev_end.strftime('%Y-%m-%d')}]"

        print(f"당기: {current_range}")
        print(f"전기: {prev_range}")

        self.create_table(f"당기{current_range[0]}~{current_range[1]}", prev_range)  # 컬럼에 들어가는 날짜

        send_data = {"code": 40501, "args": {"기준일자": current_range}}
        self.send_(send_data)

    # 클라 >> 서버
    def send_(self, data):
        self.root.send_(json.dumps(data, ensure_ascii=False))


    # 자동호출
    def recv(self, **kwargs):
        code = kwargs.get('code')
        sign = kwargs.get('sign')
        data = kwargs.get('data')

        if code == 40501:  # 불러오기
            if sign == 1:
                print("f40501 success")
                print("sign:", kwargs.get("sign"))
                print("data:", kwargs.get("data"))

                for i in range(len(data)):
                    if data[i][3][0] == "비용":
                        data[i].append(2)
                    elif data[i][3][0] == "수익":
                        data[i].append(1)

                cal = {}
                for i in data:
                    account_name, jr_dr, jr_cr, type_, align = i
                    if account_name not in cal.keys():
                        cal[account_name] = {'cr': [], 'dr': [], 'type': type_[0], 'code': type_[1], 'align': align}
                        cal[account_name]['cr'].append(math.floor(jr_cr))
                        cal[account_name]['dr'].append(math.floor(jr_dr))
                    else:
                        cal[account_name]['cr'].append(math.floor(jr_cr))
                        cal[account_name]['dr'].append(math.floor(jr_dr))
                print("cal ===", cal)
                tdata = []
                for k, v in cal.items():
                    if v['type'] == '비용':
                        tdata.append([k, sum(v['dr']) - sum(v['cr']), v['align'], v['code']])
                    elif v['type'] == '수익':
                        tdata.append([k, sum(v['cr']) - sum(v['dr']), v['align'], v['code']])

                type1 = 0 # 수익 합
                type2 = 0 # 비용 합
                for i in tdata:
                    account_name, amount, type_, code = i
                    if type_ == 1:
                        type1 += amount
                    elif type_ == 2:
                        type2 += amount

                print(f"type1 : {type1}, type2 : {type2}")
                tdata.sort(key=lambda x: (x[2], x[3]))
                a = 0
                print("tdata ===", tdata)
                for i in range(len(tdata)+1):
                    if type(tdata[i][1]) is int:
                        tdata[i][1] = format(tdata[i][1],",")
                    if tdata[i][2] == 1:
                        tdata[i].pop()
                        tdata[i].insert(1,"")
                        tdata[i].pop()
                        tdata[i].append("")
                        tdata[i].append("")
                        tdata[i].append("")
                    elif tdata[i-1][3] == "" and tdata[i][2] == 2 and a == 0:
                        a = 1
                        tdata.insert(i,['수익총계',"",format(type1,","),"",""])
                    elif tdata[i][2] == 2:
                        tdata[i].pop()
                        tdata[i].insert(1,"")
                        tdata[i].pop()
                        tdata[i].append("")
                        tdata[i].append("")
                        tdata[i].append("")
                tdata.append(['비용총계', "", format(type2, ","), "", ""])
                tdata.append(['당기순손익', "", format(type1 - type2, ","), "", ""])

                print("tdata2 :", tdata)
                self.table_data = tdata
                self.table.refresh(self.table_data)

                # send_data2 = {"code": 40502, "args": {"insert": self.table_data}}
                # self.send_(send_data2)


            else:
                print("f40501 fail")

                # print("sign:", kwargs.get("sign"))
                # print("data:", kwargs.get("data"))

        if code == 40502:  # 인서트
            if sign == 1:
                print("f40502 sucess")

                # print("sign:", kwargs.get("sign"))
                # print("data:", kwargs.get("data"))
            else:
                print("f40502 fail")

                # print("sign:", kwargs.get("sign"))
                # print("data:", kwargs.get("data"))


'''
@staticmethod
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
    print("값",data1)
    return {"sign": 1, "data": data1}





@staticmethod
# #서버 >>클라
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
'''

# 테스트용 코드
if __name__ == "__main__":
    # dbm = dbManager.DBManager(host="localhost", user="root", password="0000", port=3306)
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    fr = income_statement(r)
    fr.place(x=300, y=130)

    r.mainloop()









