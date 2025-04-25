import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import pymysql
import color
import tablewidget
import tkcalendar
import json

class BOM(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        self.dict = {}
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
        self.frame_x = [10, 100, 250]
        self.frame_y = [10, 40, 70, 100, 130, 160, 190]

        # (frame 3, 4가 하나라면 아래와 같이 사용)

        # frame1에 들어갈 것들
        # data_f1 = [[f"Data {r + 1}{chr(65 + c)}" for c in range(6)] for r in range(3)]

        self.data_f1 = [[None,None,None,None,None,None],[None,None,None,None,None,None]]
        # self.data_f1 = self.frame1_list()
        self.app1 = tablewidget.TableWidget(self.frame1,
                                       data=self.data_f1,
                                       cols= 6,
                                       col_name=["BOM 코드", "원자재 코드", "원자재 이름", "필요 수량", "단위", "매입 가격" ],
                                       # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                       col_width=[140, 140, 140, 140, 140, 140, 140],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                       width=950,  # 테이블 그려질 너비
                                       height=350,
                                       padding=10)  # 테이블 그려질 높이

        self.app1.grid(row=0, column=0)

        self.app3 = tablewidget.TableWidget(self.frame3,
                                            data=[["None",None,None,None,None,None]],
                                            cols=6,
                                            col_name=["BOM 코드", "작업표준서 코드", "생성 날짜", "발주서 코드", "완제품 코드", "완제품 이름"],
                                            # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                            col_width=[190, 190, 190, 190, 190, 190, 190],
                                            # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                            width=1300,  # 테이블 그려질 너비
                                            height=350,
                                            padding=10)  # 테이블 그려질 높이

        self.app3.grid(row=0, column=0)

        # frame2에 들어갈 것들
        self.BOM_Code = ttk.Label(self.frame2,text='BOM 코드',width=14)
        self.BOM_Code.place(x = self.frame_x[0], y = self.frame_y[0])
        self.BOM_Code_input = ttk.Entry(self.frame2,width=15)
        self.BOM_Code_input.place(x = self.frame_x[1], y = self.frame_y[0])
        self.BOM_Refer_Button =ttk.Button(self.frame2,text='조회',command=self.refer)
        self.BOM_Refer_Button.place(x = self.frame_x[2], y = self.frame_y[0])

        self.SOP_Code = ttk.Label(self.frame2,text='작업표준서 코드',width=14)
        self.SOP_Code.place(x=self.frame_x[0], y=self.frame_y[1])
        self.SOP_Code_input = ttk.Entry(self.frame2,width=15)
        self.SOP_Code_input.place(x=self.frame_x[1], y=self.frame_y[1])
        self.BOM_Create_Button = ttk.Button(self.frame2,text='생성',command=self.BOM_Create)
        self.BOM_Create_Button.place(x = self.frame_x[2], y = self.frame_y[1])

        self.BOM_Written_Date = ttk.Label(self.frame2, text='생성 날짜',width=14)
        self.BOM_Written_Date.place(x=self.frame_x[0], y=self.frame_y[2])
        self.BOM_Written_Date_input = ttk.Entry(self.frame2,width=15)
        self.BOM_Written_Date_input.place(x=self.frame_x[1], y=self.frame_y[2])
        self.BOM_Edit_Button = ttk.Button(self.frame2,text='수정',command=self.modify)
        self.BOM_Edit_Button.place(x = self.frame_x[2],y=self.frame_y[2])
        self.BOM_Written_Date_input.bind("<Button-1>", self.on_date_select)


        self.BOM_Order_Form_Code = ttk.Label(self.frame2,text='발주서 코드',width=14)
        self.BOM_Order_Form_Code.place(x = self.frame_x[0],y = self.frame_y[3])
        self.BOM_Order_Form_Code_input = ttk.Entry(self.frame2,width=15)
        self.BOM_Order_Form_Code_input.place(x = self.frame_x[1],y = self.frame_y[3])
        self.BOM_Save_Button = ttk.Button(self.frame2,text='저장',command=self.Save)
        self.BOM_Save_Button.place(x = self.frame_x[2], y = self.frame_y[3])

        self.BOM_Product_Code = ttk.Label(self.frame2,text="완제품 코드",width=14)
        self.BOM_Product_Code.place(x = self.frame_x[0],y = self.frame_y[4])
        self.BOM_Product_Code_input = ttk.Entry(self.frame2,width=15)
        self.BOM_Product_Code_input.place(x = self.frame_x[1],y = self.frame_y[4])
        self.BOM_Delete_Button = ttk.Button(self.frame2,text='상세',command=self.getdata)
        self.BOM_Delete_Button.place(x = self.frame_x[2], y = self.frame_y[4])

        self.BOM_Product_Name = ttk.Label(self.frame2,text='완제품 이름',width=14)
        self.BOM_Product_Name.place(x = self.frame_x[0],y = self.frame_y[5])
        self.BOM_Product_Name_input = ttk.Entry(self.frame2,width=15)
        self.BOM_Product_Name_input.place(x=self.frame_x[1], y=self.frame_y[5])

        self.ORD_Button = ttk.Button(self.frame2, text='발주서 상세', command=self.a)
        self.ORD_Button.place(x=self.frame_x[2], y=self.frame_y[5])

        self.list_f1 = []
        self.list_f3 = []
        self.modify_list_f1 = []
        self.modify_list_f3 = []
        self.get_frame3 =[]


        # frame3에 들어갈 것들
        self.data = None
        self.app3.bind("<Double-Button-1>", self.getdata())
        self.get_frame_list()


        # r.bind("<F2>", lambda e: self.test())
        # r.bind("<F3>", lambda e: print(self.app1.selected_row))

    def getdata(self): #frame1의 조회 (바인드)
        self.data = self.app3.data[self.app3.selected_row]['data'][0]

        keys = ['BOM 코드']  # db의 문서테이블 이름
        values = [self.data]

        d = dict(zip(keys, values))

        send_d = {
            "code": 20206,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

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
        self.modify_list_f1 =[]
        for i in self.app1.changed['updated']:
            f1_changed_row.append(i)
            print('changed_row', f1_changed_row)
            self.modify_list_f1.append(self.app1.changed['updated'][i])
        print("modify_list_f1", self.modify_list_f1)

        keys = ['modify_lsit', 'change_row','list_f1']  # db의 문서테이블 이름
        values = [self.modify_list_f1, f1_changed_row, self.list_f1]
        # keys = ['modify_list1','modify_list2','modify_list3','modify_list4','modify_list5','modify_list6', 'change_row', 'list_f1_1', 'list_f1_2', 'list_f1_3', 'list_f1_4', 'list_f1_5', 'list_f1_6']  # db의 문서테이블 이름
        # values = [self.modify_list_f1[0],self.modify_list_f1[1],self.modify_list_f1[2],self.modify_list_f1[3],self.modify_list_f1[4],self.modify_list_f1[5], f1_changed_row[0], self.list_f1[0],self.list_f1[1],self.list_f1[2],self.list_f1[3],self.list_f1[4],self.list_f1[5]]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20205,########################################################
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

    def modify(self):
        changed_row = []
        self.modify_list_f3 =[]
        for i in self.app3.changed['updated']:
            changed_row.append(i)
            print('changed_row',changed_row)
            self.modify_list_f3.append(self.app3.changed['updated'][i])
        print("modify_list_f3",self.modify_list_f3)
        print('self.app3.changed',self.app3.changed)

        keys = ['수정리스트', '수정 행', '수정전 리스트']  # db의 문서테이블 이름
        values = [self.modify_list_f3, changed_row, self.list_f3]
        d = dict(zip(keys, values))

        send_d = {
            "code": 20203,  ########################################################
            "args": d
        }

        print("d", send_d)
        print('values[0] : ',values[0])

        self.root.send_(json.dumps(send_d, ensure_ascii=False))
        self.f1_changed()


        # for i in [self.modify_list_f3]:
        #     for j in i:
        #         print(j)
        #         for k in changed_row:
        #             (f"update sop set sop_code = '{j[0]}' ,bom_code = '{j[1]}',order_code = '{j[2]}',material_code = '{j[3]}',material_name = '{j[4]}',writter = '{j[5]}',written_date = '{j[6]}' where sop_code = '{self.list_f3[k][0]}' " )

        # self.f1_changed()


    def on_date_select(self, event):  # 캘린더 생성
        self.cal = tkcalendar.Calendar(self.frame2, firstweekday="sunday", locale="ko_KR", showweeknumbers=False)
        self.cal.place(x=60, y=20)
        self.cal.bind("<<CalendarSelected>>", self.select_date)

    def select_date(self, event):  # 선택된 날짜를 엔트리에 입력
        self.BOM_Written_Date_input.delete(0, tk.END)
        self.BOM_Written_Date_input.insert(0, self.cal.selection_get())
        self.cal.destroy()  # 캘린더 닫기

    def after_init(self):
        self.refer()

    def a(self):
        for i in self.app3.changed['added']:
            if self.app3.changed['added'][i][3] != '':
                ordcode=self.app3.changed['added'][i][3]
                # print('자재코드',ordcode)

        if ordcode!='':
            keys = ['작업표준서 코드']
            values = [ordcode]
            d = dict(zip(keys, values))

            send_d = {
                "code": 20207,
                "args": {'order_code':ordcode}
            }

            print('send_d',send_d)
            self.root.send_(json.dumps(send_d, ensure_ascii=False))



    def recv(self,**kwargs):
        print("code :",kwargs.get("code"))
        print("sign :", kwargs.get("sign"))
        print("data :", kwargs.get("data"))

        if kwargs.get("sign") ==1 and kwargs.get("code") == 20201:# 조회버툰 가져온걸 다시 그림
            print(kwargs.get("data"))
            self.app3 = tablewidget.TableWidget(self.frame3,
                                                data=kwargs.get("data"),
                                                cols=6,
                                                col_name=["BOM 코드", "작업표준서 코드", "생성 날짜", "발주서 코드", "완제품 코드", "완제품 이름"],
                                                # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                                col_width=[190, 190, 190, 190, 190, 190, 190],
                                                # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                                width=1300,  # 테이블 그려질 너비
                                                height=350,
                                                padding=10)  # 테이블 그려질 높이

            self.app3.grid(row=0, column=0)
            self.get_frame3 = kwargs.get("data")

        if kwargs.get("sign") == 1 and kwargs.get("code") == 20206:
            self.app1 = tablewidget.TableWidget(self.frame1,
                                                data=kwargs.get("data"),
                                                cols=6,
                                                col_name=["BOM 코드", "원자재 코드", "원자재 이름", "필요 수량", "단위", "매입 가격"],
                                                # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                                col_width=[140, 140, 140, 140, 140, 140, 140],
                                                # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                                width=950,  # 테이블 그려질 너비
                                                height=350,
                                                padding=10)  # 테이블 그려질 높이
            self.app1.grid(row=0, column=0)
            self.app3.bind("<Double-Button-1>", lambda e: self.getdata())
            self.list_f1 = kwargs.get("data")

        if kwargs.get("sign") == 1 and kwargs.get("code") == 20207:
            list = ['', '','' ,kwargs.get("data")[0][0], kwargs.get("data")[0][1], kwargs.get("data")[0][2]]
            self.get_frame3.append(list)
            print('재조회', self.get_frame3)

            self.app3 = tablewidget.TableWidget(self.frame3,
                                                data=self.get_frame3,
                                                cols=6,
                                                col_name=["BOM 코드", "작업표준서 코드", "생성 날짜", "발주서 코드", "완제품 코드", "완제품 이름"],
                                                # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                                col_width=[190, 190, 190, 190, 190, 190, 190],
                                                # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                                width=1300,  # 테이블 그려질 너비
                                                height=350,
                                                padding=10)  # 테이블 그려질 높이
            self.app3.grid(row=0, column=0)



    def refer(self):
        def getBom():
            return self.BOM_Code_input.get()
        def getsop():
            return self.SOP_Code_input.get()
        def getDate():
            return self.BOM_Written_Date_input.get()
        def getOrder():
            return self.BOM_Order_Form_Code_input.get()
        def getProductName():
            return self.BOM_Product_Name_input.get()
        def getProductCode():
            return self.BOM_Product_Code_input.get()

        keys = ['BOM코드', '작업표준서 코드', '생성 날짜', '발주서 코드','완제품 코드','완제품 이름']
        values = [getBom(), getsop(), getDate(), getOrder(),getProductCode(),getProductName()]
        d = dict(zip(keys,values))
        print(d.values())

        send_d = {
            "code": 20201,
            "args": d
        }

        print("d", send_d)

        self.root.send_(json.dumps(send_d, ensure_ascii=False))

    def BOM_Create(self): #frame3의 신규 버튼
        addList = []

        for i in self.app3.changed['added']:
            if self.app3.changed['added'][i][0] != '':
                addList.append(self.app3.changed['added'][i])
        for j in range(len(addList)):  # 0,1
            print(addList)
            keys = ['BOM코드', '작업표준서 코드', '생성 날짜', '발주서 코드', '자재 코드', '자재 이름']
            values = [addList[j][0], addList[j][1], addList[j][2], addList[j][3], addList[j][4], addList[j][5]]
            d = dict(zip(keys, values))
            print(d.values())
            send_d = {
                "code": 20202,
                "args": d
            }

            print("d", send_d)

            self.root.send_(json.dumps(send_d, ensure_ascii=False))

    def Save(self): #frame1 저장
        addList = []
        for i in self.app1.changed['added']:
            if self.app1.changed['added'][i][0] != '':
                addList.append(self.app1.changed['added'][i])
        for j in range(len(addList)):  # 0,1
            keys = ['BOM 코드','원자재 코드', '원자재 이름', '필요 수량', '단위', '매입 가격']  # db의 문서테이블 이름
            values = [addList[j][0], addList[j][1], addList[j][2], addList[j][3],addList[j][4],addList[j][5]]
            d = dict(zip(keys, values))

            send_d = {
                "code": 20204,
                "args": d
            }

            print("d", send_d)

            self.root.send_(json.dumps(send_d, ensure_ascii=False))
        self.modify()

    def test(self):
        print(f"changed {self.app1.changed}")  # 원본 대비 변경된 데이터
        return self.app1.changed

    # @staticmethod
    # @MsgProcessor
    # def f20201(**kwargs):
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"SELECT * FROM bom where (bom_Code like '%%{valueList[0]}%%' and sop_code like '%%{valueList[1]}%%' and written_date like '%%{valueList[2]}%%' and order_code like '%%{valueList[3]}%%' and material_code like '%%{valueList[4]}%%' and material_name like '%%{valueList[5]}%%') "
    #
    #     result = dbm.query(query, [])
    #     d = [list(row) for row in result]
    #
    #     if result:
    #         return {"sign": 1, 'data': result}
    #     else:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20202(**kwargs):
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"insert into bom values('{valueList[0]}', '{valueList[1]}','{valueList[2]}','{valueList[3]}','{valueList[4]}','{valueList[5]}')"
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     else:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20203(**kwargs):  # 프레임3 수정
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #         # print(f'Index: {i}, Value: {value}
    #     for i in valueList[0]:
    #         # print('i :', i) #i : ['sop33', '', '수정', '', '', '', '']
    #         # print('i[0]',i[0])
    #         query = f"update bom set bom_code = '{i[0]}' ,sop_code = '{i[1]}',written_date = '{i[2]}',order_code = '{i[3]}',material_code = '{i[4]}',material_name = '{i[5]}' where bom_code = '{i[0]}' "  # valueList[2][k][0]
    #         result = dbm.query(query, [])
    #
    #         print("result", result)
    #
    #         if query:
    #             return {"sign": 1, 'data': result}
    #         elif not query:
    #             return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20204(**kwargs):  # frame3의 저장
    #     valueList = []
    #
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"insert into bom_f values('{valueList[0]}', '{valueList[1]}','{valueList[2]}','{valueList[3]}','{valueList[4]}','{valueList[5]}')"
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     else:
    #         return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20205(**kwargs):  # 프레임1 수정 #함수 추가#########
    #     valueList = []
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #         # print(f'Index: {i}, Value: {value}')
    #     # print('valueList[0]', valueList[1][0])
    #     # print('valueList[2][valueList[0]][0]', valueList[2][valueList[1][0]][0],)
    #     # print(valueList[2][valueList[1][0]][0], 0)
    #     # print(valueList[2][valueList[1][0]][1], 1)
    #     # print(valueList[2][valueList[1][0]][2], 2)
    #     # print(valueList[2][valueList[1][0]][3], 3)
    #     # print(valueList[2][valueList[1][0]][4], 4)
    #     # print(valueList[2][valueList[1][0]][5], 5)
    #
    #     # for i in valueList[0]:
    #     #     print('iiiiiiiii',i)
    #     #
    #     for i in valueList[0]:
    #         query = f"UPDATE bom_f SET bom_code = '{i[0]}' , material_code = '{i[1]}' , material_name = '{i[2]}' , quantity = '{i[3]}' , unit = '{i[4]}' , purchase_price = '{i[5]}' WHERE (bom_code = '{valueList[2][valueList[1][0]][0]}' AND material_code = '{valueList[2][valueList[1][0]][1]}' AND material_name = '{valueList[2][valueList[1][0]][2]}' AND quantity = '{valueList[2][valueList[1][0]][3]}' AND unit = '{valueList[2][valueList[1][0]][4]}' )"  # valueList[2][k][0]
    #         # query = f"select * from bom_f"
    #         # query = f"UPDATE bom_f SET bom_code = '{valueList[0]}' , material_code = '{valueList[1]}' , material_name = '{valueList[2]}' , quantity = '{valueList[3]}' , unit = '{valueList[4]}' , purchase_price = '{valueList[5]}' WHERE (bom_code = '{valueList[7]}' AND material_code = '{valueList[8]}' AND material_name = '{valueList[9]}' AND quantity = '{valueList[10]}' AND unit = '{valueList[11]}' AND purchase_price = '{valueList[12]}')"  # valueList[2][k][0]
    #
    #         result = dbm.query(query, [])
    #         print("result", result)
    #
    #         if query:
    #             return {"sign": 1, 'data': result}
    #         elif not query:
    #             return {"sign": 0, 'data': None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20206(**kwargs):
    #     valueList = []
    #
    #     for i, value in enumerate(kwargs.values()):
    #         valueList.append(value)
    #     query = f"SELECT * FROM bom_f WHERE bom_code = '{valueList[0]}' "
    #     # query = f"SELECT * FROM bom_f"
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     else:
    #         return {"sign": 0, 'data': None}

    # @staticmethod
    # @MsgProcessor
    # def f20207(**kwargs):
    #     valueList = []
    #
    #     for i, value in enumerate(kwargs.values()):
    #         print(i, value)
    #         valueList.append(value)
    #     query = f"SELECT order_code, product_code, product_name FROM order_form WHERE order_code = '{valueList[0]}' "
    #     result = dbm.query(query, [])
    #     print("result", result)
    #     if query:
    #         return {"sign": 1, 'data': result}
    #     elif not query:
    #         return {"sign": 0, 'data': None}



# 테스트용 코드
if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    fr = BOM(r)
    fr.place(x=300, y=130)
    r.mainloop()

