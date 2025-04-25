import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
# import dbManager
import naviframe
from tablewidget import TableWidget
from color import Color
import datetime
import json
import traceback



# receiving_columns = {
#     "입고 번호": "receiving_code",
#     "생산지시서 코드": "production_order",
#     "거래처 코드": "client_code",
#     "거래처 명": "client_name",
#     "수량": "quantity",
#     "단위": "unit",
#     "자재 코드": "material_code",
#     "자재 명": "material_name",
#     "발주 코드": "order_code",
#     "날짜": "date",
#     "입고 창고": "receiving_warehouse",
#     "입고 담당자": "receiving_responsibility",
#     "입고 구분": "receiving_classification"
# }

# dbm = dbManager.DBManager(host,user,password,port)

class Receiving(tk.Frame):
    # dbm = dbManager.DBManager(host,user,password,port)

    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        self.name = None

        self.receiving_columns = {
            "입고 번호": "receiving_code",
            "거래처 코드": "client_code",
            "거래처 명": "client_name",
            "수량": "quantity",
            "단위": "unit",
            "자재 코드": "material_code",
            "자재 명": "material_name",
            "발주 코드": "order_code",
            "가격" : "price",
            "창고 코드": "plant_code",
            "제품 상태" : "state",
            "입고 담당자": "receiving_responsibility",
            "입고 구분": "receiving_classification",
            "구매 오더 코드" : "purchase_order_code"
        }

        self.frame1 = tk.Frame(self, width=950, height=350)  # 왼쪽 위 구역
        self.frame2 = tk.Frame(self, width=350, height=350)  # 오른쪽 위 구역
        self.frame3 = tk.Frame(self, width=1300, height=350)  # 아래 구역

        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.grid_propagate(False)
        self.frame3.pack_propagate(False)

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0, columnspan=2)

        self.main_table_columns = None #테이블 이름에 맞는 컬럼명 추출
        self.mo_column = None
        self.purchasing_column = None
        self.main_datalist = None #테이블 이름에 맞는 데이터 추출
        self.mo_datalist = None
        self.purchasing_datalist = None

        self.sub_table_flag = True

        self.main_data = []
        self.sub_data = []
        self.save_list = []

        self.material_columns = []
        self.material_data = []

        self.main_table = None
        self.sub_table = None

        self.mo_column = []
        self.purchasing_column = []

        self.tlabel1 = ttk.Label(self.frame2, text="구매 오더 코드", width=14)
        self.tentry1 = ttk.Entry(self.frame2, textvariable=self.receiving_columns.get("구매 오더 코드"), width=18)
        self.tlabel2 = ttk.Label(self.frame2, text="제품 상태", width=14)
        self.tentry2 = ttk.Entry(self.frame2, textvariable=self.receiving_columns.get("제품 상태"), width=18)
        self.tlabel3 = ttk.Label(self.frame2, text="입고 구분", width=14)
        self.tentry3 = ttk.Entry(self.frame2, textvariable=self.receiving_columns.get("입고 구분"), width=18)
        self.tlabel4 = ttk.Label(self.frame2, text="자재 코드", width=14)
        self.tentry4 = ttk.Entry(self.frame2, textvariable=self.receiving_columns.get("자재 코드"), width=18)
        self.tlabel5 = ttk.Label(self.frame2, text="입고 번호", width=14)
        self.tentry5 = ttk.Entry(self.frame2, textvariable=self.receiving_columns.get("입고 번호"), width=18)
        self.tlabel6 = ttk.Label(self.frame2, text="거래처 코드", width=14)
        self.tentry6 = ttk.Entry(self.frame2, textvariable=self.receiving_columns.get("거래처 코드"), width=18)

        self.tlabel1.grid(row=0, column=0, padx=5, pady=10)
        self.tentry1.grid(row=0, column=1, padx=5, pady=10)
        self.tlabel2.grid(row=1, column=0, padx=5, pady=10)
        self.tentry2.grid(row=1, column=1, padx=5, pady=10)
        self.tlabel3.grid(row=2, column=0, padx=5, pady=10)
        self.tentry3.grid(row=2, column=1, padx=5, pady=10)
        self.tlabel4.grid(row=3, column=0, padx=5, pady=10)
        self.tentry4.grid(row=3, column=1, padx=5, pady=10)
        self.tlabel5.grid(row=4, column=0, padx=5, pady=10)
        self.tentry5.grid(row=4, column=1, padx=5, pady=10)
        self.tlabel6.grid(row=5, column=0, padx=5, pady=10)
        self.tentry6.grid(row=5, column=1, padx=5, pady=10)

        self.test_button = ttk.Button(self.frame2, text= "조회", command=self.check_data)
        self.test_button.grid(row=0, column=2,pady=5)
        self.test_button2 = ttk.Button(self.frame2, text= "입고", command=self.receiving_process)
        self.test_button2.grid(row=1, column=2,pady=5)
        # self.test_button3 = ttk.Button(self.frame2, text= "생성")
        # self.test_button3.grid(row=2, column=2,pady=5)
        self.test_button3 = ttk.Button(self.frame2, text= "저장", command=self.save_to_db)
        self.test_button3.grid(row=2, column=2,pady=5)
        self.test_button4 = ttk.Button(self.frame2, text= "수정", command=self.update_data)
        self.test_button4.grid(row=3, column=2,pady=5)

        self.test_button5 = ttk.Button(self.frame2, text= "구매오더", command=self.purchase_table_load)
        self.test_button5.grid(row=4, column=2,pady=5)

        self.test_button6 = ttk.Button(self.frame2, text= "생산지시서", command=self.mo_table_load)
        self.test_button6.grid(row=5, column=2,pady=5)

        self.test_button7 = ttk.Button(self.frame2, text= "사용법", command=self.show_message)
        self.test_button7.grid(row=6, column=2,pady=5)

    def show_message(self):
        tk.messagebox.showinfo("사용법","""
        1. 구매오더코드 엔트리 값 조회시 서브테이블(왼쪽 상단 테이블)의 데이터가 생산지시서라면 메인 테이블(아래 테이블만 새로고침)
        1-1. 서브테이블의 데이터가 구매오더라면 po_num 컬럼에 해당하는 값 입력시 해당 데이터만 출력\n
        2. 서브 테이블에서 원하는 값 체크 후 입고 버튼 누르면 아래 메인 테이블에 값 이동(구매오더, 생산지시서 상관 없음)\n
        3. 저장버튼을 누르면 입고 버튼으로 메인 테이블에 추가된 데이터 행 DB에 저장\n 
        4. 아래 메인 테이블에서 엔터 후 값 수정 뒤에 수정 버튼을 누르면 수정 된 값 DB반영\n
        5. 구매오더, 생산지시서 버튼은 서브테이블의 데이터를 각각의 데이터로 맞춰 다시 그리고 새로고침 하는 역할
        """)

    def purchase_table_load(self):
        self.get_purchasing_columns("purchasing_order")
        self.get_purchasing_all_data("purchasing_order")

    def mo_table_load(self):
        self.get_mo_columns("mo")
        self.get_mo_all_data("mo")

    def after_init(self):
        self.get_main_columns("receiving")#테이블 이름에 맞는 컬럼명 추출
        self.get_mo_columns("mo")
        self.get_main_all_data("receiving") #테이블 이름에 맞는 데이터 추출
        self.get_mo_all_data("mo")
        self.send_({"code": 20813, "args": {}})
        self.send_({"code": 20814, "args": {}})
        pass

    def onkey(self):

        # 테이블에 들어갈 데이터 // db에서 데이터를 불러와 [[],[],[]] 이중배열로 가공해서 넣기
        data = [['00001', '(주)이상한과자가게전천당', '123-12-45678', '성진하'],
                ['00002', '이상한과자가게전천당', '123-12-45678', '성진하'],
                ['00003', '(주)아크라시아사탕가게', '457-34-44587', '박미나니'],
                ['00025', '엘가시아과자가게', '942-34-47898', '김니나브'],
                ['00284', '신창섭의극극극성비가게', '766-56-10957', '신창섭'],
                ['09876', '만능고물상', '186-78-05957', '몽땅따']
                ]

        # 테이블 위젯을 만들때 필요한 정보
        naviData = {"검색유형": ['거래처코드', '거래처명'],  # 검색기준 설정 []안의 내용만 바꾸면 됨, 단 col_name에 있는 것이어야함.
                    "data": data,  # 위에서 불러온 데이터
                    "col_name": ['거래처코드', '거래처명', '사업자등록번호', '대표자 성명'],  # 컬럼 이름
                    "col_width": [80, 220, 125, 101],  # 컬럼별 사이즈
                    "col_align": ['center', 'left', 'center', 'center']  # 컬럼별 정렬 기준
                    }

        # 생성자
        fr = naviframe.NaviFrame(self.root,  # 최상위 프레임
                                 naviData,  # 위에서 작성한 테이블 위젯 생성시에 필요한 정보
                                 {
                                     # 1:1 대응 // self.bkClientEnt 위치에는 '거래처코드' 값이 들어가고, self.bkClientContent 위치에는 '거래처명'이 들어감
                                     "entry": [self.tentry2],  # 테이블 행 선택시 정보가 들어갈 엔트리박스 변수명
                                     "key": ["거래처코드"]},  # 선택한 테이블 행의 데이터중 얻을 값 ( 컬럼 이름 적으면 됨 )
                                 x=100,  # 코드 검색창 뜰 위치 좌표 X값 // 미입력시 디폴트값 x=700
                                 y=180,  # 코드 검색창 뜰 위치 좌표 Y값 // 미입력시 디폴트값 y=180
                                 width=602)  # 코드 검색창 가로사이즈 ( 세로사이즈는 고정임 ) // 미입력시 디폴트값 width=602
        # 배치
        fr.place(x=500, y=300)

    def check_data(self): #데이터 조회 버튼
        if self.tentry1.get() or self.tentry2.get() or self.tentry3.get() or self.tentry4.get() or self.tentry5.get() or self.tentry6.get():
            if self.tentry1.get():
                print("1번")
                self.sub_table.draw_table()
                target = self.tentry1.get()
                self.tentry1.delete(0, tk.END)
                if self.sub_table_flag:
                    pass
                else:
                    send_dict = {"code": 20810, "args": {"po_num": target}}
                    self.send_(send_dict)


            elif self.tentry2.get():
                print("2번")
                self.main_table.draw_table()
                target = self.tentry2.get()
                self.tentry2.delete(0, tk.END)
                if self.sub_table_flag:
                    send_dict = {"code": 20809, "args": {self.tentry2.cget("textvariable"): target}}
                    self.send_(send_dict)
                else:
                    pass

            elif self.tentry3.get():
                print("3번")
                self.main_table.draw_table()
                target = self.tentry3.get()
                self.tentry3.delete(0, tk.END)
                send_dict = {"code": 20801, "args":{self.tentry3.cget("textvariable"): target}}
                self.send_(send_dict)

            elif self.tentry4.get():
                print("4번")
                self.main_table.draw_table()
                target = self.tentry4.get()
                self.tentry4.delete(0, tk.END)
                send_dict = {"code": 20801, "args":{self.tentry4.cget("textvariable"): target}}
                self.send_(send_dict)

            elif self.tentry5.get():
                print("5번")
                self.main_table.draw_table()
                target = self.tentry5.get()
                self.tentry5.delete(0, tk.END)
                send_dict = {"code": 20801,"args":{self.tentry5.cget("textvariable"): target}}
                self.send_(send_dict)

            elif self.tentry6.get():
                print("6번")
                self.main_table.draw_table()
                target = self.tentry6.get()
                self.tentry6.delete(0, tk.END)
                send_dict = {"code": 20801,"args":{self.tentry6.cget("textvariable"): target}}
                self.send_(send_dict)
        else:
            self.main_table.draw_table()
            self.tentry2.delete(0, tk.END)
            send_dict = {"code": 20801, "args":{"0": 0}}
            self.send_(send_dict)
            print("선택값 없음")

    def get_main_all_data(self, tablename):
        send_dict={"code":20805,"args":{tablename:"*"}}
        self.send_(send_dict)

    def get_mo_all_data(self, tablename):
        send_dict={"code":20806,"args":{tablename:"*"}}
        self.send_(send_dict)

    def get_purchasing_all_data(self, tablename):
        send_dict={"code":20811,"args":{tablename:"*"}}
        self.send_(send_dict)

    def get_main_columns(self, tablename):
        send_dict = {"code": 20807, "args": {"tablename": tablename}}
        self.send_(send_dict)

    def get_mo_columns(self, tablename):
        send_dict = {"code": 20808, "args": {"tablename": tablename}}
        self.send_(send_dict)

    def get_purchasing_columns(self, tablename):
        send_dict = {"code": 20812, "args": {"tablename": tablename}}
        self.send_(send_dict)

    def reorder_columns(self, original_data, index):
        # 컬럼명 리스트 가져오기
        sub_columns = []
        main_columns = []

        if self.sub_table_flag == True: #True 일때 mo 테이블
            for r in range(len(self.mo_column)):
                for i in self.mo_column[r]:
                    sub_columns.append(i)
        elif self.sub_table_flag == False:
            for r in range(len(self.purchasing_column)):
                for i in self.purchasing_column[r]:
                    sub_columns.append(i)

        for r in range(len(self.main_table_columns)):
            for i in self.main_table_columns[r]:
                main_columns.append(i)

        for r in range(len(self.material_columns)):
            for i in self.material_columns[r]:
                sub_columns.append(i)

        for k in self.material_data[index]:
            original_data.append(k)

        print(original_data)

        # for i in original_data:
        #     print("prd찾는 for문 진입")
        #     if "PRD" in i:
        #         print("PRD찾기")

        column_mapping = {
            "order_code": "order_code",
            "quantity": "quantity",
            "unit": "unit",
            "material_code":"material_code",
            "mat_code":"material_code",
            "materialName":"material_name",
            "state":"receiving_classification",
            "measure":"unit",
            "vendor":"client_code",
            "po_num":"purchase_order_code",
            "sellingPrice": "price",
            "amount": "price",
            "correspondentCode": "client_code",
            "correspondentName": "client_name",
            "plant":"plant_code"
        }

        reordered_data = [0] * len(main_columns)

        for sub_col, main_col in column_mapping.items():
            if sub_col in sub_columns and main_col in main_columns:
                sub_idx = sub_columns.index(sub_col)  # mo에서의 인덱스
                main_idx = main_columns.index(main_col)
                reordered_data[main_idx] = original_data[sub_idx]  # 해당 위치에 값 삽입

        # now = datetime.datetime.now()
        # date_idx = main_columns.index("date")
        # reordered_data[date_idx] = now.strftime("%y-%m-%d")

        if self.sub_table_flag == False:
            recl_idx = main_columns.index("receiving_classification")
            reordered_data[recl_idx] = "원자재 입고"

        print("reorder_data",reordered_data[7])
        for i in self.material_data:
            if i[0] == reordered_data[7]:
                print(i)
                reordered_data[8] = i[1]
                print(reordered_data)

        reordered_data[9] = 'e001'
        sub_columns = []

        return reordered_data

    def receiving_process(self):
        for i in self.sub_table.data.keys():
            if self.sub_table.data[i]['checked']:  # 체크된 행만 이동
                original_data = self.sub_table.data[i]['data']  # mo 테이블 데이터
                print("체크된 데이터",self.sub_table.data[i]['checked'])
                last_shipment_code = self.main_data[-1][0]  # 기본값
                if self.main_data:  # main_data에 기존 데이터가 있을 경우
                    last_shipment_code = self.main_data[-1][0]  # 마지막 출고번호 가져오기

                last_number = int(last_shipment_code[3:])  # 'SHP' 이후 숫자만 추출
                new_shipment_code = f"REC{last_number + 1:03}"  # 숫자 3자리 형식 유지

                reordered_data = self.reorder_columns(original_data, i)
                reordered_data[0] = new_shipment_code

                print(reordered_data)
                self.main_data.append(reordered_data)
                self.save_list.append(reordered_data)
                self.main_table.from_data(data=self.main_data, col_name=self.main_table_columns,
                                          col_width=[130 for _ in range(len(self.main_table_columns))])
                self.main_table.draw_table()

    def check_main_data(self):
        print(f"data: {self.main_table.data}")  # 저장된 데이터
        print(f"rows cols: {self.main_table.rows} {self.main_table.cols}")  # 행 열 개수
        print(f"selected: {self.main_table.selected_row} {self.main_table.selected_col}")  # 선택된 행 열 index
        print(f"changed {self.main_table.changed}")

    def check_sub_data(self):
        print(f"data: {self.sub_table.data}")  # 저장된 데이터
        print(f"rows cols: {self.sub_table.rows} {self.sub_table.cols}")  # 행 열 개수
        print(f"selected: {self.sub_table.selected_row} {self.sub_table.selected_col}")  # 선택된 행 열 index
        print(f"changed {self.sub_table.changed}")  # 원본 대비 변경된 데이터
        print(self.save_list)

    def save_to_db(self):
        if self.save_list is None:
            pass
        save_dict = {}
        main_columns = []
        for r in range(len(self.main_table_columns)):
            for i in self.main_table_columns[r]:
                main_columns.append(i)

        for r in range(len(self.save_list)):
            for i,j in zip(main_columns,self.save_list[r]):
                save_dict[i] = j

        print("저장될 데이터",self.save_list)
        print("보낼 데이터",save_dict)
        print("받게될데이터",save_dict.values())
        send_dict = {"code":20803,"args":save_dict}
        self.save_list = []
        self.send_(send_dict)

    def update_data(self):
        column_index=[]
        change_data = []
        standard_data = []
        key_name = "change_data"
        send_data = {}

        for i in self.main_table.data.keys():
            for j in self.main_table.changed['updated'].keys():
                if i == j:
                    for k,m in zip(self.main_table.data[i]['data'],self.temp_data[i]):
                        if k != m:
                            column_index.append(self.main_table_columns[self.main_table.data[i]['data'].index(k)])
                            if self.main_table_columns[self.main_table.data[i]['data'].index(k)][0] == "plant_code":
                                temp = self.main_table.data[i]['data'][-3]
                                rec = self.main_table.data[i]['data'][0]

                                self.send_({"code":20815,"args":{temp: k}})

                                self.send_({"code":20816,"args":{rec: k}})

                                return
                            send_data[key_name+str(i)] = self.main_table.data[i]['data'][0],self.main_table_columns[self.main_table.data[i]['data'].index(k)][0],k
                            standard_data.append(self.main_table.data[i]['data'][0])
                            change_data.append(k)
                            i += 1
        # print(self.main_table_columns[self.main_table.data[i]['data'].index(k)])
        send_dict = {"code": 20804, "args": send_data}
        self.send_(send_dict)

    def send_(self,dict):
        # self.send_test(json.dumps(dict, ensure_ascii=False))
        self.root.send_(json.dumps(dict, ensure_ascii=False))

    def create_main_table(self):
        if self.main_datalist is not None and self.main_table_columns is not None:
            self.main_data = [[f"{c}" for c in self.main_datalist[r]] for r in range(len(self.main_datalist))]
            self.temp_data = self.main_data

            self.main_table = TableWidget(self.frame3,
                                          data=self.main_data,
                                          col_name=self.main_table_columns,
                                          col_width=[130 for _ in range(len(self.main_table_columns))],
                                          # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                          width=1300,
                                          height=350,
                                          padding=10)
            self.main_table.grid(row=0, column=0, columnspan=2, sticky="nsew")

            # self.main_scrollbar = ttk.Scrollbar(self.frame3, orient="horizontal", command=self.main_table.canvas.xview)
            # self.main_scrollbar.pack(side="bottom", fill="x")
            # self.main_table.canvas.configure(xscrollcommand=self.main_scrollbar.set)

    def create_sub_table(self):
        if self.mo_datalist is not None and self.mo_column is not None:
            if self.sub_table is None:
                self.sub_data = [[f"{c}" for c in self.mo_datalist[r]] for r in range(len(self. mo_datalist))]

                self.sub_table = TableWidget(self.frame1,
                                             data=self.sub_data,
                                             col_name=self.mo_column,
                                             col_width=[130 for _ in range(len(self.mo_column))],
                                             width=950,
                                             height=350,
                                             padding=10)
                self.sub_table.grid(row=0, column=0, columnspan=2, sticky="nsew")

                # self.sub_scrollbar = ttk.Scrollbar(self.frame1, orient="horizontal", command=self.sub_table.canvas.xview)
                # self.sub_scrollbar.pack(side="bottom", fill="x")
                # self.sub_table.canvas.configure(xscrollcommand=self.sub_scrollbar.set)
            else:
                print("Updating existing sub_table with new data...")  # 디버깅 로그 추가
                print("New Data:", self.sub_data)  # 데이터 확인
                print("New Columns:", self.mo_column)
                self.sub_data = [[f"{c}" for c in self.mo_datalist[r]] for r in range(len(self.mo_datalist))]
                self.sub_table.from_data(data=self.sub_data, col_name=self.mo_column,
                                         col_width=[130 for _ in range(len(self.mo_column))])
                self.sub_table.draw_table()

    def recv(self, **kwargs):
        code = kwargs.get("code")
        sign = kwargs.get("sign")
        data = kwargs.get("data")
        print("recv", kwargs)
        if sign == 1:
            if code == 20801:
                self.main_table.draw_table()
                self.main_datalist = data
                self.main_data = [[f"{c}" for c in self.main_datalist[r]] for r in range(len(self.main_datalist))]
                self.main_table.from_data(data=self.main_data, col_name=self.main_table_columns,
                                          col_width=[130 for _ in range(len(self.main_table_columns))])
                self.main_table.draw_table()

            elif code == 20802:
                pass

            elif code == 20803:
                pass

            elif code == 20804:
                pass

            elif code == 20805:
                self.main_datalist = data
                self.create_main_table()


            elif code == 20806:
                # self.sub_table.draw_table()
                self.mo_datalist = data
                self.sub_table_flag = True
                self.create_sub_table()


            elif code == 20807:
                self.main_table_columns = data
                self.create_main_table()

            elif code == 20808:
                self.mo_column = data
                self.get_mo_all_data("mo")
                # self.mo_column = data
                # self.create_sub_table()

            elif code == 20809:
                self.sub_table.draw_table()
                self.mo_datalist = data
                self.sub_table_flag = True
                self.sub_data = [[f"{c}" for c in self.mo_datalist[r]] for r in range(len(self.mo_datalist))]
                self.sub_table.from_data(data=self.sub_data, col_name=self.mo_column,
                                         col_width=[130 for _ in range(len(self.mo_column))])  # 데이터 갱신
                self.sub_table.draw_table()

            elif code == 20810:
                self.purchasing_datalist = data
                self.sub_table_flag = False
                self.sub_data = [[f"{c}" for c in self.purchasing_datalist[r]] for r in range(len(self.purchasing_datalist))]
                self.sub_table.from_data(data=self.sub_data, col_name=self.purchasing_column,
                                         col_width=[130 for _ in range(len(self.purchasing_column))])  # 데이터 갱신
                self.sub_table.draw_table()

            elif code == 20811:
                self.purchasing_datalist = data
                self.sub_table_flag = False
                self.sub_data = [[f"{c}" for c in self.purchasing_datalist[r]] for r in range(len(self.purchasing_datalist))]
                self.sub_table.from_data(data=self.sub_data, col_name=self.purchasing_column,
                                         col_width=[130 for _ in range(len(self.purchasing_column))])  # 데이터 갱신
                self.sub_table.draw_table()

            elif code == 20812:
                self.purchasing_column = data

            elif code == 20813:
                self.material_columns = data
                print("자재테이블 컬럼 가져오기",code,self.material_columns)

            elif code == 20814:
                self.material_data = data
                print("자재테이블 전체 데이터 가져오기", code, self.material_data)

            elif code == 20815:
                pass

            elif code == 20816:
                pass

    # @staticmethod
    # def f20801(**kwargs): #발주번호 외 나머지 조회시
    #     result_dict = {}
    #     data_dict= kwargs
    #
    #     for key, value in data_dict.items():
    #         if key == "0" or value == 0:
    #             result = dbm.query(f"SELECT * FROM receiving;")
    #         else:
    #             result = dbm.query(f"SELECT * FROM receiving where {key} = '{value}';")
    #
    #     if result is not None:
    #         result_dict = {"sign": 1, "data": list(result)}
    #     else:
    #         result_dict = {"sign": 0, "data": None}
    #
    #     return result_dict
    #
    # @staticmethod
    # def f20803(**kwargs): #저장시 값 db 추가
    #     save_dict = kwargs
    #     data_list = list(save_dict.values())
    #
    #     insert_query = """
    #         INSERT INTO receiving (receiving_code, order_code, receiving_classification, client_code, client_name, quantity, unit, material_code, material_name, receiving_responsibility, purchase_order_code, plant_code, price)
    #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    #     """
    #     result = dbm.transaction([(insert_query,tuple(data_list))])
    #
    #     if result is not None:
    #         return {"sign": 1, "data": result}
    #     else:
    #         return {"sign": 0, "data": None}
    #
    #
    # @staticmethod
    # def f20804(**kwargs): #값 수정
    #     send_data = kwargs
    #
    #     update_cases = {}
    #     receiving_codes = set()
    #
    #     for key, (receiving_code, column, value) in send_data.items():
    #         if column not in update_cases:
    #             update_cases[column] = []
    #         update_cases[column].append(f"WHEN receiving_code = '{receiving_code}' THEN '{value}'")
    #         receiving_codes.add(f"'{receiving_code}'")
    #
    #     update_sql = "UPDATE receiving SET \n"
    #     update_sql += ",\n".join([
    #         f"{column} = CASE \n" + "\n".join(conditions) + "\nEND"
    #         for column, conditions in update_cases.items()
    #     ])
    #     update_sql += f"\nWHERE receiving_code IN ({', '.join(receiving_codes)});"
    #     result = dbm.query(update_sql)
    #     print("결과",result)
    #     if result is not None:
    #         return {"sign": 1, "data": result}
    #     else:
    #         return {"sign": 0, "data": None}
    #
    # @staticmethod
    # def f20805(**kwargs): #전체 데이터 가져오기
    #     for key, value in kwargs.items():
    #         result = dbm.query(f"SELECT {value} FROM {key}")
    #
    #     if result is not None:
    #         return {"sign": 1, "data": result}
    #     else:
    #         return {"sign": 0, "data": None}
    #
    # @staticmethod
    # def f20806(**kwargs): # mo 서브테이블 전체 데이터 가져오기
    #     for key, value in kwargs.items():
    #         result = dbm.query(f"SELECT {value} FROM {key}")
    #
    #     if result is not None:
    #         return {"sign": 1, "data": result}
    #     else:
    #         return {"sign": 0, "data": None}
    #
    # @staticmethod
    # def f20807(**kwargs): #메인테이블 컬럼 가져오기
    #     result = dbm.query(
    #         f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = '{kwargs["tablename"]}' ORDER BY ORDINAL_POSITION;")
    #
    #     if result is not None:
    #         return {"sign": 1, "data": result}
    #     else:
    #         return {"sign": 0, "data": None}
    #
    # @staticmethod
    # def f20808(**kwargs): #mo 서브테이블 컬럼 가져오기
    #     result = dbm.query(
    #         f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = '{kwargs["tablename"]}' ORDER BY ORDINAL_POSITION;")
    #
    #     if result is not None:
    #         return {"code": 20808, "sign": 1, "data": result}
    #     else:
    #         return {"code": 20808, "sign": 0, "data": None}
    #
    # @staticmethod
    # def f20809(**kwargs): # mo 서브 테이블 조건 조회 데이터 가져오기
    #     result_dict = {}
    #     data_dict = kwargs
    #
    #     for key, value in data_dict.items():
    #         result = dbm.query(f"SELECT * FROM mo where {key} = '{value}';")
    #
    #     if result is not None:
    #         result_dict = {"sign": 1, "data": list(result)}
    #     else:
    #         result_dict = {"sign": 0, "data": None}
    #
    #     return result_dict
    #
    # @staticmethod
    # def f20810(**kwargs): # purchasing_order 서브 테이블 조건 조회 데이터 가져오기
    #     result_dict = {}
    #     data_dict = kwargs
    #
    #     for key, value in data_dict.items():
    #         result = dbm.query(f"SELECT * FROM purchasing_order where {key} = '{value}';")
    #
    #     for i, v in enumerate(result):
    #         for j, w in enumerate(v):
    #             if type(w) is datetime.datetime:
    #                 result[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")
    #
    #     if result is not None:
    #         result_dict = {"sign": 1, "data": list(result)}
    #     else:
    #         result_dict = {"sign": 0, "data": None}
    #
    #     return result_dict
    #
    #
    # @staticmethod
    # def f20811(**kwargs): # purchasing 서브테이블 전체 데이터 가져오기
    #     for key, value in kwargs.items():
    #         result = dbm.query(f"SELECT {value} FROM {key}")
    #
    #     for i, v in enumerate(result):
    #         for j, w in enumerate(v):
    #             if type(w) is datetime.datetime:
    #                 result[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")
    #
    #     if result is not None:
    #         return {"sign": 1, "data": result}
    #     else:
    #         return {"sign": 0, "data": None}
    #
    # @staticmethod
    # def f20812(**kwargs): #purchasing 서브테이블 컬럼 가져오기
    #     result = dbm.query(
    #         f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = '{kwargs["tablename"]}' ORDER BY ORDINAL_POSITION;")
    #
    #     for i, v in enumerate(result):
    #         for j, w in enumerate(v):
    #             if type(w) is datetime.datetime:
    #                 result[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")
    #
    #     if result is not None:
    #         return {"sign": 1, "data": result}
    #     else:
    #         return {"sign": 0, "data": None}

    # @staticmethod
    # @MsgProcessor
    # def f20813(**kwargs):  # materialtable 컬럼 가져오기
    #     result = dbm.query(
    #         f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'erp_db' AND TABLE_NAME  = 'materialtable' ORDER BY ORDINAL_POSITION;")
    #
    #     if result is not None:
    #         return {"sign": 1, "data": result}
    #     else:
    #         return {"sign": 0, "data": None}
    #
    # @staticmethod
    # @MsgProcessor
    # def f20814(**kwargs):  # materialtable 테이블 데이터 가져오기
    #     result = None
    #     result_list = []
    #
    #     result = dbm.query(f"SELECT * FROM materialtable")
    #
    #     for i in result:
    #         result_list.append(list(i))
    #
    #     for i, v in enumerate(result_list):
    #         for j, w in enumerate(v):
    #             if type(w) is datetime.datetime:
    #                 result_list[i][j] = w.strftime("%Y-%m-%d %H:%M:%S")
    #
    #     if result_list is not None:
    #         return {"sign": 1, "data": result_list}
    #     else:
    #         return {"sign": 0, "data": None}

    # @staticmethod
    # @MsgProcessor
    # def f20815(**kwargs):  # purchasing_order에 plant 값 바꾸기
    #     result = None
    #
    #     for po_num, plant in kwargs.items():
    #         result = dbm.query(f"UPDATE purchasing_order SET plant = '{plant}' WHERE po_num = '{po_num}'")
    #
    #     if result is not None:
    #         return {"sign": 1, "data": []}
    #     else:
    #         return {"sign": 0, "data": None}

    # @staticmethod
    # @MsgProcessor
    # def f20816(**kwargs):  # purchasing_order에 plant 값 바꾸기
    #     result = None
    #
    #     for receiving_code, plant in kwargs.items():
    #         result = dbm.query(f"UPDATE receiving SET plant_code = '{plant}' WHERE receiving_code = '{receiving_code}'")
    #
    #     if result is not None:
    #         return {"sign": 1, "data": []}
    #     else:
    #         return {"sign": 0, "data": None}


    def send_test(self, msg):
        try:
            encoded = msg.encode()
            test_socket.send(str(len(encoded)).ljust(16).encode())
            test_socket.send(encoded)
        except Exception:
            print(traceback.format_exc())

    def send_test(self, msg):
        try:
           encoded = msg.encode()
           test_socket.send(str(len(encoded)).ljust(16).encode())
           test_socket.send(encoded)
        except Exception as e:
           print(traceback.format_exc())
           # print(e)

    def recv_test(self):
        def recv_all(count):
            buf = b""
            while count:
                new_buf = test_socket.recv(count)
                if not new_buf:
                   return None
                buf += new_buf
                count -= len(new_buf)
            return buf

        try:
            while True:
                length = recv_all(16)
                data = recv_all(int(length))
                d = json.loads(data.decode())
                if type(d) is str:
                    d = json.loads(d)
                self.recv(**d)

        except Exception as e:
            print(traceback.format_exc())
            # print(e)

test_socket = None

if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = "0000"
    port = 3306
    # dbm = dbManager.DBManager(host, user, password, port)

    import socket
    from threading import Thread

    root = tk.Tk()  # 부모 창
    root.geometry("1600x900")
    test_frame = Receiving(root)
    test_frame.place(x=300, y=130)


    HOST = "192.168.0.29"
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        test_socket = sock
        sock.connect((HOST, PORT))
        test_frame.after_init()
        t = Thread(target=test_frame.recv_test, args=())
        t.daemon = True
        t.start()
        root.mainloop()