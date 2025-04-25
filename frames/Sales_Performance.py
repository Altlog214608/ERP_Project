import tkinter as tk
import tkinter.messagebox as msgbox
from tablewidget import TableWidget
from color import Color
import json
from tkinter import ttk

# tkcalendar 달력 선택 패키지 설치 필수
from tkcalendar import DateEntry  # 날짜 선택을 위한 모듈 추가
dbm = None
class Sales_Performance(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root

        # frame 생성
        self.topleft_Frame = tk.Frame(self, width=950, height=350)  # 왼쪽 위 구역
        self.topright_Frame = tk.Frame(self, width=350, height=350)  # 오른쪽 위 구역
        self.bottom_Frame = tk.Frame(self, width=1300, height=350)  # 아래 구역

        # frame 크기 자동 축소 방지 (pack/grid)
        self.topleft_Frame.grid_propagate(False)
        self.topleft_Frame.pack_propagate(False)
        self.topright_Frame.grid_propagate(False)
        self.topright_Frame.pack_propagate(False)
        self.bottom_Frame.grid_propagate(False)
        self.bottom_Frame.pack_propagate(False)

        # frame 배치
        self.topleft_Frame.grid(row=0, column=0)
        self.topright_Frame.grid(row=0, column=1)
        self.bottom_Frame.grid(row=1, column=0, columnspan=2)


        # 판매 실적 필드 생성
        self.create_order_form()

    def create_order_form(self): # 등록
        w=14
        e=15
        self.topleft_Frame.grid_columnconfigure(0, weight=2)
        self.topleft_Frame.grid_columnconfigure(1, weight=3)
        self.topleft_Frame.grid_columnconfigure(2, weight=2)
        self.topleft_Frame.grid_columnconfigure(3, weight=3)
        self.topleft_Frame.grid_columnconfigure(4, weight=2)
        self.topleft_Frame.grid_columnconfigure(5, weight=3)


        self.label2 = ttk.Label(self.topleft_Frame, text="발주서 코드",width=w, anchor="w")
        self.label2.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entry2 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry2.grid(row=0, column=1, padx=5, pady=5,sticky="ew")


        self.label3 = ttk.Label(self.topleft_Frame, text="내/외부",width=w, anchor="w")
        self.label3.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry3 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry3.grid(row=1, column=1, padx=5, pady=5,sticky="ew")

        self.label4 = ttk.Label(self.topleft_Frame, text="작성자 명",width=w, anchor="w")
        self.label4.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry4 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry4.grid(row=2, column=1, padx=5, pady=5,sticky="ew")

        self.label5 = ttk.Label(self.topleft_Frame, text="작성자 직책",width=w, anchor="w")
        self.label5.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.entry5 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry5.grid(row=3, column=1, padx=5, pady=5,sticky="ew")

        self.label6 = ttk.Label(self.topleft_Frame, text="작성자 연락처",width=w, anchor="w")
        self.label6.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.entry6 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry6.grid(row=4, column=1, padx=5, pady=5,sticky="ew")

        self.label7 = ttk.Label(self.topleft_Frame, text="작성자 이메일",width=w, anchor="w")
        self.label7.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.entry7 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry7.grid(row=5, column=1, padx=5, pady=5,sticky="ew")

        self.label8 = ttk.Label(self.topleft_Frame, text="관리자 명",width=w, anchor="w")
        self.label8.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.entry8 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry8.grid(row=6, column=1, padx=5, pady=5,sticky="ew")

        self.label9 = ttk.Label(self.topleft_Frame, text="관리자 직책",width=w, anchor="w")
        self.label9.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.entry9 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry9.grid(row=7, column=1, padx=5, pady=5,sticky="ew")

        self.label10 = ttk.Label(self.topleft_Frame, text="관리자 연락처",width=w, anchor="w")
        self.label10.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        self.entry10 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry10.grid(row=8, column=1, padx=5, pady=5,sticky="ew")

        self.label11 = ttk.Label(self.topleft_Frame, text="관리자 이메일",width=w, anchor="w")
        self.label11.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        self.entry11 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry11.grid(row=9, column=1, padx=5, pady=5,sticky="ew")

        self.label12 = ttk.Label(self.topleft_Frame, text="완제품 코드",width=w, anchor="w")
        self.label12.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.production_Entry=ttk.Entry(self.topleft_Frame,width=e,state="disabled")
        self.production_Entry.grid(row=0, column=3, padx=5, pady=5,sticky="ew")

        self.label12 = ttk.Label(self.topleft_Frame, text="완제품 명",width=w, anchor="w")
        self.label12.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.product_name=ttk.Entry(self.topleft_Frame,width=e,state="disabled")
        self.product_name.grid(row=1,column=3,padx=5,pady=5,sticky="ew")


        self.label14 = ttk.Label(self.topleft_Frame, text="단가",width=w, anchor="w")
        self.label14.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.entry14 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry14.grid(row=2, column=3, padx=5, pady=5,sticky="ew")

        self.label16 = ttk.Label(self.topleft_Frame, text="거래 수량",width=w, anchor="w")
        self.label16.grid(row=3, column=2, padx=5, pady=5, sticky="w")
        self.entry16 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry16.grid(row=3, column=3, padx=5, pady=5,sticky="ew")

        self.label17 = ttk.Label(self.topleft_Frame, text="총 가격",width=w, anchor="w")
        self.label17.grid(row=4, column=2, padx=5, pady=5, sticky="w")
        self.entry17 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry17.grid(row=4, column=3, padx=5, pady=5,sticky="ew")

        self.label18 = ttk.Label(self.topleft_Frame, text="부가세",width=w, anchor="w")
        self.label18.grid(row=5, column=2, padx=5, pady=5, sticky="w")
        self.entry18 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry18.grid(row=5, column=3, padx=5, pady=5,sticky="ew")

        self.label30 = ttk.Label(self.topleft_Frame, text="순 이익",width=w, anchor="w")
        self.label30.grid(row=6, column=2, padx=5, pady=5, sticky="w")

        self.net_profit_entry = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.net_profit_entry.grid(row=6,column=3,padx=5,pady=5,sticky="ew")

        self.label19 = ttk.Label(self.topleft_Frame, text="거래처 코드",width=w, anchor="w")
        self.label19.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        self.correspondent_entry = ttk.Entry(self.topleft_Frame,width=e,state="disabled")
        self.correspondent_entry.grid(row=0, column=5, padx=5, pady=5,sticky="ew")

        self.label20 = ttk.Label(self.topleft_Frame, text="사업자 번호",width=w, anchor="w")
        self.label20.grid(row=1, column=4, padx=5, pady=5, sticky="w")
        self.entry20 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry20.grid(row=1, column=5, padx=5, pady=5,sticky="ew")

        self.label21 = ttk.Label(self.topleft_Frame, text="거래처 명",width=w, anchor="w")
        self.label21.grid(row=2, column=4, padx=5, pady=5, sticky="w")
        self.entry21 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry21.grid(row=2, column=5, padx=5, pady=5,sticky="ew")

        self.label22 = ttk.Label(self.topleft_Frame, text="거래처 종류",width=w, anchor="w")
        self.label22.grid(row=3, column=4, padx=5, pady=5, sticky="w")
        self.entry22 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry22.grid(row=3, column=5, padx=5, pady=5,sticky="ew")

        self.label23 = ttk.Label(self.topleft_Frame, text="거래처 주소",width=w, anchor="w")
        self.label23.grid(row=4, column=4, padx=5, pady=5, sticky="w")
        self.entry23 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry23.grid(row=4, column=5, padx=5, pady=5,sticky="ew")

        self.label24 = ttk.Label(self.topleft_Frame, text="거래처 담당자 명",width=w, anchor="w")
        self.label24.grid(row=5, column=4, padx=5, pady=5, sticky="w")
        self.entry24 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry24.grid(row=5, column=5, padx=5, pady=5,sticky="ew")

        self.label25 = ttk.Label(self.topleft_Frame, text="담당자 연락처",width=w, anchor="w")
        self.label25.grid(row=6, column=4, padx=5, pady=5, sticky="w")
        self.entry25 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry25.grid(row=6, column=5, padx=5, pady=5,sticky="ew")

        self.label26 = ttk.Label(self.topleft_Frame, text="담당자 이메일",width=w, anchor="w")
        self.label26.grid(row=7, column=4, padx=5, pady=5, sticky="w")
        self.entry26 = ttk.Entry(self.topleft_Frame, width=e,state="disabled")
        self.entry26.grid(row=7, column=5, padx=5, pady=5,sticky="ew")

        self.label27 = ttk.Label(self.topleft_Frame, text="납기일",width=w, anchor="w")
        self.label27.grid(row=8, column=4, padx=5, pady=5, sticky="w")
        self.date_entry2 = DateEntry(self.topleft_Frame, width=w, background="#e3e3e3",state="disabled", foreground="white",date_pattern="yyyy-mm-dd")
        self.date_entry2.grid(row=8, column=5, padx=5, pady=5,sticky="ew")

        self.Creation_label = ttk.Label(self.topleft_Frame, text="작성 일자",width=w, anchor="w")
        self.Creation_label.grid(row=9, column=4, padx=5, pady=5, sticky="w")
        self.date_entry1 = DateEntry(self.topleft_Frame, width=w, background="#e3e3e3",state="disabled", foreground="white", date_pattern="yyyy-mm-dd")
        self.date_entry1.grid(row=9, column=5, padx=5, pady=5,sticky="ew")

        self.label28 = ttk.Label(self.topleft_Frame, text="수정 일자",width=w, anchor="w")
        self.label28.grid(row=10, column=4, padx=5, pady=5, sticky="w")
        self.date_entry3 = DateEntry(self.topleft_Frame, width=w, background="#e3e3e3",state="disabled", foreground="white",date_pattern="yyyy-mm-dd")
        self.date_entry3.grid(row=10, column=5, padx=5, pady=5,sticky="ew")

        self.topright_Frame.columnconfigure(0, weight=1, uniform="equal")  # column 1에 비례적으로 공간 분배
        self.topright_Frame.columnconfigure(1, weight=1, uniform="equal")  # column 2에도 동일하게 적용
        self.topright_Frame.columnconfigure(2, weight=1, uniform="equal")

        # 오른쪽 위
        self.label00 = ttk.Label(self.topright_Frame, text="발주서 코드", width=w, anchor="w")
        self.label00.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entry00 = ttk.Entry(self.topright_Frame, width=e)
        self.entry00.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.labela = ttk.Label(self.topright_Frame, text="거래처 코드", width=w, anchor="w")
        self.labela.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.allCorrespondent_entry = ttk.Entry(self.topright_Frame, width=e)
        self.allCorrespondent_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.labelb = ttk.Label(self.topright_Frame, text="완제품 코드", width=w, anchor="w")
        self.labelb.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.allproduction_entry = ttk.Entry(self.topright_Frame, width=e)
        self.allproduction_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.labelc = ttk.Label(self.topright_Frame, text="작성자명", width=w, anchor="w")
        self.labelc.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.allAuthor_entry = ttk.Entry(self.topright_Frame, width=e)
        self.allAuthor_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.labeld = ttk.Label(self.topright_Frame, text="관리자명", width=w, anchor="w")
        self.labeld.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.administrator_entry = ttk.Entry(self.topright_Frame, width=e)
        self.administrator_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        self.label31 = ttk.Label(self.topright_Frame, text="담당자명", width=w, anchor="w")
        self.label31.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        self.allmanager_entry = ttk.Entry(self.topright_Frame, width=e)
        self.allmanager_entry.grid(row=5, column=1, pady=5, padx=5, sticky="ew")

        self.labelz = ttk.Label(self.topright_Frame, width=w, text="납기일", anchor="w")
        self.labelz.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.date_entry4 = DateEntry(self.topright_Frame, width=e, foreground="white", date_pattern="yy.mm.dd")
        self.date_entry4.grid(row=6, column=1, padx=5, pady=6, sticky="ew")  # sticky="nsew"로 모든 방향에 맞게 채우기

        self.date_entry5 = DateEntry(self.topright_Frame, width=e, foreground="white", date_pattern="yy.mm.dd")
        self.date_entry5.grid(row=6, column=2, padx=5, pady=6, sticky="ew")  # sticky="nsew"로 모든 방향에 맞게 채우기

        self.labelf = ttk.Label(self.topright_Frame, text="작성일자", width=w, anchor="w")
        self.labelf.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.creation_date_start = DateEntry(self.topright_Frame, width=e, foreground="white",
                                             date_pattern="yy.mm.dd")
        self.creation_date_start.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

        self.creation_date_end = DateEntry(self.topright_Frame, width=e, foreground="white",
                                           date_pattern="yy.mm.dd")
        self.creation_date_end.grid(row=7, column=2, padx=5, pady=5, sticky="ew")

        self.labelg = ttk.Label(self.topright_Frame, text="수정 일자", width=w, anchor="w")
        self.labelg.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        self.modified_date_start = DateEntry(self.topright_Frame, width=e, foreground="white", date_pattern="yy.mm.dd")
        self.modified_date_start.grid(row=8, column=1, padx=5, pady=5, sticky="ew")

        self.modified_date_end = DateEntry(self.topright_Frame, width=e, foreground="white", date_pattern="yy.mm.dd")
        self.modified_date_end.grid(row=8, column=2, padx=5, pady=5, sticky="ew")

        self.btn_search = ttk.Button(self.topright_Frame, text="조회", command=self.select_performance)
        self.btn_search.grid(row=0, column=2, columnspan=2, padx=10, pady=5, sticky="e")

    def clear_fields(self):
        self.entry00.delete(0,tk.END)
        self.entry2.delete(0,tk.END)
        self.entry3.delete(0,tk.END)
        self.entry4.delete(0,tk.END)
        self.entry5.delete(0,tk.END)
        self.entry6.delete(0,tk.END)
        self.entry7.delete(0,tk.END)
        self.entry8.delete(0,tk.END)
        self.entry9.delete(0,tk.END)
        self.entry10.delete(0,tk.END)
        self.entry11.delete(0,tk.END)
        self.production_Entry.delete(0,tk.END)
        self.product_name.delete(0,tk.END)
        self.entry14.delete(0,tk.END)
        self.entry16.delete(0,tk.END)
        self.entry17.delete(0,tk.END)
        self.entry18.delete(0,tk.END)
        self.net_profit_entry.delete(0,tk.END)
        self.correspondent_entry.delete(0,tk.END)
        self.entry20.delete(0,tk.END)
        self.entry21.delete(0,tk.END)
        self.entry22.delete(0,tk.END)
        self.entry23.delete(0,tk.END)
        self.entry24.delete(0,tk.END)
        self.entry25.delete(0,tk.END)
        self.entry26.delete(0,tk.END)
        self.date_entry2.delete(0,tk.END)
        self.date_entry1.delete(0,tk.END)
        self.date_entry3.delete(0, tk.END)

    def select_info(self):
        #
        self.entry00.config(state = "normal")
        self.entry2.config(state = "normal")
        self.entry3.config(state = "normal")
        self.entry4.config(state = "normal")
        self.entry5.config(state = "normal")
        self.entry6.config(state = "normal")
        self.entry7.config(state = "normal")
        self.entry8.config(state = "normal")
        self.entry9.config(state = "normal")
        self.entry10.config(state = "normal")
        self.entry11.config(state = "normal")
        self.production_Entry.config(state = "normal")
        self.product_name.config(state = "normal")
        self.entry14.config(state = "normal")
        self.entry16.config(state = "normal")
        self.entry17.config(state = "normal")
        self.entry18.config(state = "normal")
        self.net_profit_entry.config(state = "normal")
        self.correspondent_entry.config(state = "normal")
        self.entry20.config(state = "normal")
        self.entry21.config(state = "normal")
        self.entry22.config(state = "normal")
        self.entry23.config(state = "normal")
        self.entry24.config(state = "normal")
        self.entry25.config(state = "normal")
        self.entry26.config(state = "normal")
        self.date_entry2.config(state = "normal")
        self.date_entry1.config(state = "normal")
        self.date_entry3.config(state = "normal")



    def select_performance(self): # 조건에 따라서 조회
        order_code=self.entry00.get() # 발주서 코드
        Customer_code=self.allCorrespondent_entry.get() # 거래처 코드
        product_code=self.allproduction_entry.get() # 완제품 코드
        creator_name=self.allAuthor_entry.get()  # 작성자명
        administrator_name=self.administrator_entry.get() # 관리자 명
        account_manager=self.allmanager_entry.get() # 거래처 담당자 명

        delivery_date_start=self.date_entry4.get_date() # 납기일
        delivery_date_start=delivery_date_start.strftime('%Y-%m-%d') if delivery_date_start else None
        delivery_date_end = self.date_entry5.get_date()
        delivery_date_end = delivery_date_end.strftime('%Y-%m-%d') if delivery_date_end else None

        creation_date_start=self.creation_date_start.get_date() # 작성일자별
        creation_date_start = creation_date_start.strftime('%Y-%m-%d') if creation_date_start else None
        creation_date_end = self.creation_date_end.get_date()
        creation_date_end=creation_date_end.strftime('%Y-%m-%d') if creation_date_end else None

        modified_date_start=self.modified_date_start.get_date() # 수정일자별
        modified_date_start = modified_date_start.strftime('%Y-%m-%d') if modified_date_start else None
        modified_date_end = self.modified_date_end.get_date()
        modified_date_end = modified_date_end.strftime('%Y-%m-%d') if modified_date_end else None

        send = {
            "code": 30401,
            "args": {
                "order_code": order_code,
                "Customer_code": Customer_code,
                "product_code": product_code,
                "creator_name": creator_name,
                "administrator_name":administrator_name,
                "account_manager":account_manager,
                "delivery_date_start": delivery_date_start,
                "delivery_date_end": delivery_date_end,
                "creation_date_start": creation_date_start,
                "creation_date_end": creation_date_end,
                "modified_date_start": modified_date_start,
                "modified_date_end": modified_date_end
            }
        }
        self.send_(send)

    # @staticmethod
    # def f30401(**kwargs):
    #     # 조회할 컬럼
    #     columns = [
    #         'order_form.order_code', 'order_form.internal_external', 'order_form.creator_name',
    #         'order_form.creator_position',
    #         'order_form.creator_phone', 'order_form.creator_email', 'order_form.administrator_name',
    #         'order_form.administrator_position',
    #         'order_form.administrator_phone', 'order_form.administrator_email', 'order_form.product_code',
    #         'order_form.product_name',
    #         'order_form.unit_price', 'order_form.stock', 'order_form.transaction_quantity', 'order_form.total_price',
    #         'order_form.order_vat',
    #         '(order_form.total_price - (order_form.unit_price * order_form.transaction_quantity)) AS NetProfit',
    #         # 순이익 계산
    #         'order_form.Customer_code', 'customer_management.business_number', 'customer_management.Customer_name',
    #         'customer_management.Type_business',
    #         'customer_management.business_adress', 'customer_management.ContactPerson_name',
    #         'customer_management.ContactPerson_phone', 'customer_management.e_mail',
    #         'order_form.delivery_date', 'order_form.creation_date', 'order_form.modified_date'
    #     ]
    #
    #     # 기본 쿼리 (order_form 테이블과 customer_management 테이블을 JOIN)
    #     sql_query = f"""
    #     SELECT
    #         {", ".join(columns)}
    #         FROM erp_db.order_form
    #         INNER JOIN erp_db.customer_management
    #         ON order_form.Customer_code = customer_management.Customer_code
    #     """
    #
    #     conditions = []  # 조건 리스트 초기화
    #     start_value, end_value = None, None  # 날짜 변수 초기화
    #
    #     # kwargs에서 조건 처리
    #     for key, value in kwargs.items():
    #         print("select:", key, value)
    #         if value:  # None 또는 빈 문자열을 제외하고 처리
    #             column_name = key  # 기본적으로 key를 column_name으로 설정
    #
    #             # 시작 날짜 처리 (start와 관련된 처리)
    #             if "start" in key:
    #                 start_value = value
    #                 column_name = key.replace('_start', '')  # '_start'를 제거하여 실제 컬럼명 추출
    #                 if start_value:
    #                     current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    #                     if start_value != current_date:  # 오늘 날짜가 아니면 조건 추가
    #                         conditions.append(f"{column_name} >= '{start_value} 00:00:00'")
    #
    #             # 종료 날짜 처리 (end와 관련된 처리)
    #             elif "end" in key:
    #                 end_value = value
    #                 column_name = key.replace('_end', '')  # '_end'를 제거하여 실제 컬럼명 추출
    #                 if end_value:
    #                     if start_value == end_value:
    #                         # start와 end 값이 같으면 조건을 추가하지 않음
    #                         continue
    #                     conditions.append(f"{column_name} <= '{end_value} 23:59:59'")
    #
    #             # 일반적인 값 비교 처리
    #             elif isinstance(value, str):  # 문자열일 때 LIKE 조건
    #                 conditions.append(f"{column_name} LIKE '%{value}%'")
    #             else:  # 문자열이 아닐 때 (정확한 값 비교)
    #                 conditions.append(f"{column_name} = '{value}'")
    #
    #     # WHERE 절이 존재할 경우 조건 추가
    #     if conditions:
    #         sql_query += " WHERE " + " AND ".join(conditions)
    #
    #     # 최종 SQL 쿼리
    #     print("쿼리:", sql_query)
    #     result = dbm.query(sql_query)
    #     print(result)
    #
    #     if result is not None:
    #         # datetime 문자열 형식 변경
    #         result = [
    #             tuple(item.strftime('%Y.%m.%d') if isinstance(item, datetime.datetime) else item for item in row)
    #             for row in result  # row에 값 넣고 item의 값을 하나씩 빼서 처리
    #         ]
    #         sign = 1
    #     else:
    #         print("오류:", result)
    #         sign = 0
    #
    #     # 결과 반환
    #     recv = {
    #         "sign": sign,
    #         "data": result if result else []  # 결과가 없으면 빈 리스트 반환
    #     }
    #     print(recv)
    #
    #     return recv



    def send_(self, some_dict):
        self.root.send_(json.dumps(some_dict, ensure_ascii=False))

    def recv(self, **kwargs):
        code, sign, data = kwargs.get("code"), kwargs.get("sign"), kwargs.get("data")
        print("code:", code)
        print("sign:", sign)
        print("data:", data)

        if code == 30401:
            if any(data[0]):
                    # 정상적인 데이터 처리
                    self.table = TableWidget(self.bottom_Frame,
                                             data=data,
                                             col_name=["발주 코드", "내/외부 여부", "작성자명", "작성자 직책", "작성자 연락처",
                                                       "작성자 이메일", "관리자명", "관리자 직책", "관리자 연락처", "관리자 이메일", "완제품 코드",
                                                       "완제품 명", "단가", "현 재고", "거래 수량", "총 가격", "부가세", "순 이익", "거래처 코드",
                                                       "사업자 번호", "거래처 명", "거래처 종류", "거래처 주소", "거래처 담당자", "담당자 연락처",
                                                       "담당자 이메일", "납기일", "작성일자", "수정일자"],
                                             has_checkbox=False,
                                             cols=29,
                                             new_row=False,
                                             col_width=[150] * 29,
                                             width=1300,
                                             height=350,
                                             padding=10)
                    self.table.grid(row=0, column=0)
                    self.clear_fields()
                    self.select_info()
                    print(data)

                    # 발주 코드
                    self.entry2.insert(0, data[0][0])
                    # 내/외부
                    self.entry3.insert(0, data[0][1])
                    # 작성자 명
                    self.entry4.insert(0, data[0][2])
                    # 작성자 직책
                    self.entry5.insert(0, data[0][3])
                    # 작성자 연락처
                    self.entry6.insert(0, data[0][4])
                   # 작성자 이메일
                    self.entry7.insert(0, data[0][5])
                    # 관리자 명
                    self.entry8.insert(0, data[0][6])
                    # 관리자 직책
                    self.entry9.insert(0, data[0][7])
                    # 관리자 연락처
                    self.entry10.insert(0, data[0][8])
                    # 관리자 이메일
                    self.entry11.insert(0, data[0][9])
                    # 완제품 코드
                    self.production_Entry.insert(0, data[0][10])
                    # 완제품 명
                    self.product_name.insert(0, data[0][11])
                    # 단가
                    self.entry14.insert(0, data[0][12])
                    # 거래 수량
                    self.entry16.insert(0, data[0][13])
                    # 총 가격
                    self.entry17.insert(0, data[0][14])
                    # 부가세
                    self.entry18.insert(0, data[0][15])
                    # 순 이익
                    self.net_profit_entry.insert(0, data[0][16])
                    # 거래처 코드
                    self.correspondent_entry.insert(0, data[0][17])
                    # 사업자 번호
                    self.entry20.insert(0, data[0][18])
                    # 거래처 명
                    self.entry21.insert(0, data[0][19])
                    # 거래처 종류
                    self.entry22.insert(0, data[0][20])
                    # 거래처 주소(국가)
                    self.entry23.insert(0, data[0][21])
                    # 거래처 담당자
                    self.entry24.insert(0, data[0][22])
                    # 거래처 담당자 연락처
                    self.entry25.insert(0, data[0][23])
                    # 거래처 담당자 이메일
                    self.entry26.insert(0, data[0][24])
                    # 납기일
                    self.date_entry2.set_date(data[0][25])
                    # 작성 일자
                    self.date_entry1.set_date(data[0][26])
                    # 수정 일자
                    self.date_entry3.set_date(data[0][27])
            else:
                msgbox.showerror("조회 오류", "조회된 데이터가 없습니다.")

    def after_init(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1600x900")
    r = Sales_Performance(root)
    r.place(x=300, y=130)
    root.mainloop()