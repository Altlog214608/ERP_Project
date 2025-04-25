import datetime
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import pymysql
import tablewidget
import tkcalendar
import  json


class Manufacturing_Order(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        self.dict ={}        # frame 생성
        self.add_dict = {}
        self.frame1 = tk.Frame(self, width=950, height=350)  # 왼쪽 위 구역
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
        self.frame_y = [10, 40, 70, 100, 130, 160, 190,220,250]

        # (frame 3, 4가 하나라면 아래와 같이 사용)

        # frame1에 들어갈 것들 신규 생성
        self.Man_Order_Code_f1 = ttk.Label(self.frame1,text='생산지시서 코드',width=14)
        self.Man_Order_Code_f1.place(x = self.frame_x[0], y = self.frame_y[0])
        self.Man_Order_Code_input_f1 = ttk.Entry(self.frame1,state=tk.DISABLED,width=17)
        self.Man_Order_Code_input_f1.place(x = self.frame_x[1], y = self.frame_y[0])

        self.sop_list =[]
        self.Man_SOP_Code_f1 = ttk.Label(self.frame1,text='작업표준서 코드',width=14)
        self.Man_SOP_Code_f1.place(x = self.frame_x[0],y = self.frame_y[1])
        self.Man_SOP_Code_input_f1 = ttk.Combobox(self.frame1,state=tk.DISABLED,width=15,values=self.sop_list)
        self.Man_SOP_Code_input_f1.place(x = self.frame_x[1], y = self.frame_y[1])

        self.Man_BOM_Code_f1 = ttk.Label(self.frame1, text='BOM 코드', width=14)
        self.Man_BOM_Code_f1.place(x=self.frame_x[0], y=self.frame_y[2])
        self.Man_BOM_Code_input_f1 = ttk.Entry(self.frame1,state=tk.DISABLED, width=17)
        self.Man_BOM_Code_input_f1.place(x=self.frame_x[1], y=self.frame_y[2])

        self.Man_Quantity_f1 = ttk.Label(self.frame1,text="제작 수량", width=14)
        self.Man_Quantity_f1.place(x = self.frame_x[0],y = self.frame_y[3])
        self.Man_Quantity_f1_input = ttk.Entry(self.frame1,text="제작 수량",state=tk.DISABLED, width=17)
        self.Man_Quantity_f1_input.place(x = self.frame_x[1],y = self.frame_y[3])

        statement = ["생산계획", "생산중", "생산 완료"]
        self.Man_Statement_f1 = ttk.Label(self.frame1, text='진행 상태', width=14)
        self.Man_Statement_f1.place(x = self.frame_x[0],y = self.frame_y[4])
        self.Man_Statement_input_f1 = ttk.Combobox(self.frame1, values=statement, width=15,state=tk.DISABLED)
        self.Man_Statement_input_f1.place(x = self.frame_x[1],y = self.frame_y[4])

        self.Man_Product_Code_f1 = ttk.Label(self.frame1, text="완제품 코드",width=14)
        self.Man_Product_Code_f1.place(x = self.frame_x[0],y = self.frame_y[5])
        self.Man_Product_Code_input_f1 = ttk.Entry(self.frame1, text="완제품 코드",state=tk.DISABLED,width=17)
        self.Man_Product_Code_input_f1.place(x=self.frame_x[1], y=self.frame_y[5])

        self.Man_Product_Name_f1 =ttk.Label(self.frame1, text="완제품 이름", width=14)
        self.Man_Product_Name_f1.place(x = self.frame_x[0], y = self.frame_y[6])
        self.Man_Product_Name_input_f1 =ttk.Entry(self.frame1,state=tk.DISABLED, width=17)
        self.Man_Product_Name_input_f1.place(x=self.frame_x[1], y=self.frame_y[6])

        self.Man_Order_Form_Code_f1 = ttk.Label(self.frame1, text="발주서 코드", width=14)
        self.Man_Order_Form_Code_f1.place(x=self.frame_x[0], y=self.frame_y[7])
        self.Man_Order_Form_Codeinput_f1 = ttk.Entry(self.frame1,state=tk.DISABLED, width=17)
        self.Man_Order_Form_Codeinput_f1.place(x=self.frame_x[1], y=self.frame_y[7])

        self.Man_DueDay_input_f1 = ttk.Label(self.frame1,text="마감 날짜", width=14)
        self.Man_DueDay_input_f1.place(x = self.frame_x[0],y = self.frame_y[8])
        self.Man_DueDay_Button_f1 = ttk.Entry(self.frame1, state=tk.DISABLED, width=17)
        self.Man_DueDay_Button_f1.place(x=self.frame_x[1], y=self.frame_y[8])
        self.Man_DueDay_Button_f1.bind("<Button-1>", self.on_date_select)

        self.list_f1 = []
        self.list_f3 = []
        self.modify_list_f1 = []
        self.modify_list_f3 = []
        # self.get_frame_list()



        # self.test_entry = tk.Entry(self.frame1)
        # self.test_entry.grid(row=1)
        # self.test_entry.bind("<Return>", self.test_function)

        # frame2에 들어갈 것들 조회
        self.frame2_x = [10, 110, 250]
        self.frame2_y = [10, 40, 70, 100, 130, 160, 190]
        self.Man_Order_Code_f2 = ttk.Label(self.frame2,text='생산지시서 코드',width=14)
        self.Man_Order_Code_f2.place(x = self.frame2_x[0], y = self.frame2_y[0])
        self.Man_Order_Code_input_f2 = ttk.Entry(self.frame2, width=15)
        self.Man_Order_Code_input_f2.place(x = self.frame2_x[1], y = self.frame2_y[0])
        self.Man_Refer_Button_f2 =ttk.Button(self.frame2,text='조회',command=self.refer)
        self.Man_Refer_Button_f2.place(x = self.frame2_x[2], y = self.frame2_y[0])

        self.Man_SOP_Code_f2 = ttk.Label(self.frame2,text='작업표준서 코드',width=14)
        self.Man_SOP_Code_f2.place(x = self.frame2_x[0],y = self.frame2_y[1])
        self.Man_SOP_Code_input_f2 = ttk.Entry(self.frame2, width=15)
        self.Man_SOP_Code_input_f2.place(x = self.frame2_x[1], y = self.frame2_y[1])
        # self.Man_Create_Button_f2 = ttk.Button(self.frame2,text='생성',command=self.Create)
        # self.Man_Create_Button_f2.place(x = self.frame2_x[2], y = self.frame2_y[1])
        self.Man_Edit_Button_f2 = ttk.Button(self.frame2, text='수정', command=self.Modify)
        self.Man_Edit_Button_f2.place(x=self.frame2_x[2], y=self.frame2_y[1])

        self.Man_BOM_Code_f2 = ttk.Label(self.frame2,text='BOM 코드', width=14)
        self.Man_BOM_Code_f2.place(x = self.frame2_x[0],y = self.frame2_y[2])
        self.Man_BOM_Code_input_f2 =ttk.Entry(self.frame2,width=15)
        self.Man_BOM_Code_input_f2.place(x = self.frame2_x[1],y = self.frame2_y[2])
        self.Man_Save_Button_f2 = ttk.Button(self.frame2, text='저장', command=self.Create)
        self.Man_Save_Button_f2.place(x=self.frame2_x[2], y=self.frame2_y[2])

        self.Man_Order_Form_Code_f2 = ttk.Label(self.frame2, text='발주서 코드',width=14)
        self.Man_Order_Form_Code_f2.place(x=self.frame2_x[0], y=self.frame2_y[3])
        self.Man_Order_Form_Code_input_f2 = ttk.Entry(self.frame2,width=15)
        self.Man_Order_Form_Code_input_f2.place(x=self.frame2_x[1], y=self.frame2_y[3])


        self.Man_Product_Code_f2 = ttk.Label(self.frame2,text="완제품 코드",width=14)
        self.Man_Product_Code_f2.place(x = self.frame2_x[0],y = self.frame2_y[4])
        self.Man_Product_Code_input_f2 = ttk.Entry(self.frame2,width=15)
        self.Man_Product_Code_input_f2.place(x = self.frame2_x[1],y = self.frame2_y[4])
        # self.Man_Delete_Button_f2 = tk.Button(self.frame2,text='삭제')
        # self.Man_Delete_Button_f2.place(x = self.frame2_x[2], y = self.frame2_y[4])

        self.Man_Product_Name_f2 = ttk.Label(self.frame2,text='완제품 이름',width=14)
        self.Man_Product_Name_f2.place(x = self.frame2_x[0],y = self.frame2_y[5])
        self.Man_Product_Name_input_f2 = ttk.Entry(self.frame2,width=15)
        self.Man_Product_Name_input_f2.place(x=self.frame2_x[1], y=self.frame2_y[5])

        # frame3에 들어갈 것들
        # data_f3 = [["생산지시서 코드","작업표준서 코드", "BOM 코드", "제작 수량", "진행 상태", "완제품 코드", "발주처 코드"] ,[1,2,3]]  # 임의의 데이터
        # self.data_f3 = [[f"Data {r + 1}{chr(65 + c)}" for c in range(9)] for r in range(5)]
        self.app1 = tablewidget.TableWidget(self.frame3,
                                            data=[[None,None,None,None,None,None,None,None,None]],
                                            cols=9,
                                            col_name=["생산지시서 코드", "작업표준서 코드", "BOM 코드", "제작 수량", "진행 상태", "완제품 코드",
                                                      "완제품 이름", "발주처 코드", "작업 기한"],  # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                            col_width=[135, 135, 135, 135, 135, 135, 135, 135, 135],
                                            # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                            new_row=False,
                                            width=1300,  # 테이블 그려질 너비
                                            height=350,
                                            padding=10)  # 테이블 그려질 높이
        # col_width 생략 시 크기에 맞게 분배
        # col_name 생략 시 Col1, Col2, ... 지정

        self.app1.grid(row=0, column=0)

        # 디버그용
        self.frame3.bind("<F5>", lambda e: test())
        self.Man_BOM_Code_input_f1.bind('<Button-1>',self.bom_config)
        self.Man_Quantity_f1_input.bind('<Button-1>', self.prod_code)
        self.Man_Order_Code_input_f1.bind('<Button-1>',self.sop_com)

        def test():
            print(f"data: {self.app1.data}")  # 저장된 데이터
            print(f"rows cols: {self.app1.rows} {self.app1.cols}")  # 행 열 개수
            print(f"selected: {self.app1.selected_row} {self.app1.selected_col}")  # 선택된 행 열 index
            print(f"changed {self.app1.changed}")  # 원본 대비 변경된 데이터

    def after_init(self):
        self.refer()

    # def get_frame_list(self):
    #     for i in self.app1.data:
    #         for j in [self.app1.data[i]['data']]:
    #             self.list_f3.append(j)
    #     print(self.list_f3)

    def test_function(self, e):
        msgbox.showinfo("제목", self.test_entry.get())

    def on_date_select(self, event):  # 캘린더 생성
        self.cal = tkcalendar.Calendar(self.frame1, firstweekday="sunday", locale="ko_KR", showweeknumbers=False)
        self.cal.place(x=60, y=200)
        self.cal.bind("<<CalendarSelected>>", self.select_date)

    def select_date(self, event):  # 선택된 날짜를 엔트리에 입력
        self.Man_DueDay_Button_f1.delete(0, tk.END)
        self.Man_DueDay_Button_f1.insert(0, self.cal.selection_get())
        self.cal.destroy()  # 캘린더 닫기

    def modify2(self):
        changed_row = []
        self.modify_list_f3=[]
        for i in self.app1.changed['updated']:
            changed_row.append(i)
            print('changed_row',changed_row)
            print("self.app1.changed['updated'][i] : ", self.app1.changed['updated'][i])
            self.modify_list_f3.append(self.app1.changed['updated'][i])
        print("modify_list_f3",self.modify_list_f3)

        keys = ['수정리스트', '수정 행', 'pk']  # db의 문서테이블 이름
        values = [self.modify_list_f3, changed_row, self.list_f3]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20305,  ########################################################
            "args": d
        }

        print("d", send_d)
        print('values[0] : ',values[0])

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

    def sop_com(self,e): #frame1 작업표준서 콤보박스 리셋

        keys = ['x']
        values = ['x']
        d = dict(zip(keys, values))

        send_d = {
            "code": 20304,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

    def bom_config(self,e): #f20303

        keys = ['작업표준서 코드']
        values = [self.getSopF1()]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20303,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

    def prod_code(self,e):

        keys = ['bom 코드']
        values = [self.getBomF1()]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20306,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))


    # @staticmethod
    # @MsgProcessor
    # def f20301(**kwargs):
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"SELECT * FROM mo where (mo_code like '%%{valueList[0]}%%' and sop_code like '%%{valueList[1]}%%' and bom_code like '%%{valueList[2]}%%' and order_code like '%%{valueList[3]}%%' and material_code like '%%{valueList[4]}%%' and material_name like '%%{valueList[5]}%%') "
    #
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     else:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20302(**kwargs):
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"INSERT INTO mo values('{valueList[0]}','{valueList[1]}','{valueList[2]}','{valueList[3]}','{valueList[4]}','{valueList[5]}','{valueList[6]}','{valueList[7]}','{valueList[8]}') "
    #
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     else:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20303(**kwargs):
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"SELECT * FROM sop WHERE sop_code = '{valueList[0]}'"
    #
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     else:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20304(**kwargs):
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"SELECT sop_code FROM sop"
    #
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     else:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20305(**kwargs):  # 프레임3 수정
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #         # print(f'Index: {i}, Value: {value}
    #     for i in valueList[0]:
    #         # print('i :', i) #i : ['sop33', '', '수정', '', '', '', '']
    #         print('i[0]', i[0])
    #         query = f"update mo set mo_code = '{i[0]}' ,sop_code = '{i[1]}',bom_code = '{i[2]}',quantity = '{i[3]}',state = '{i[4]}',material_code = '{i[5]}',material_name = '{i[6]}', order_code = '{i[7]}', due_date = '{i[8]}' WHERE mo_code = '{i[0]}' "  # valueList[2][k][0]
    #         result = dbm.query(query, [])
    #
    #         print("result", result)
    #
    #         if query:
    #             return {"sign": 1, 'data': result}
    #         elif not query:
    #             return {"sign": 0, 'data': None}

    # @staticmethod
    # @MsgProcessor
    # def f20306(**kwargs):  # 프레임3 수정
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #         # print(f'Index: {i}, Value: {value}
    #     for i in valueList[0]:
    #         # print('i :', i) #i : ['sop33', '', '수정', '', '', '', '']
    #         print('i[0]', i[0])
    #         query = f"SELECT material_code FROM bom_f WHERE sop_code = '{valueList[0]}'"
    #         result = dbm.query(query, [])
    #
    #         print("result", result)
    #
    #         if query:
    #             return {"sign": 1, 'data': result}
    #         elif not query:
    #             return {"sign": 0, 'data': None}

    def getmo(self):
        return self.Man_Order_Code_input_f2.get()
    def getsop(self):
        return self.Man_SOP_Code_input_f2.get()
    def getbom(self):
        return self.Man_BOM_Code_input_f2.get()
    def getorder(self):
        return self.Man_Order_Form_Code_input_f2.get()
    def getprodcode(self):
        return self.Man_Product_Code_input_f2.get()
    def getprodname(self):
        return self.Man_Product_Name_input_f2.get()

    def refer(self):
        def getmo():
            return self.Man_Order_Code_input_f2.get()
        def getsop():
            return self.Man_SOP_Code_input_f2.get()
        def getbom():
            return self.Man_BOM_Code_input_f2.get()
        def getorder():
            return self.Man_Order_Form_Code_input_f2.get()
        def getprodcode():
            return self.Man_Product_Code_input_f2.get()
        def getprodname():
            return self.Man_Product_Name_input_f2.get()

        keys = ['생산지시서 코드', '작업표준서 코드', 'BOM 코드', '발주서 코드','완제품 코드', '완제품 이름']
        values = [getmo(), getsop(), getbom(), getorder(),getprodcode(), getprodname()]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20301,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

    def recv(self,**kwargs):
        print("code :",kwargs.get("code"))
        print("sign :", kwargs.get("sign"))
        print("data :", kwargs.get("data"))

        if kwargs.get("sign") ==1 and kwargs.get("code") == 20301:
            print('kwargs.get("data") : ',kwargs.get("data"))
            self.app1 = tablewidget.TableWidget(self.frame3,
                                                data=kwargs.get("data"),
                                                cols=9,
                                                col_name=["생산지시서 코드", "작업표준서 코드", "BOM 코드", "제작 수량", "진행 상태", "완제품 코드",
                                                          "완제품 이름", "발주처 코드", "작업 기한"],  # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                                col_width=[135, 135, 135, 135, 135, 135, 135, 135, 135],
                                                # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                                new_row=False,
                                                width=1300,  # 테이블 그려질 너비
                                                height=350,
                                                padding=10)  # 테이블 그려질 높이
            # col_width 생략 시 크기에 맞게 분배
            # col_name 생략 시 Col1, Col2, ... 지정

            self.app1.grid(row=0, column=0)

        if kwargs.get("sign") ==1 and kwargs.get("code") == 20302:
            print('kwargs.get("data") : ',kwargs.get("data"))

        if kwargs.get("sign") ==1 and kwargs.get("code") == 20303:
            tables = kwargs.get("data")
            self.Man_BOM_Code_input_f1.insert(0, tables[0][1])
            self.Man_Order_Form_Codeinput_f1.insert(0, tables[0][2])
            self.Man_Product_Code_input_f1.insert(0, tables[0][3])
            self.Man_Product_Name_input_f1.insert(0, tables[0][4])

        if kwargs.get("sign") ==1 and kwargs.get("code") == 20304:
            tables = kwargs.get("data")
            for i in tables:
                if len(self.sop_list) != len(tables):
                    self.sop_list.append(i)

            self.Man_SOP_Code_input_f1 = ttk.Combobox(self.frame1, values=self.sop_list,width=15)
            self.Man_SOP_Code_input_f1.place(x=self.frame_x[1], y=self.frame_y[1])

        if kwargs.get("sign") ==1 and kwargs.get("code") == 20306:
            tables = kwargs.get("data")
            print(11111111,kwargs.get("data"))
            for i in tables:
                self.product_Code_combo.append(i)

            self.Man_Product_Code_input_f1 = ttk.Combobox(self.frame1, text="완제품 코드", state=tk.DISABLED, width=15,values=self.product_Code_combo)
            self.Man_Product_Code_input_f1.place(x=self.frame_x[1], y=self.frame_y[5])


    def getMoF1(self):
        return self.Man_Order_Code_input_f1.get()

    def getSopF1(self):
        return self.Man_SOP_Code_input_f1.get()

    def getBomF1(self):
        return self.Man_BOM_Code_input_f1.get()

    def getQuntityF1(self):
        return self.Man_Quantity_f1_input.get()

    def getStateF1(self):
        return self.Man_Statement_input_f1.get()

    def getProdCodeF1(self):
        return self.Man_Product_Code_input_f1.get()

    def getProdNameF1(self):
        return self.Man_Product_Code_input_f1.get()

    def getOrderF1(self):
        return self.Man_Product_Code_input_f1.get()

    def getDueF1(self):
        return self.Man_DueDay_Button_f1.get()

    def Create(self):
        keys = [ '생산지시서 코드', '작업표준서 코드', 'BOM 코드', '제작 수량', '진행 상태', '완제품 코드', '완제품 이름', '발주처 코드', '작업기한']
        values = [self.getMoF1(), self.getSopF1(), self.getBomF1(), self.getQuntityF1(), self.getStateF1(), self.getProdCodeF1(),self.getProdNameF1(), self.getOrderF1(),self.getDueF1()]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20302,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

        self.Man_Order_Code_f1 = ttk.Label(self.frame1, text='생산지시서 코드', width=14)
        self.Man_Order_Code_f1.place(x=self.frame_x[0], y=self.frame_y[0])
        self.Man_Order_Code_input_f1 = ttk.Entry(self.frame1, state=tk.DISABLED, width=17)
        self.Man_Order_Code_input_f1.place(x=self.frame_x[1], y=self.frame_y[0])

        self.sop_list = []
        self.Man_SOP_Code_f1 = ttk.Label(self.frame1, text='작업표준서 코드', width=14)
        self.Man_SOP_Code_f1.place(x=self.frame_x[0], y=self.frame_y[1])
        self.Man_SOP_Code_input_f1 = ttk.Combobox(self.frame1, state=tk.DISABLED, width=15, values=self.sop_list)
        self.Man_SOP_Code_input_f1.place(x=self.frame_x[1], y=self.frame_y[1])

        self.Man_BOM_Code_f1 = ttk.Label(self.frame1, text='BOM 코드', width=14)
        self.Man_BOM_Code_f1.place(x=self.frame_x[0], y=self.frame_y[2])
        self.Man_BOM_Code_input_f1 = ttk.Entry(self.frame1, state=tk.DISABLED, width=17)
        self.Man_BOM_Code_input_f1.place(x=self.frame_x[1], y=self.frame_y[2])

        self.Man_Quantity_f1 = ttk.Label(self.frame1, text="제작 수량", width=14)
        self.Man_Quantity_f1.place(x=self.frame_x[0], y=self.frame_y[3])
        self.Man_Quantity_f1_input = ttk.Entry(self.frame1, text="제작수량", state=tk.DISABLED, width=17)
        self.Man_Quantity_f1_input.place(x=self.frame_x[1], y=self.frame_y[3])
        # self.Man_Quantity_f1_input.insert(0,'')

        statement = ["생산계획", "생산중", "생산 완료"]
        self.Man_Statement_f1 = ttk.Label(self.frame1, text='진행 상태', width=14)
        self.Man_Statement_f1.place(x=self.frame_x[0], y=self.frame_y[4])
        self.Man_Statement_input_f1 = ttk.Combobox(self.frame1, values=statement, width=15, state=tk.DISABLED)
        self.Man_Statement_input_f1.place(x=self.frame_x[1], y=self.frame_y[4])

        self.Man_Product_Code_f1 = ttk.Label(self.frame1, text="완제품 코드", width=14)
        self.Man_Product_Code_f1.place(x=self.frame_x[0], y=self.frame_y[5])
        self.Man_Product_Code_input_f1 = ttk.Entry(self.frame1, text="완제품코드", state=tk.DISABLED, width=17)
        self.Man_Product_Code_input_f1.place(x=self.frame_x[1], y=self.frame_y[5])
        # self.Man_Product_Code_input_f1.insert(0,'')

        self.Man_Product_Name_f1 = ttk.Label(self.frame1, text="완제품 이름", width=14)
        self.Man_Product_Name_f1.place(x=self.frame_x[0], y=self.frame_y[6])
        self.Man_Product_Name_input_f1 = ttk.Entry(self.frame1, state=tk.DISABLED, width=17)
        self.Man_Product_Name_input_f1.place(x=self.frame_x[1], y=self.frame_y[6])

        self.Man_Order_Form_Code_f1 = ttk.Label(self.frame1, text="발주서 코드", width=14)
        self.Man_Order_Form_Code_f1.place(x=self.frame_x[0], y=self.frame_y[7])
        self.Man_Order_Form_Codeinput_f1 = ttk.Entry(self.frame1, state=tk.DISABLED, width=17)
        self.Man_Order_Form_Codeinput_f1.place(x=self.frame_x[1], y=self.frame_y[7])

        self.Man_DueDay_input_f1 = ttk.Label(self.frame1, text="마감 날짜", width=14)
        self.Man_DueDay_input_f1.place(x=self.frame_x[0], y=self.frame_y[8])
        self.Man_DueDay_Button_f1 = ttk.Entry(self.frame1, state=tk.DISABLED, width=17)
        self.Man_DueDay_Button_f1.place(x=self.frame_x[1], y=self.frame_y[8])


    def Modify(self):
        self.Man_Order_Code_input_f1.config(state = tk.NORMAL)
        self.Man_SOP_Code_input_f1.config(state=tk.NORMAL)
        self.Man_BOM_Code_input_f1.config(state=tk.NORMAL)
        self.Man_Quantity_f1_input.config(state=tk.NORMAL)
        self.Man_Statement_input_f1.config(state=tk.NORMAL)
        self.Man_Product_Code_input_f1.config(state=tk.NORMAL)
        self.Man_Product_Name_input_f1.config(state=tk.NORMAL)
        self.Man_Order_Form_Codeinput_f1.config(state=tk.NORMAL)
        self.Man_DueDay_Button_f1.config(state=tk.NORMAL)
        self.modify2()



# 테스트용 코드
if __name__ == "__main__":
    # dbm = dbManager.DBManager(host="localhost", user="root", password="0000", port=3306)
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    fr = Manufacturing_Order(r)
    fr.place(x=300, y=130)
    r.mainloop()
