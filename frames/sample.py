import tkinter as tk
import tkinter.ttk as ttk

class SampleFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        
        # frame 생성
        self.frame1 = tk.Frame(self, width=950, height=350, bg="red") # 왼쪽 위 구역
        self.frame2 = tk.Frame(self, width=350, height=350, bg="yellow") # 오른쪽 위 구역
        self.frame3 = tk.Frame(self, width=950, height=350, bg="green") # 왼쪽 아래 구역
        self.frame4 = tk.Frame(self, width=350, height=350, bg="blue") # 오른쪽 아래 구역

        # frame
        self.frame2.grid_propagate(False)

        # frame 배치
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0)
        self.frame4.grid(row=1, column=1)

        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        # grid로 배치하기
        # 아래 내용 참고
        self.la_1 = ttk.Label(self.frame2, text="최대 일곱글자임", width=14)
        self.en_1 = ttk.Entry(self.frame2, width=15)
        self.bt_1 = ttk.Button(self.frame2, text="1")

        self.la_2 = ttk.Label(self.frame2, text="두자", width=14)
        self.en_2 = ttk.Entry(self.frame2, width=15)
        self.bt_2 = ttk.Button(self.frame2, text="2")
        
        self.la_1.grid(row=0, column=0, padx=5, pady=10)
        self.en_1.grid(row=0, column=1, padx=5, pady=10)
        self.bt_1.grid(row=0, column=2, padx=5, pady=10)

        self.la_2.grid(row=1, column=0, padx=5, pady=10)
        self.en_2.grid(row=1, column=1, padx=5, pady=10)
        self.bt_2.grid(row=1, column=2, padx=5, pady=10)

        self.frame2.grid_columnconfigure(1, weight=1)

        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        
        
        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        # place로 배치하기
        self.la_3 = ttk.Label(self.frame4, text="세글자", width=14)
        self.en_3 = ttk.Entry(self.frame4, width=15)
        self.bt_3 = ttk.Button(self.frame4, text="3")

        self.la_4 = ttk.Label(self.frame4, text="네글자임", width=14)
        self.en_4 = ttk.Entry(self.frame4, width=15)
        self.bt_4 = ttk.Button(self.frame4, text="4")

        # 좌표는 들어가는 위젯에 따라 달라질 수 있음
        # 다른 프레임 구조에 따라 y값이 바뀔 수 있음
        self.la_3.place(x=5, y=12)
        self.en_3.place(x=127, y=12)
        self.bt_3.place(x=258, y=12)

        self.la_4.place(x=5, y=57) # 12 + i * 45
        self.en_4.place(x=127, y=57)
        self.bt_4.place(x=258, y=57)