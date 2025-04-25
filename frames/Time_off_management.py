from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import tkinter.messagebox as msb
import locale
import tablewidget as tablewidget
# import mysql.connector
# import dbManager
import json


# 연차관리.
class Timeoffmanagement(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        locale.setlocale(locale.LC_TIME, 'ko_KR')

        self.root = root
        self.memo = {}

        # 입력 프레임 (950x350, 왼쪽 위)
        self.input_frame = tk.LabelFrame(self)
        self.input_frame.place(x=0, y=30, width=950, height=350)

        self.create_input_fields()

        # 제어 프레임 (350x350, 오른쪽 위)
        self.control_frame = tk.LabelFrame(self)
        self.control_frame.place(x=950, y=30, width=350, height=350)

        self.create_control_fields()

        # 출력 프레임 (1300x350, 아래)
        self.output_frame = tk.LabelFrame(self)
        self.output_frame.place(x=0, y=380, width=1300, height=350)

        # self.create_output_fields()

    # 휴가 수정 관리 창
    def open_new_window(self, event):
        self.new_win = tk.Toplevel(self)
        self.new_win.title("휴가 수정 (가제)")
        self.new_win.geometry("300x300")

        self.new_win_label1 = tk.Label(self.new_win, text='휴가 종류')
        self.new_win_label1.place(x=50, y=50)

        # 사원코드
        tk.Label(self.new_win, text='사원코드').place(x=50, y=20)
        self.emp_entry = tk.Entry(self.new_win, width=13)
        self.emp_entry.place(x=120, y=20)

        # 연차 종류 선택 박스
        self.new_win_var1 = tk.StringVar()
        self.new_win_box = ttk.Combobox(self.new_win, textvariable=self.new_win_var1,
                                        values=["연차", "반차", "월차", "경조사", "기타"], state="readonly", width=10)
        self.new_win_box.place(x=120, y=50)
        self.new_win_box.current(0)

        self.new_win_label2 = tk.Label(self.new_win, text='사유')
        self.new_win_label2.place(x=50, y=90)

        # 사유 텍스트 박스
        self.new_win_var2 = tk.StringVar()
        self.new_win_entry = ttk.Entry(self.new_win, textvariable=self.new_win_var2)
        self.new_win_entry.place(x=100, y=90, width=150, height=150)

        # 저장 버튼
        self.save_button1 = ttk.Button(self.new_win, text='저장', width=5, command=self.memo_plus)
        self.save_button1.place(x=200, y=250)

        self.save_button2 = ttk.Button(self.new_win, text='취소', width=5, command=self.memo_delete)
        self.save_button2.place(x=250, y=250)

    def create_input_fields(self):
        # 달력에 대한 프레임
        self.Calendar_frame = tk.LabelFrame(self)
        self.Calendar_frame.place(x=0, y=30, width=950, height=350)
        self.cal = Calendar(self.Calendar_frame,
                            selectmode='day',
                            background='white',
                            foreground='black',
                            headersbackground='#ADD8E6',
                            normalforeground='black',
                            weekendbackground='#BDCDD6',
                            weekendforground='black',
                            othermonthforeground='gray50',
                            othermonthbackground='white',
                            othermonthweforeground='gray50',
                            othermonthwebackground='#EEE9DA'
                            )

        self.cal.pack(fill="both", expand=True, pady=20)
        self.cal.bind("<<CalendarSelected>>", self.open_new_window)

    def create_control_fields(self):
        # 왼쪽 입력 필드 (사원코드, 이름)
        tk.Label(self.control_frame, text="사원코드").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_code = tk.Entry(self.control_frame, width=20)
        self.entry_code.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.control_frame, text="이름").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_name = tk.Entry(self.control_frame, width=20)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        # 콤보박스 (부서, 직급)
        tk.Label(self.control_frame, text="부서").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.combo_department = ttk.Combobox(self.control_frame, values=["인사부", "영업부", "기술부"], state="readonly",
                                             width=18)
        self.combo_department.grid(row=2, column=1, padx=5, pady=5)
        self.combo_department.current(0)  # 기본값 설정

        tk.Label(self.control_frame, text="직급").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.combo_position = ttk.Combobox(self.control_frame, values=["사원", "대리", "과장", "부장"], state="readonly",
                                           width=18)
        self.combo_position.grid(row=3, column=1, padx=5, pady=5)
        self.combo_position.current(0)  # 기본값 설정

        # 버튼
        button_frame = tk.Frame(self.control_frame)
        button_frame.grid(row=0, column=2, rowspan=4, padx=5, pady=5, sticky="e")

        tk.Button(button_frame, text="조회", width=10, command=self.search_attendance).pack(pady=3)
        tk.Button(button_frame, text="신규", width=10).pack(pady=3)
        tk.Button(button_frame, text="수정", width=10).pack(pady=3)
        tk.Button(button_frame, text="저장", width=10).pack(pady=3)

    # def create_output_fields(self):
    #     columns = ["사원코드", "사원명", "부서", "출근시간", "퇴근시간", "지각", "조퇴", "연장근무", "연차사용", "근태상태"]

    #     # 더미 데이터 (나중에 DB에서 불러오는 함수 `load_employee_data()`에서 업데이트 예정)
    #     dummy_data = [
    #         ["SCP-772", "징징이", "인사부", "09:00", "17:50", "지각함 ㅋ", "조퇴마려움", "절대안하지", "연차쓰고감 ㅂㅂ", "자르죠?"]
    #     ]

    #     # TableWidget을 출력 화면에 배치
    #     self.table = tablewidget.TableWidget(
    #         self.output_frame,
    #         data=dummy_data,
    #         col_name=columns,
    #         width=1300,
    #         height=350
    #     )

    #     self.table.pack()

    # 조회 함수(클라이언트용)
    def search_attendance(self):
        self.search = {
            "사원 코드": self.entry_code.get(),  # 사원 코드
            "이 름": self.entry_name.get(),  # 이 름
            "부  서": self.combo_department.get(),  # 부 서
            "직 급": self.combo_position.get()  # 직 급
        }

        data = {"code": 10701, "args": self.search}
        # self.f10701(**data)
        self.root.send_(json.dumps(data, ensure_ascii=False))

    # @staticmethod
    # # 서버용 조회 함수
    # def f10701(**kwargs):
    #     #     dbm = dbManager.DBManager(host="192.168.0.29", user="root", password="0000", port=3306)
    #     # 사원 코드 , 이름 , 부서 , 직급 검색 조건 ---> 검색 결과는 사원 코드 ,이름 ,부서, 초과근무날짜, 시작시간 ,종료 시간 ,승인 여부, 수당지급
    #
    #     base_query = """
    #         SELECT employee_code, name, department, position, join_date,
    #         total_leave, used_leave, approval_status
    #         FROM annual_leave_management
    #       """
    #
    #     # 검색 조건으로 사용할 유효한 컬럼 목록
    #     valid_columns = {"employee_code", "name", "department"}
    #
    #     # 입력된 kwargs에서 유효한 검색 조건 필터링
    #     valid_conditions = [
    #         f"COALESCE({key}, '') LIKE '%%{value}%%'" for key, value in kwargs.items()
    #         if key in valid_columns and value]
    #
    #     # 조건이 있으면 WHERE 절 추가
    #     query = base_query if not valid_conditions else f"{base_query} WHERE {' AND '.join(valid_conditions)}"
    #
    #     # SQL 실행
    #     data = dbm.query(query) or []
    #
    #     # 전체 출력 조건 추가
    #     if not data:
    #         data = dbm.query(base_query) or []
    #
    #     # 날짜 데이터를 문자열로 변환
    #     formatted_data = [
    #         [str(item) if isinstance(item, (datetime.date, datetime.time, datetime.timedelta)) else item for item in
    #          row]
    #         for row in data]
    #
    #     return {"sign": 1, "data": formatted_data} if formatted_data else {"sign": 0, "data": "쿼리 실패"}

    def send_(self, some_dict):
        self.root.send_(json.dumps(some_dict, ensure_ascii=False))

    def after_init(self):
        pass

    def recv(self, **kwargs):
        code, sign, data = kwargs.get("code"), kwargs.get("sign"), kwargs.get("data")
        print("code:", kwargs.get("code"))
        print("sign:", kwargs.get("sign"))
        print("data:", kwargs.get("data"))
        print("recv")
        if kwargs.get("code") == 10701:
            # 테이블이 없으면 새로 생성
            if kwargs.get("sign") == 1:
                print(data)
                self.table = tablewidget.TableWidget(
                    self.output_frame,
                    data=data,
                    col_name=["사원코드", "사원명", "부서", "직급", "입사일", "총 연차", "사용한 연차", "승인여부"],
                    col_width=[150, 150, 150, 150, 150, 150, 150, 150, 150],
                    width=1300,
                    height=350
                )
                self.table.grid(row=0, column=0)
            else:
                msb.showerror("오류", "쿼리 실패")
        elif kwargs.get("code") == 10701 and kwargs.get("sign") == 1:
            self.table.refresh(kwargs.get("data"))

    # 연차 저장 버튼 눌렀을 때
    def memo_plus(self):

        emp_code = self.emp_entry.get()
        leave_type = self.new_win_box.get()
        reason = self.new_win_entry.get()

        if not emp_code or not reason:
            msb.showwarning("경고", "작성해주시기 바랍니다.")


        else:
            self.emp_entry.delete(0, tk.END)
            self.new_win_entry.delete(0, tk.END)
            msb.showinfo("완료", "저장이 완료되었습니다.")
            self.new_win.destroy()

        # 새로운 딕셔너리 구조
        new_entry = {
            "연차 종류": leave_type,
            "사유": reason
        }

        # 만약 해당 사원코드가 이미 존재하면 기존 데이터에 추가
        if emp_code in self.memo:
            self.memo[emp_code].append(new_entry)
        else:
            self.memo[emp_code] = [new_entry]  # 새로운 리스트 생성

        print("저장된 데이터:", self.memo)

        date = {"code": 10702, "arges": self.memo}

        # self.f10702(**date)

    def memo_delete(self):
        # 취소버튼을 눌렀으면 한 번 경고창을 띄우고 아니오-하면 다시 창으로 ㄱㄱ, 예 하면 콤보박스는 기본값으로 돌아가고 , entry를 삭제
        message1 = msb.askquestion('askokcancel', "작성을 취소하시겠습니까?")
        if message1 == 'yes':
            self.new_win.destroy()

        elif message1 == 'no':
            msb.showinfo("messagebox", "취소하셨습니다.")

    # @staticmethod
    # def f10702(**kwargs):
    #     result ={
    #         'sign' : 1,
    #         'data': '10702'
    #     }
    #     return result

    # def recv(self, **kwargs):
    #     print("code:", kwargs.get("code"))
    #     print("sign:", kwargs.get("sign"))
    #     print("data:", kwargs.get("data"))

    #     if "code" == 10702:
    #         if "sign" == 1:
    #             print("저장이 완료되었습니다.")

    #         else:
    #             print("저장이 실패했습니다.")


# test_socket = None
# dbm = None


if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    app = Timeoffmanagement(r)
    app.place(x=300, y=130)

    app.mainloop()