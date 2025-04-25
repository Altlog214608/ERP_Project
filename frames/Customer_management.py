import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import ttk
from tablewidget import TableWidget, ColName
from color import Color
import pymysql
import json
# import dbManager
#
# dbm = dbManager.DBManager(host="192.168.0.29", user="root", password="0000", port=3306)

class Customer_management_Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        # self.root.title("ERP 영업(2.거래처관리)")
        
        # frame 생성
        self.frame1 = tk.Frame(self, width=950, height=350) # 왼쪽 위 구역
        self.frame2 = tk.Frame(self, width=350, height=350) # 오른쪽 위 구역
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
        self.label1 = ttk.Label(self.frame1, text="거래처명")
        self.label1.grid(padx=5, pady=5, sticky="w")
        self.label1.place(x=10, y=10)

        self.entry1 = tk.Entry(self.frame1, width=10)
        self.entry1.grid(padx=5, pady=5, sticky="w")
        self.entry1.place(x=110, y=10, width=180)

        # --------------------------------------------------------------------------------

        self.label2 = ttk.Label(self.frame1, text="사업자번호")
        self.label2.grid(padx=5, pady=5, sticky="w")
        self.label2.place(x=10, y=40)

        self.entry2 = tk.Entry(self.frame1, width=10)
        self.entry2.grid(padx=5, pady=5, sticky="w")
        self.entry2.place(x=110, y=40, width=180)

        # --------------------------------------------------------------------------------

        self.label3 = ttk.Label(self.frame1, text="거래처코드")
        self.label3.grid(padx=5, pady=5, sticky="w")
        self.label3.place(x=10, y=70)

        self.entry3 = tk.Entry(self.frame1, width=10)
        self.entry3.grid(padx=5, pady=5, sticky="w")
        self.entry3.place(x=110, y=70, width=180)

        # --------------------------------------------------------------------------------

        self.label9 = ttk.Label(self.frame1, text="국     가")
        self.label9.grid(padx=5, pady=5, sticky="w")
        self.label9.place(x=10, y=100)

        self.a=["한국", "일본", "중국", "미국"]
        self.combobox2 = ttk.Combobox(self.frame1)
        self.combobox2.config(height=0)
        self.combobox2.config(values=self.a)
        self.combobox2.config(state="readonly")
        self.combobox2.set("국가 선택")
        self.combobox2.grid()
        self.combobox2.place(x=110, y=100)


        self.test_data = [
            #[[self.cursor.execute(f"SELECT * from Customer_management where Customer_name={self.entry1.get()}[0][2]")], "5", "6", "3", "3", "3", "3", "3"],
            #[self.cursor.execute(f"SELECT Customer_name from Customer_management WHERE Customer_name LIKE '%{self.entry1.get()}%'"), "5", "6", "3", "3", "3", "3", "3"],
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
                           has_checkbox=True,
                           cols=8,
                           col_name=["거래처명", "사업자번호", "거래처코드", "거래처종류", "사업자주소", "담당자", "전화번호", "e-mail"],# 열 이름(순서대로, 데이터 열 개수와 맞게)
                           col_width=[150, 110, 100, 100, 345, 100, 150, 150],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                           #col_align=["left", "center", "right", "left"],
                           editable=[True, True, True, True, True, True, True, True],
                           width=1300,  # 테이블 그려질 너비
                           height=350,
                            padding=10)  # 테이블 그려질 높이
        # col_width 생략 시 크기에 맞게 분배
        # col_name 생략 시 Col1, Col2, ... 지정

        self.app1.grid(row=0, column=0)


        self.Button = ttk.Button(self.frame2, text="검색", command=self.search)
        self.Button.place(x=250, y=10)
        self.Button = ttk.Button(self.frame2, text="수정")
        self.Button.place(x=250, y=40)
















    def recv(self,**kwargs):
        #서버로부터 받은 데이터를 테이블에 올리기 등

        # if kwargs.get("code") == 30102:
        self.data = kwargs.get("data")
        self.app1.refresh(kwargs.get("data"))


    def search(self):#버튼에 연결된 함수로 , 내부에서 서버에 send_하는 함수를 호출한다, send는 rew_data형태(json)으로 만들어서 쏴준다.,
        d = {
            "Customer_name" : self.entry1.get(), #거래처명
            "business_number" : self.entry2.get(), #사업자번호
            "Customer_code" : self.entry3.get(), #거래처코드
            "Country" : self.combobox2.get(), #국가
            }

        test_dict={
            "code":30102,
            "args": d
        }

        self.root.send_(json.dumps(test_dict, ensure_ascii=False))


    # def f30102(**kwargs):
    #
    #     result=dbm.query(f"SELECT Customer_name, business_number, Customer_code, Type_business, business_adress, ContactPerson_name, ContactPerson_phone, e_mail from Customer_management WHERE Customer_name LIKE '%{kwargs.get("Customer_name")}%'")
    #     # result=dbm.query(f"SELECT Customer_name, business_number, Customer_code, Type_business, business_adress, ContactPerson_name, ContactPerson_phone, e_mail from Customer_management WHERE Customer_name LIKE '%{kwargs.get("Customer_name")}%' or business_number LIKE '%{kwargs.get("business_number")}%' or Customer_code LIKE '%{kwargs.get("Customer_code")}%' or Country LIKE '%{kwargs.get("Country")}%'")
    #     print("결과 : ", result)
    #     if result is not None:
    #         result = {"sign": 1, "data": result}
    #     else :
    #         result = {"sign": 0, "data": None}
    #
    #
    #     return result




















        # frame3에 들어갈 것들




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
    fr = Customer_management_Frame(r)
    fr.place(x=300, y=130)
    r.mainloop()