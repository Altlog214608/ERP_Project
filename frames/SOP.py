import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import pymysql

import tablewidget
import tkcalendar
import json
# import dbManager

class SOP(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        self.recvData = None
        # frame 생성
        self.frame1 = tk.Frame(self, width=950, height=350, bg="grey")  # 왼쪽 위 구역
        self.frame2 = tk.Frame(self, width=350, height=350 )  # 오른쪽 위 구역
        self.frame3 = tk.Frame(self, width=1300, height=350, bg="green")  # 아래 구역

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
        self.frame_x = [10, 110, 250]
        self.frame_y = [10, 40, 70, 100, 130, 160, 190]

        # (frame 3, 4가 하나라면 아래와 같이 사용)

        # frame1에 들어갈 것들
        # self.data_f1 = [[f"Data {r + 1}{chr(65 + c)}" for c in range(4)] for r in range(5)]
        self.data_f1 = [['','','','']]


        self.app1 = tablewidget.TableWidget(self.frame1,
                                       data=self.data_f1,
                                       cols=4,
                                       col_name=["작업표준서 코드", "작업명", "작업 내용", "사진 / 사진경로"], # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                       col_width=[210, 210, 210, 210],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                       width=950,  # 테이블 그려질 너비
                                       height=350,  # 테이블 그려질 높이
                                        padding=10)
        # col_width 생략 시 크기에 맞게 분배
        # col_name 생략 시 Col1, Col2, ... 지정

        self.app1.grid(row=0, column=0)

        self.list_f1 = []
        self.list_f3 = []
        self.l3 =[]
        self.modify_list_f1 = []
        self.modify_list_f3 = []
        # self.get_frame_list()
        # 디버그용

        # frame2에 들어갈 것들
        self.SOP_Code = ttk.Label(self.frame2,text='작업표준서 코드',width=14 )
        self.SOP_Code.place(x = self.frame_x[0], y = self.frame_y[0])
        self.SOP_Code_input = ttk.Entry(self.frame2,width=15)
        self.SOP_Code_input.place(x = self.frame_x[1], y = self.frame_y[0])
        self.SOP_Refer_Button =ttk.Button(self.frame2,text='조회',command=self.refer)
        self.SOP_Refer_Button.place(x = self.frame_x[2], y = self.frame_y[0])

        self.SOP_Writter = ttk.Label(self.frame2,text='작성자',width=14)
        self.SOP_Writter.place(x = self.frame_x[0],y = self.frame_y[1])
        self.SOP_Writter_input = ttk.Entry(self.frame2,width=15)
        self.SOP_Writter_input.place(x = self.frame_x[1], y = self.frame_y[1])
        self.SOP_Create_Button = ttk.Button(self.frame2,text='생성',command=self.SOP_Create)
        self.SOP_Create_Button.place(x = self.frame_x[2], y = self.frame_y[1])

        self.SOP_Written_Date = ttk.Label(self.frame2,text='생성 날짜',width=14)
        self.SOP_Written_Date.place(x = self.frame_x[0],y = self.frame_y[2])
        self.SOP_Written_Date_input =ttk.Entry(self.frame2,width=15)
        self.SOP_Written_Date_input.place(x = self.frame_x[1],y = self.frame_y[2])
        self.SOP_Edit_Button = ttk.Button(self.frame2,text='수정',command=self.modify)
        self.SOP_Edit_Button.place(x = self.frame_x[2],y=self.frame_y[2])
        self.SOP_Written_Date_input.bind("<Button-1>", self.on_date_select)


        self.SOP_Order_Form_Code = ttk.Label(self.frame2,text='발주서 코드',width=14)
        self.SOP_Order_Form_Code.place(x = self.frame_x[0],y = self.frame_y[3])
        self.SOP_Order_Form_Code_input = ttk.Entry(self.frame2,width=15)
        self.SOP_Order_Form_Code_input.place(x = self.frame_x[1],y = self.frame_y[3])
        self.SOP_Save_Button = ttk.Button(self.frame2,text='저장',command=self.Save)
        self.SOP_Save_Button.place(x = self.frame_x[2], y = self.frame_y[3])

        self.SOP_Product_Code = ttk.Label(self.frame2,text="완제품 코드",width=14)
        self.SOP_Product_Code.place(x = self.frame_x[0],y = self.frame_y[4])
        self.SOP_Product_Code_input = ttk.Entry(self.frame2,width=15)
        self.SOP_Product_Code_input.place(x = self.frame_x[1],y = self.frame_y[4])
        self.SOP_Delete_Button = ttk.Button(self.frame2,text='상세',command=self.getdata)
        self.SOP_Delete_Button.place(x = self.frame_x[2], y = self.frame_y[4])

        self.SOP_Product_Name = ttk.Label(self.frame2,text='완제품 이름',width=14)
        self.SOP_Product_Name.place(x = self.frame_x[0],y = self.frame_y[5])
        self.SOP_Product_Name_input = ttk.Entry(self.frame2,width=15)
        self.SOP_Product_Name_input.place(x=self.frame_x[1], y=self.frame_y[5])

        self.orderxx_Button = ttk.Button(self.frame2,text='발주서 상세',command=self.a)
        self.orderxx_Button.place(x = self.frame_x[2], y = self.frame_y[5])

        # self.xxx_Button = ttk.Button(self.frame2, text='xxx', command=self.tt)
        # self.xxx_Button.place(x=self.frame_x[2], y=self.frame_y[6])

        self.get_frame3 =[]
        self.data = None

        # frame3에 들어갈 것들
        # self.data_f3 = [[f"Data {r + 1}{chr(65 + c)}" for c in range(9)] for r in range(5)]
        self.app3 = tablewidget.TableWidget(self.frame3,
                                            data=[[None,None,None,None,None,None,None]],
                                            cols=7,
                                            col_name=["작업표준서 코드", "BOM 코드", "발주서 코드", "완제품 코드", "완제품 이름", "작성자",
                                                      "생성 날짜"],
                                            # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                            col_width=[150, 150, 150, 150, 150, 150, 150],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                            width=1300,  # 테이블 그려질 너비
                                            height=350,  # 테이블 그려질 높이
                                            padding=10)
        # col_width 생략 시 크기에 맞게 분배
        # col_name 생략 시 Col1, Col2, ... 지정

        self.app3.grid(row=0, column=0)

        self.app3.bind("<Return>", lambda event: self.a(event))

        # self.app3.bind("<Double-Button-1>", lambda e: self.getdata())
        # self.get_frame_list()


    def tt(self):
        self.l3 =[]
        for i in self.app3.data:
            for j in [self.app3.data[i]['data']]:
                self.l3.append(j)
        self.l3.pop()

        keys = ['작업표준서 코드', 'BOM 코드', '발주서 코드', '자재 코드', '자재 이름', '작성자', '생성 날짜']
        values = [self.l3[-1][0], self.l3[-1][1], self.l3[-1][2], self.l3[-1][3], self.l3[-1][4], self.l3[-1][5],
                  self.l3[-1][6]]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20102,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))
        # print(self.l3)

    def a(self):
        for i in self.app3.changed['added']:
            if self.app3.changed['added'][i][2] != '':
                ordcode=self.app3.changed['added'][i][2]
                print('자재코드',ordcode)

        if ordcode!='':
            keys = ['발주서 코드']
            values = [ordcode]
            d = dict(zip(keys, values))

            send_d = {
                "code": 20107,
                "args": {'order_code':ordcode}
            }
            self.root.send_(json.dumps(send_d, ensure_ascii=False))

        # data_f3 = [[f"Data {r + 1}{chr(65 + c)}" for c in range(8)] for r in range(8)]
        # self.data = None
    def getdata(self): #더블클릭에 대한 문서조회
        # print("getdata getdata getdata getdata getdata getdata getdata getdata getdata ")
        self.data = self.app3.data[self.app3.selected_row]['data'][0]
        # print("self.data :", self.app3.get())

        keys = ['작업표준서 코드']
        values = [self.data]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20106,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))
        # self.get_frame1_list()

        # 디버그용
        # self.app3.bind("<F5>", lambda e: self.test())
        # self.app3.bind("<F5>", lambda e: self.getChanged())



    def after_init(self):
        self.refer()
        # self.getdata()

    def test_function(self, e):
        msgbox.showinfo("제목", self.test_entry.get())

    def on_date_select(self, event):  # 캘린더 생성
        self.cal = tkcalendar.Calendar(self.frame2, firstweekday="sunday", locale="ko_KR", showweeknumbers=False)
        self.cal.place(x=60, y=20)
        self.cal.bind("<<CalendarSelected>>", self.select_date)

    def select_date(self, event):  # 선택된 날짜를 엔트리에 입력
        self.SOP_Written_Date_input.delete(0, tk.END)
        self.SOP_Written_Date_input.insert(0, self.cal.selection_get())
        self.cal.destroy()  # 캘린더 닫기

    def get_frame_list(self):
        for i in self.app3.data:
            for j in [self.app3.data[i]['data']]:
                self.list_f3.append(j)
        print(self.list_f3)

    def get_frame1_list(self):
        self.list_f1 =[]
        for i in self.app1.data:
            for j in [self.app1.data[i]['data']]:
                self.list_f1.append(j)
        print('self.list_f1 : ',self.list_f1)
        # print(self.app1.changed)

    def f1_changed(self):
        f1_changed_row =[]
        for i in self.app1.changed['updated']:
            f1_changed_row.append(i)
            print('changed_row', f1_changed_row)
            self.modify_list_f1.append(self.app1.changed['updated'][i])
        print("modify_list_f1", self.modify_list_f1)

        keys = ['modify_lsit', 'change_row','list_f1','']  # db의 문서테이블 이름
        values = [self.modify_list_f1, f1_changed_row,self.list_f1]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20105,########################################################
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

    def modify(self):
        changed_row = []
        self.modify_list_f3 = []
        for i in self.app3.changed['updated']:
            changed_row.append(i)
            print('changed_row',changed_row)
            self.modify_list_f3.append(self.app3.changed['updated'][i])
        print("modify_list_f3",self.modify_list_f3)

        keys = ['수정리스트', '수정 행', 'pk']  # db의 문서테이블 이름
        values = [self.modify_list_f3, changed_row, self.list_f3]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20103,  ########################################################
            "args": d
        }

        print("d", send_d)
        print('values[0] : ',values[0])

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

        # for i in [self.modify_list_f3]:
        #     for j in i:
        #         print(j)
        #         for k in changed_row:
        #             (f"update sop set sop_code = '{j[0]}' ,bom_code = '{j[1]}',order_code = '{j[2]}',material_code = '{j[3]}',material_name = '{j[4]}',writter = '{j[5]}',written_date = '{j[6]}' where sop_code = '{self.list_f3[k][0]}' " )

        self.f1_changed()



    def recv(self,**kwargs):
        print("code :",kwargs.get("code"))
        print("sign :", kwargs.get("sign"))
        print("data :", kwargs.get("data"))

        if kwargs.get("sign") ==1:
            if kwargs.get("code") == 20101: # 조회버툰 가져온걸 다시 그림
                # print(kwargs.get("data"))
                self.get_frame3=kwargs.get("data")
                self.app3 = tablewidget.TableWidget(self.frame3,
                                                    data=kwargs.get("data"),
                                                    cols=7,
                                                    col_name=["작업표준서 코드", "BOM 코드", "발주서 코드", "완제품 코드", "완제품 이름", "작성자",
                                                              "생성 날짜"],
                                                    # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                                    col_width=[150, 150, 150, 150, 150, 150, 150],
                                                    # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                                    width=1300,  # 테이블 그려질 너비
                                                    height=350,
                                                    padding=10)  # 테이블 그려질 높이

                self.app3.grid(row=0, column=0)

            elif kwargs.get("code") == 20102: #frame3 생성
                pass
            elif kwargs.get("code") == 20103: # 수정
                pass
            elif kwargs.get("code") == 20104: # 저장
                pass
            elif kwargs.get("code") == 20106: #프레임 1번의 조회
                self.app1 = tablewidget.TableWidget(self.frame1,
                                                    data=kwargs.get("data"),
                                                    cols=4,
                                                    col_name=["작업표준서 코드", "작업명", "작업 내용", "사진 / 사진경로"],
                                                    # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                                    col_width=[210, 210, 210, 210],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                                    width=950,  # 테이블 그려질 너비
                                                    height=350,
                                                    padding=10)  # 테이블 그려질 높이
                # col_width 생략 시 크기에 맞게 분배
                # col_name 생략 시 Col1, Col2, ... 지정
                self.app1.grid(row=0, column=0)
                # self.app1.refresh(kwargs.get('data'))
                self.list_f1 = kwargs.get("data")

            elif kwargs.get("code") == 20107:
                print(kwargs.get("data"))
                print(self.get_frame3)
                list=['','',kwargs.get("data")[0][0],kwargs.get("data")[0][1],kwargs.get("data")[0][2],'','']
                self.get_frame3.append(list)
                print('재조회',self.get_frame3)

                self.app3 = tablewidget.TableWidget(self.frame3,
                                                    data=self.get_frame3,
                                                    cols=7,
                                                    col_name=["작업표준서 코드", "BOM 코드", "발주서 코드", "완제품 코드", "완제품 이름", "작성자",
                                                              "생성 날짜"],
                                                    # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                                    col_width=[150, 150, 150, 150, 150, 150, 150],
                                                    # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                                    width=1300,  # 테이블 그려질 너비
                                                    height=350,
                                                    padding=10)  # 테이블 그려질 높이

                self.app3.grid(row=0, column=0)


    # @staticmethod
    # @MsgProcessor
    # def f20101(**kwargs):
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #         # print(f'Index: {i}, Value: {value}')
    #     query = f"SELECT * FROM sop where (sop_Code like '%%{valueList[0]}%%' and writter like '%%{valueList[1]}%%' and written_date like '%%{valueList[2]}%%' and order_code like '%%{valueList[3]}%%' and material_code like '%%{valueList[4]}%%' and material_name like '%%{valueList[5]}%%') "
    #     result = dbm.query(query, [])
    #     print("result", result)
    #
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     elif not query:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20102(**kwargs):
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"insert into sop values('{valueList[0]}', '{valueList[1]}','{valueList[2]}','{valueList[3]}','{valueList[4]}','{valueList[5]}','{valueList[6]}')"
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     elif not query:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20103(**kwargs):  # 프레임3 수정
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #         # print(f'Index: {i}, Value: {value}
    #     for i in valueList[0]:
    #         # print('i :', i) #i : ['sop33', '', '수정', '', '', '', '']
    #         # print('i[0]',i[0])
    #         query = f"update sop set sop_code = '{i[0]}' ,bom_code = '{i[1]}',order_code = '{i[2]}',material_code = '{i[3]}',material_name = '{i[4]}',writter = '{i[5]}',written_date = '{i[6]}' where sop_code = '{i[0]}' "  # valueList[2][k][0]
    #         result = dbm.query(query, [])
    #
    #         print("result", result)
    #
    #         if query:
    #             return {"sign": 1, 'data': result}
    #         elif not query:
    #             return {"sign": 0, 'data': None}
    #         # for j in i:
    #         # for k in valueList[1]:
    #
    # @staticmethod
    # @MsgProcessor
    # def f20104(**kwargs):
    #     valueList = []
    #
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"insert into sop_f values('{valueList[0]}', '{valueList[1]}','{valueList[2]}','{valueList[3]}')"
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     elif not query:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20105(**kwargs):  # 프레임1 수정
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #         # print(f'Index: {i}, Value: {value}')
    #     # print('valueList[0]', valueList[1][0])
    #     # print('valueList[2][valueList[0]][0]', valueList[2][valueList[1][0]][0],)
    #     print(valueList[2], 1111111111)
    #
    #     for i in valueList[0]:
    #         query = f"update sop_f set sop_code = '{i[0]}' ,work_name = '{i[1]}',working = '{i[2]}',photo = '{i[3]}' where (work_name = '{valueList[2][valueList[1][0]][1]}' )"  # valueList[2][k][0]
    #     result = dbm.query(query, [])
    #     print("result", result)
    #
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     elif not query:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20106(**kwargs):  # 문서더블클릭
    #     valueList = []
    #
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"SELECT * FROM sop_f WHERE sop_code = '{valueList[0]}' "
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     elif not query:
    #         return {"sign": 0, 'data': None}

    # @staticmethod
    # @MsgProcessor
    # def f20107(**kwargs):  # 문서더블클릭
    #     valueList = []
    #
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"SELECT order_code, product_code, product_name FROM order_form WHERE order_code = '{valueList[0]}' "
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     elif not query:
    #         return {"sign": 0, 'data': None}


    def refer(self): # 조회버튼
        def getsop():
            return self.SOP_Code_input.get()
        def getwritter():
            return self.SOP_Writter_input.get()
        def getdate():
            return self.SOP_Written_Date_input.get()
        def getorder():
            return self.SOP_Order_Form_Code_input.get()
        def getproductcode():
            return self.SOP_Product_Code_input.get()
        def getproductName():
            return self.SOP_Product_Name_input.get()

        keys = ['작업표준서 코드', '작성자', '생성 날짜', '발주서 코드', '자재 코드','자재 이름']
        values = [getsop(), getwritter(), getdate(), getorder(),getproductcode() ,getproductName()]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20101,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

    @staticmethod
    def f20107(**kwargs):
        pass

    def SOP_Create(self):
        self.tt()

        addList = [] # 추가입력된 값들이 들어갈 리스트
        for i in self.app3.changed['added']:
            if self.app3.changed['added'][i][0] != '':
                addList.append(self.app3.changed['added'][i])
        # if addList != None:
        for j in range(len(addList)):  # 0,1
             # 커서란 sql쿼리를 실행하고 받아오는 객체
            query = f"insert into sop values('{addList[j][0]}', '{addList[j][1]}','{addList[j][2]}','{addList[j][3]}','{addList[j][4]}','{addList[j][5]}','{addList[j][6]}')"

            keys = ['작업표준서 코드', 'BOM 코드', '발주서 코드', '자재 코드', '자재 이름', '작성자','생성 날짜']
            values = [addList[j][0], addList[j][1], addList[j][2], addList[j][3], addList[j][4], addList[j][5],addList[j][6]]
            d = dict(zip(keys, values))

        #################################################################
            send_d = {
                "code": 20102,
                "args": d
            }

            print("d", send_d)

            self.root.send_(json.dumps(send_d, ensure_ascii=False))
    #################################################################
        # else:
        #     self.tt()


    def Save(self): #생성 버튼 클릭 시 문서 테이블 또한 생성되야함, 문서 내용 저장 시 해당 문서 테이블에 저장되야 하는데
        addList = []
        for i in self.app1.changed['added']:
            if self.app1.changed['added'][i][0] != '':
                addList.append(self.app1.changed['added'][i])
        for j in range(len(addList)):  # 0,1
            keys = ['작업표준서 코드','작업명', '작업 내용', '사진'] # db의 문서테이블 이름
            values = [addList[j][0], addList[j][1], addList[j][2], addList[j][3]]
            d = dict(zip(keys, values))

            send_d = {
                "code": 20104,
                "args": d
            }

            print("d", send_d)

            self.root.send_(json.dumps(send_d, ensure_ascii=False))
        self.modify()





        # keys = ['작업표준서 코드', '작업명', '작업 내용', '사진']  # db의 문서테이블 이름
        # values = [addList[j][0], addList[j][1], addList[j][2], addList[j][3]]
    # def delete(self):
    #     addList = []
    #     for i in self.app3.changed['deleted']:
    #         if self.app1.changed['deleted'][i][0] != '':
    #             addList.append(self.app1.changed['deleted'][i])
    #     for j in range(len(addList)):  # 0,1
    #         connection = pymysql.connect(
    #             host='localhost',  # 접속하려는 주소 ip 지정 // cmd ipconfig //내 주소 : localhost
    #             user='root',  # 해당 ip에 mysql서버 계정
    #             password='0000',  # 해당 계정의 pw
    #             database='ERP',  # 접속하려는 DB이름
    #             port=3306  # 포트번호
    #         )
    #         print('addList[j][0] :', addList[j][0])
    #         cursor = connection.cursor()  # 커서란 sql쿼리를 실행하고 받아오는 객체
    #         cursor.execute(
    #             f"delete from sop where sop_code = {addList[j][0]}")
    #         connection.commit()
    #         tables = cursor.fetchall()
    #
    #         cursor.close()  # 객체를 닫는다
    #         connection.close()
    #     keys = ['code', '작업표준서 코드', '작업명', '작업 내용', '사진', '문서명']  # db의 문서테이블 이름
    #     values = ['f20202', addList[j][0], addList[j][1], addList[j][2], addList[j][3], self.data]
    #     d = dict(zip(keys, values))
    #     self.app3.grid(row=0, column=0)
    #     return self.f20104(**d)

    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ



# 테스트용 코드
if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    fr = SOP(r)
    fr.place(x=300, y=130)
    r.mainloop()