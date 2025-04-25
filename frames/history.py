import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
from tablewidget import TableWidget, ColName
from color import Color
import pymysql
import json


# import dbManager
#
# dbm = dbManager.DBManager(host="192.168.0.29", user="root", password="0000", port=3306)

class history_Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        # self.root.title("ERP 영업(3.거래내역조회)")

        # frame 생성
        self.frame1 = tk.Frame(self, width=950, height=350)  # 왼쪽 위 구역
        self.frame2 = tk.Frame(self, width=350, height=350)  # 오른쪽 위 구역
        self.frame3 = tk.Frame(self, width=1300, height=350)  # 아래 구역

        # frame 크기 자동 축소 방지 (pack/grid)
        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.grid_propagate(False)
        self.frame3.pack_propagate(False)

        # frame 배치
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0, columnspan=2)

        # frame1에 들어갈 것들
        self.label1 = ttk.Label(self.frame1, text="조회구분")
        self.label1.grid(padx=5, pady=5, sticky="w")
        self.label1.place(x=10, y=10)

        self.var = tk.IntVar(value=1)

        self.radiobutton1 = tk.Radiobutton(self.frame1, text="거래처명", variable=self.var, value=1)
        self.radiobutton1.grid()
        self.radiobutton1.select()
        self.radiobutton1.place(x=100, y=10)
        self.radiobutton2 = tk.Radiobutton(self.frame1, text="사업자번호", variable=self.var, value=2)
        self.radiobutton2.grid()
        self.radiobutton2.place(x=190, y=10)
        self.radiobutton3 = tk.Radiobutton(self.frame1, text="거래처코드", variable=self.var, value=3)
        self.radiobutton3.grid()
        self.radiobutton3.place(x=290, y=10)

        # --------------------------------------------------------------------------------

        self.label2 = ttk.Label(self.frame1, text="입   력", background="")
        self.label2.grid(padx=5, pady=5, sticky="w")
        self.label2.place(x=10, y=40)

        self.entry2 = tk.Entry(self.frame1, width=10)
        self.entry2.grid(padx=5, pady=5, sticky="w")
        self.entry2.place(x=100, y=40, width=180)

        # --------------------------------------------------------------------------------

        self.label3 = ttk.Label(self.frame1, text="조회일자")
        self.label3.grid(padx=5, pady=5, sticky="w")
        self.label3.place(x=10, y=70)

        self.today = datetime.date.today()
        self.cal1 = DateEntry(self.frame1, date_pattern='yyyy-MM-dd', dateformat=self.today, width=12,
                              background='gray',
                              foreground='white', borderwidth=4, Calendar=2025)
        self.cal1.grid(sticky='nsew')
        self.cal1.place(x=100, y=70)

        self.label4 = ttk.Label(self.frame1, text="부터")
        self.label4.grid(padx=5, pady=5, sticky="w")
        self.label4.place(x=210, y=70)

        self.today = datetime.date.today()
        self.cal2 = DateEntry(self.frame1, date_pattern='yyyy-MM-dd', dateformat=self.today, width=12,
                              background='gray',
                              foreground='white', borderwidth=4, Calendar=2025)
        self.cal2.grid(sticky='nsew')
        self.cal2.place(x=240, y=70)

        self.label4 = ttk.Label(self.frame1, text="까지")
        self.label4.grid(padx=5, pady=5, sticky="w")
        self.label4.place(x=350, y=70)

        # --------------------------------------------------------------------------------

        # frame2에 들어갈 것들
        self.Button = ttk.Button(self.frame2, text="검색", command=self.search)
        self.Button.place(x=250, y=10)

        # frame3에 들어갈 것들
        self.test_data = [
            # [[self.cursor.execute(f"SELECT * from Customer_management where Customer_name={self.entry1.get()}[0][2]")], "5", "6", "3", "3", "3", "3", "3"],
            # [self.cursor.execute(f"SELECT Customer_name from Customer_management WHERE Customer_name LIKE '%{self.entry1.get()}%'"), "5", "6", "3", "3", "3", "3", "3"],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
        ]

        self.app1 = TableWidget(self.frame3,
                                data=self.test_data,
                                has_checkbox=False,
                                cols=10,
                                col_name=["거래일자", "거래처명", "사업자번호", "거래처코드", "거래처종류", "국가", "품목", "수량", "단가", "총 가격"],
                                # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                col_width=[120, 150, 100, 130, 150, 50, 150, 50, 150, 185],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                # col_align=["left", "center", "right", "left"],
                                editable=[False, False, False, False, False, False, False, False, False, False],
                                width=1300,  # 테이블 그려질 너비
                                height=350,
                                padding=10)  # 테이블 그려질 높이
        # col_width 생략 시 크기에 맞게 분배
        # col_name 생략 시 Col1, Col2, ... 지정

        self.app1.grid(row=0, column=0)

    def recv(self, **kwargs):
        # 서버로부터 받은 데이터를 테이블에 올리기 등
        print("code:", kwargs.get("code"))
        print("sign:", kwargs.get("sign"))
        print("data:", kwargs.get("data"))

        aa = kwargs.get("data")
        self.app1.refresh(aa)
        return kwargs

    # def search(self):#버튼에 연결된 함수로 , 내부에서 서버에 send_하는 함수를 호출한다, send는 rew_data형태(json)으로 만들어서 쏴준다.,
    #
    #     d = {
    #         "input" : self.entry2.get(),
    #         "select_value": self.var.get()
    #             }
    #
    #     test_dict = {
    #         "code":30201,
    #         "args": d
    #     }
    #
    #     self.select_value = self.var.get()
    #
    #     if self.select_value == 1:
    #         kwargs.result1()
    #
    #     elif self.select_value == 2:
    #         kwargs.result2()
    #
    #     elif self.select_value == 3:
    #         kwargs.result3()
    #
    #     elif self.entry2.get() == "":
    #         msgbox.showinfo("알림", "값을 입력해 주세요")
    #
    #
    #
    #     self.root.send_(json.dumps(test_dict, ensure_ascii=False))
    #
    #     def f30201(**kwargs):
    #         # result=dbm.query(f"SELECT Customer_name, business_number, Customer_code, Type_business, business_adress, ContactPerson_name, ContactPerson_phone, e_mail from Customer_management WHERE Customer_name LIKE '%{self.entry1.get()}%'")
    #
    #         result1 = dbm.query(f"SELECT order_form.creation_date, Customer_management.Customer_name, Customer_management.business_number, Customer_management.Customer_code, Customer_management.Type_business, Customer_management.Country, order_form.product_name, order_form.transaction_quantity, order_form.unit_price, order_form.total_price FROM Customer_management INNER JOIN order_form ON Customer_management.Customer_code = order_form.Customer_code WHERE Customer_management.Customer_name LIKE '%{kwargs.get("input")}%'")
    #         result2 = dbm.query(f"SELECT order_form.creation_date, Customer_management.Customer_name, Customer_management.business_number, Customer_management.Customer_code, Customer_management.Type_business, Customer_management.Country, order_form.product_name, order_form.transaction_quantity, order_form.unit_price, order_form.total_price FROM Customer_management INNER JOIN order_form ON Customer_management.Customer_code = order_form.Customer_code WHERE Customer_management.business_number LIKE '%{kwargs.get("input")}%'")
    #         result3 = dbm.query(f"SELECT order_form.creation_date, Customer_management.Customer_name, Customer_management.business_number, Customer_management.Customer_code, Customer_management.Type_business, Customer_management.Country, order_form.product_name, order_form.transaction_quantity, order_form.unit_price, order_form.total_price FROM Customer_management INNER JOIN order_form ON Customer_management.Customer_code = order_form.Customer_code WHERE Customer_management.Customer_code LIKE '%{kwargs.get("input")}%'")
    #
    #
    #         if result is not None:
    #             result = {"sign": 1, "data": result}
    #         else :
    #             result = {"sign": 0, "data": None}
    #
    #         return result

    def search(self):
        d = {
            "input": self.entry2.get(),
            "select_value": self.var.get(),
            "date1": self.cal1.get(),
            "date2": self.cal2.get()
        }

        if d["input"] == "":
            msgbox.showinfo("알림", "값을 입력해 주세요")
            return

        test_dict = {
            "code": 30201,
            "args": d
        }

        self.root.send_(json.dumps(test_dict, ensure_ascii=False))

        # def f30201(**kwargs): #history
        #     input_value = kwargs.get("input", "")
        #     select_value = kwargs.get("select_value", 1)
        #
        #     column1 = {
        #         1: "Customer_management.Customer_name",
        #         2: "Customer_management.business_number",
        #         3: "Customer_management.Customer_code"
        #     }
        #
        #     column = column1.get(select_value, "Customer_management.Customer_name")
        #
        #     query = f"SELECT order_form.creation_date, Customer_management.Customer_name, Customer_management.business_number, Customer_management.Customer_code, Customer_management.Type_business, Customer_management.Country, order_form.product_name, order_form.transaction_quantity,order_form.unit_price, order_form.total_price FROM Customer_management INNER JOIN order_form ON Customer_management.Customer_code = order_form.Customer_code WHERE {column} LIKE %s AND order_form.creation_date BETWEEN '{kwargs.get("date1")}' AND '{kwargs.get("date2")}'"
        #
        #     result = dbm.query(query, (f"%%{input_value}%%",))
        #
        #     result = [[str(j) for j in list(i)] for i in result]
        #
        #     if result is not None:
        #         result = {"sign": 1, "data": result}
        #     else :
        #         result = {"sign": 0, "data": None}
        #
        #     return result

        # def test3(self):
        #     def f30201(**kwargs):
        #         # aa = kwargs.get("거")
        #
        #         self.select_value = self.var.get()
        #
        #         self.cursor = self.connection.cursor()
        #         self.cursor.execute("use kth_db;")
        #
        #         if self.select_value == 1:
        #             self.cursor.execute(f"SELECT order_form.creation_date, Customer_management.Customer_name, Customer_management.business_number, Customer_management.Customer_code, Customer_management.Type_business, Customer_management.Country, order_form.product_name, order_form.transaction_quantity, order_form.unit_price, order_form.total_price FROM Customer_management INNER JOIN order_form ON Customer_management.Customer_code = order_form.Customer_code WHERE Customer_management.Customer_name LIKE '%{self.entry2.get()}%'")
        #
        #         if self.select_value == 2:
        #             self.cursor.execute(f"SELECT order_form.creation_date, Customer_management.Customer_name, Customer_management.business_number, Customer_management.Customer_code, Customer_management.Type_business, Customer_management.Country, order_form.product_name, order_form.transaction_quantity, order_form.unit_price, order_form.total_price FROM Customer_management INNER JOIN order_form ON Customer_management.Customer_code = order_form.Customer_code WHERE Customer_management.business_number LIKE '%{self.entry2.get()}%'")
        #
        #         if self.select_value == 3:
        #             self.cursor.execute(f"SELECT order_form.creation_date, Customer_management.Customer_name, Customer_management.business_number, Customer_management.Customer_code, Customer_management.Type_business, Customer_management.Country, order_form.product_name, order_form.transaction_quantity, order_form.unit_price, order_form.total_price FROM Customer_management INNER JOIN order_form ON Customer_management.Customer_code = order_form.Customer_code WHERE Customer_management.Customer_code LIKE '%{self.entry2.get()}%'")
        #
        #         if self.entry2.get() == "":
        #             msgbox.showinfo("알림", "값을 입력해 주세요")
        #
        #         self.connection.commit()
        #         aa = self.cursor.fetchall()
        #
        #         #print(aa[0][4])
        #
        #         self.test_data = [
        #
        #         ]
        #
        #         result = {
        #             "sign": 1,
        #             "data": aa
        #         }
        #
        #         aa=result.get("data")
        #         self.app1.refresh(aa)
        #         return result
        #
        #         self.cursor.close()  # 커서 객체는 닫는다
        #         self.connection.close()  # 커넥션 객체는 닫는다
        #
        #     dd = {
        #         "거래처명": "ㅇㅇ"
        #     }
        #
        #     print(f30201(**dd).get("data"))

        def send_(self):
            test_dict = {
                "code": 30201,
                "args": {
                    "작업표준서코드": 123
                }
            }
            self.root.send_(json.dumps(test_dict, ensure_ascii=False))

        def recv(self, **kwargs):
            print("code:", kwargs.get("code"))
            print("sign:", kwargs.get("sign"))
            print("data:", kwargs.get("data"))

            # 디버그용
            self.root.bind("<F5>", lambda e: test())
            self.root.bind("<F4>", lambda e: self.app1.add_row())
            self.root.bind("<F3>", lambda e: test2())
            self.root.bind("<F2>", lambda e: print(self.app1.get()))

            def test():
                print(f"data: {self.app1.data}")  # 저장된 데이터
                print(f"rows cols: {self.app1.rows} {self.app1.cols}")  # 행 열 개수
                print(f"selected: {self.app1.selected_row} {self.app1.selected_col}")  # 선택된 행 열 index
                print(f"changed {self.app1.changed}")  # 원본 대비 변경된 데이터

            def test2():
                self.app1.from_data(
                    data=[
                        ["1", "2", "3"],
                        ["4", "5", "6"],
                        ["7", "8", "9"],
                    ],
                    cols=3,
                    new_row=False,
                    has_checkbox=False,
                    col_name=["A", "B", "C"],
                    col_width=None,
                    col_align=["left", "center", "right"],
                    editable=[False, True, True],
                    width=1300,
                    height=350,
                )


# 테스트용 코드
if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    fr = history_Frame(r)
    fr.place(x=300, y=130)
    r.mainloop()
