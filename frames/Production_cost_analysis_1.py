# report_id 문서번호
# budget 예상비용
# cost_id 실제비용
# jr_account_code 계정과목코드
# product_code 제품코드

import tkinter
# import pymysql
import tkinter as tk
# from tkcalendar import Calendar
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
from tablewidget import TableWidget, ColName
from color import Color
# import naviframe
# import dbManager
import json
from tkinter import ttk as ttk
import tablewidget

class Production_cost_analysis_1(tk.Frame): #비용분석 - 1

    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root

        self.table_data = []
        # self.table2 = None
        self.scTable = None

        self.data_1 = None #과목
        self.data_2 = None #예상비용
        self.data_3 = None #실제비용

        self.scData = None

        # self.db_data = None

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
        self.frame1.grid(row=0, column=0, rowspan = 2 ,)
        self.frame2.grid(row=0, column=1)
        # self.frame3.grid(row=1, column=0)
        self.frame4.grid(row=1, column=1)

        self.table =TableWidget(self.frame1,
                                            data=None,
                                            cols = 3,
                                            new_row= True,
                                            has_checkbox=False,  # 체크박스 존재 여부
                                            col_name=["계정과목명", "예상비용", "실제비용"],  # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                            col_width=[165,360,360],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                            col_align=["center", "right", "right"],
                                            editable=[True,True, True],
                                            width=950,  # 테이블 그려질 너비
                                            height=700,
                                            padding=10
                                )  # 테이블 그려질 높이)

        self.table.grid(row=0, column=0)
        self.table.bind("<F2>", lambda e:self.on_serch('subject','jr'))

        self.frame2.columnconfigure(0, weight=1)  # 첫 번째 열 가중치
        self.frame2.columnconfigure(1, weight=1)  # 두 번째 열 가중치
        self.frame2.columnconfigure(2, weight=1)  # 세 번째 열 가중치
        self.frame2.columnconfigure(3, weight=1)  # 네 번째 열 가중치 (오른쪽 공간 확보)

        # frame2에 들어갈 것들
        # frame2에 들어갈 것들
        self.test_btn1 = ttk.Button(self.frame2, text="분석 및 결과보기",width=15, command=self.on_click)
        self.test_btn1.grid(row=0, column=2, columnspan=2, padx=23, pady=10, sticky="e")  # column=2로 조정
        # self.test_btn1.place(x=230, y=10, )  # column=2로 조정

        self.test_btn2 = ttk.Button(self.frame2, text="계정 과목 검색",width=15, command=lambda :self.on_serch('subject','table'))
        self.test_btn2.grid(row=1, column=2, columnspan=2, padx=23, pady=0, sticky="e")  # column=2로 조정
        # self.test_btn1.place(x=230, y=40, )  # column=2로 조정

        # self.test_btn2 = tk.Button(self.frame2, text="계정 과목 검색", bg=Color.BUTTON) #보류
        # self.test_btn2.place(x=230, y=0)
        # self.test_btn2.bind("<Button-1>", lambda e: self.on_key(e))
        # print(self.table.data[0]["data"][0])

    def after_init(self):
        pass

    def on_click(self):  # 분석 및 결과 보기
        for i, j in self.table.data.items():
            # print(j)      #값 가져옴
            self.data_1 = j["data"][0]  # 과목
            self.data_2 = j["data"][1]  # 예상 비용
            self.data_3 = j["data"][2]  # 실제 비용
            # 빈 값
            if not self.data_1 or not self.data_2 or not self.data_3:
                continue
            send_data = {
                "code": 40601, #분석테이블에 데이터 삽입
                "args": {
                    "insert": [self.data_1,self.data_2,self.data_3]
                }
            }
            self.send_(send_data)
        self.root.next_page()


    def send_(self,data): #분석테이블에 값 넣기
        self.root.send_(json.dumps(data, ensure_ascii=False))

    # 자동호출
    def recv(self, **kwargs):

        code = kwargs.get('code')
        sign = kwargs.get('sign')
        data = kwargs.get('data')

        if code == 40601:
            if sign == 1:
                print("f40601 sucess")

                print("sign:", kwargs.get("sign"))
                print("data:", kwargs.get("data"))
            else:
                print("f40601 fail")

                print("sign:", kwargs.get("sign"))
                print("data:", kwargs.get("data"))

        elif code == 40702 and sign == 1:
            if data:
                self.scData = data

            else:
                self.scData = [["", "", ""]]

            if self.scTable:
                self.scTable.refresh(self.scData)
            else:
                pass


    def getRow(self, table):
        if table == "sc":
            return self.scTable.data[self.scTable.get_key(self.scTable.selected_row)]

    def on_serch(self,key,cont):  #계정과목코드 , 계정과목명
        serch_data = {
            "code": 40702,
            "args": {}
        }
        self.send_(serch_data)
        if key == 'subject':
            # 확인버튼
            def confirm():
                row = self.getRow('sc')['data']
                selRow = self.table.selected_row
                # print("sc row :",row)
                data = self.table.get_data()
                # print("sc data :",data)
                for i in range(len(data)):
                    if i == selRow:
                        data[i][0] = row[1]
                    if data[i][0] == "":
                        data.pop(i)

                cancel()
                self.table.refresh(data)

            def cancel():
                self.scFrame.place_forget()
                self.table.focus_set()

            self.scFrame = tk.Frame(self, width=318, height=440, borderwidth=1, relief='solid')
            self.scData = [["", "", ""]]
            self.scTable = tablewidget.TableWidget(self.scFrame,
                                                   data=self.scData,
                                                   has_checkbox=False,
                                                   cols=3,
                                                   new_row=False,
                                                   col_name=['계정코드', '계정과목명', '유형'],
                                                   col_width=[70, 123, 60],
                                                   col_align=['center', 'left', 'center'],
                                                   editable=[False, False, False],
                                                   width=314, height=380, padding=10
                                                   )
            self.scTable.place(x=0, y=0)
            reqsctable = {'code': 40702, 'args': {}}
            self.send_(reqsctable)
            self.choiceBtn = ttk.Button(self.scFrame, text='확인', width=8, command=confirm)
            self.choiceBtn.place(x=230, y=400)
            self.cancelBtn = ttk.Button(self.scFrame, text='취소', width=8, command=cancel)
            self.cancelBtn.place(x=160, y=400)
            self.scFrame.place(x=300, y=70)
            self.scTable.focus_set()
            self.scTable.bind('<Escape>', lambda e: cancel())
            self.scTable.bind('<Button-1>', lambda e: self.scTable.focus_set())
            self.scTable.bind('<Return>', lambda e: confirm())

    '''
    @staticmethod
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
    def f40603(**kwargs):
        query = dbm.query(
            "SELECT account_code, account_name FROM journalizingbook")
        if query is not None:
            return {"sign": 1, "data": query}
        else:
        #elif not query:
            return {"sign": 0, "data": None}
    '''





# 테스트용 코드
if __name__ == "__main__":

    # dbm = dbManager.DBManager(host="localhost", user="root", password="0000", port=3306)
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    fr = Production_cost_analysis_1(r)
    fr.place(x=300, y=130)
    r.mainloop()



