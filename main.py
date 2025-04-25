import base64
import json
import socket
import threading
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import traceback
from io import BytesIO
from PIL import Image, ImageTk

import pyglet

from color import Color
from frames import *
from frames import notification
from line import *

pyglet.options["win32_gdi_font"] = True
font_name = "경기천년제목 Medium"
font_path = "경기천년제목_Medium.ttf"
pyglet.font.add_file(font_path)

# logo generator
# https://fontmeme.com/pixel-fonts/

# find icon
# https://www.flaticon.com/icon-fonts-most-downloaded?weight=bold&type=uicon

# find font
# https://noonnu.cc/index

class Notification(tk.Frame):
    def __init__(self, root, radius, bg, fg, font, *args, **kwargs):
        super().__init__(root)
        self.root = root
        self.radius = radius
        self.bg = bg
        self.fg = fg
        self.font = font
        self.config(width=radius * 2 + 1, height=radius * 2 + 1)

        self.canvas = tk.Canvas(self, width=radius * 2 + 1, height=radius * 2 + 1, bg=Color.WHITE, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.draw(0)

    def draw(self, n):
        self.canvas.delete("all")
        if not n or n < 0:
            return
        self.canvas.create_oval(0, 0, self.radius * 2, self.radius * 2, fill=self.bg, outline=self.bg)
        self.canvas.create_text(self.radius, self.radius, text=n, font=self.font, fill=self.fg, anchor="center")

class Tab:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
        self.button = None

    def __hash__(self):
        return hash((self.first, self.second, self.third))

    def __eq__(self, other):
        if isinstance(other, Tab):
            return (self.first, self.second, self.third) == (other.first, other.second, other.third)
        return False

class Category:
    def __init__(self, btn: tk.Button = None):
        self.button = btn
        self.categories = {}

    def add(self, id_, category):
        self.categories[id_] = category

    def get(self, id_):
        return self.categories[id_]

class AppFrame(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

    def font(self, size, *args):
        return self.root.font(size, *args)

    def send_(self, msg):
        self.root.send_(msg)

    def prev_page(self):
        self.root.prev_page()

    def next_page(self):
        self.root.next_page()

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.socket = None

        self.geometry("1600x900")
        self.resizable(width=False, height=False)
        self.title("ERP")
        self.configure(background=Color.WHITE)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.category = {
            "인사": {
                "직원관리": {
                    # "테스트": [sample.SampleFrame, sample2.SampleFrame2],
                    "사원관리": [employee_management.EmployeeManagement],
                },
                # "출퇴기록": {
                #     "근태현황": [attendance_status.AttendanceStatus],
                # },
                "연차휴가관리": {
                    "초과근무관리": [overtime_management.OvertimeManagement],
                    "연차관리": [Time_off_management.Timeoffmanagement],
                },
                "급여관리": {
                    "급여관리명세서": [pay_stub.PayStub],
                    "퇴직금명세서": [serverance_pay.SeverancePay],
                },
                # "회사정보": {
                #     "회사정보": [company_information.CompanyInformation],
                # },
            },
            "기술": {
                "생산관리": {
                    "작업표준서": [SOP.SOP],
                    "BOM": [BOM.BOM],
                    "생산지시서": [MO.Manufacturing_Order],
                    "출고": [shipping.Shipping],
                    "입고": [receiving.Receiving],
                },
                "자재관리": {
                    "자재조회": [materialFrame.materialFrame],
                    "구매요청서": [PO.PurchasingOrder]
                },
                "물류관리": {
                    "창고등록마스터": [Plant.Plant],
                    "창고별자재조회": [plantFrame.plantFrame],
                }
            },
            "영업": {
                "거래처": {
                    "거래처등록": [add_business_partner.add_business_partner_Frame],
                    "거래처관리": [Customer_management.Customer_management_Frame],
                    "거래내역 조회": [history.history_Frame],
                },
                "발주서": {
                    "발주서관리": [order_form.order],
                },
                "판매 실적": {
                    "판매 실적 조회": [Sales_Performance.Sales_Performance],
                }
            },
            "회계": {
                "재무회계": {
                    "전표": [ac_accountbook.AccountBookFrame],
                    "세금계산서": [ac_taxinvoice.TaxInvoiceFrame],
                    "계정관리": [ac_accountsubject.AccountSubjectFrame],
                    "재무상태표": [Financial_statement.Financial_statement],
                    "손익계산서": [income_statement.income_statement],
                },
                "관리회계": {
                    "생산비용 분석": [Production_cost_analysis_1.Production_cost_analysis_1,
                                Production_cost_analysis_2.Production_cost_analysis_2]
                },
            },
        }

        self.font_family = font_name
        self.logged_in = False
        self.id_ = None
        self.name = None
        self.dept = None
        self.grade = None
        self.pic = None

        self.current_category = [None, None, None]
        self.opened_category = []
        self.tabs = []
        self.etc_buttons = []

        # 상단 좌측
        self.fr_logo = tk.Frame(self, width=300, height=130, bg=Color.WHITE)
        self.fr_logo.grid(row=0, column=0)

        # self.im_logo = tk.PhotoImage(file="images/logo.png")
        # self.la_logo = tk.Label(self.fr_logo, image=self.im_logo, width=120, height=100, bg=Color.WHITE)
        # self.la_logo.bind("<Button-1>", lambda e: self.screen_main())
        # self.la_logo.place(x=160, y=0)

        # 상단 우측
        self.fr_nav = tk.Frame(self, width=1300, height=130, bg=Color.WHITE)
        self.fr_nav.grid(row=0, column=1)

        self.fr_notification = tk.Frame(self.fr_nav, width=1300, height=100, bg=Color.WHITE)
        self.fr_tabs = tk.Frame(self.fr_nav, width=1300, height=30, bg=Color.WHITE)

        # self.en_id = ttk.Entry(self.fr_notification)
        #
        # self.im_login = tk.PhotoImage(file="images/sign-in-alt.png")
        # self.bt_login = tk.Button(self.fr_notification, image=self.im_login, relief="flat", bg=Color.WHITE,
        #                           command=self.login)
        #
        # self.im_logout = tk.PhotoImage(file="images/sign-out-alt.png")
        # self.bt_logout = tk.Button(self.fr_notification, image=self.im_logout, relief="flat", bg=Color.WHITE,
        #                            command=self.logout)
        #
        # self.im_alarm = tk.PhotoImage(file="images/bell.png")
        # self.im_alarm2 = tk.PhotoImage(file="images/bell-ring.png")
        # # self.bt_alarm = tk.Button(self.fr_notification, padx=10, pady=10, text=0, command=self.draw_nt)
        # self.bt_alarm = tk.Button(self.fr_notification, image=self.im_alarm, relief="flat", bg=Color.WHITE,
        #                           command=self.draw_nt)
        #
        # self.im_chat = tk.PhotoImage(file="images/comment-alt-middle.png")
        # self.bt_chat = tk.Button(self.fr_notification, image=self.im_chat, relief="flat", bg=Color.WHITE,
        #                          command=self.toggle_chat)
        self.im_login = tk.PhotoImage(file="images/login.png")
        self.im_logout = tk.PhotoImage(file="images/logout.png")
        self.im_notification = tk.PhotoImage(file="images/notification.png")
        self.im_messenger = tk.PhotoImage(file="images/messenger.png")

        self.en_id = tk.Entry(self.fr_nav, width=20, highlightthickness=0, bd=0)
        self.en_pw = tk.Entry(self.fr_nav, width=20, show="*", highlightthickness=0, bd=0)

        # self.bt_login = tk.Button(self.fr_notification, width=18, pady=5, relief="flat", bg=Color.FOCUS, font=self.font(10), text="로그인", command=self.login)
        self.bt_login = tk.Button(self.fr_nav, width=170, pady=5, relief="flat", bg=Color.WHITE, image=self.im_login, command=self.login)
        self.bt_logout = tk.Button(self.fr_nav, width=170, pady=5, relief="flat", bg=Color.WHITE, image=self.im_logout, command=self.logout)
        self.bt_alarm = tk.Button(self.fr_nav, width=170, pady=5, relief="flat", bg=Color.WHITE, image=self.im_notification, command=self.draw_nt)
        self.bt_chat = tk.Button(self.fr_nav, width=170, pady=5, relief="flat", bg=Color.WHITE, image=self.im_messenger, command=self.toggle_chat)
        # self.bt_logout = tk.Button(self.fr_notification, width=18, pady=5, relief="flat", bg=Color.FOCUS, font=self.font(10), text="로그아웃", command=self.logout)
        # self.bt_alarm = tk.Button(self.fr_notification, width=18, pady=5, relief="flat", bg=Color.FOCUS, font=self.font(10), text="알림", command=self.draw_nt)
        # self.bt_chat = tk.Button(self.fr_notification, width=18, pady=5, relief="flat", bg=Color.FOCUS, font=self.font(10), text="채팅", command=self.toggle_chat)
        self.la_alarm = Notification(self.fr_nav, radius=8, bg="#FF0000", fg=Color.WHITE, font=self.font(8, "bold"))
        self.la_info = tk.Label(self.fr_nav, bg=Color.WHITE, font=self.font(10))
        self.im_info = None
        self.la_photo = tk.Label(self.fr_nav, image=self.im_info)


        # self.en_id.place(x=660, y=63)
        # self.en_pw.place(x=820, y=63)
        # self.bt_login.place(x=980, y=57)

        # self.la_photo.place(x=920, y=17)
        self.default_img = Image.open("images/default_profile.jpg").resize((100, 100))

        self.en_id.place(x=920, y=17)
        self.en_pw.place(x=920, y=57)
        self.hl_id = HorizontalLine(self.fr_nav, 920, 42, 143, Color.BLACK)
        self.hl_pw = HorizontalLine(self.fr_nav, 920, 82, 143, Color.BLACK)

        self.bt_alarm.place(x=1090, y=17)
        self.bt_chat.place(x=1090, y=57)
        self.bt_login.place(x=1090, y=97)

        self.la_alarm.place(x=1260, y=3)

        self.fr_notification.grid(row=0, column=0)
        self.fr_tabs.grid(row=1, column=0)
        self.fr_tabs.pack_propagate(False)

        # 중앙 좌측
        self.fr_menu = tk.Frame(self, width=300, height=700, bg=Color.WHITE)
        self.fr_menu.grid(row=1, column=0)

        # 중앙 우측
        self.fr_app = AppFrame(self, width=1300, height=700)
        self.fr_app.grid(row=1, column=1)

        self.apps = {}
        self.app = None

        # 하단 좌측
        self.fr_etc = tk.Frame(self, width=300, height=70, bg=Color.WHITE)
        self.fr_etc.grid(row=2, column=0, sticky="n")
        # self.fr_etc.pack_propagate(False)
        #
        # self.fr_etc_inner = tk.Frame(self.fr_etc, bg=Color.WHITE)
        # self.fr_etc_inner.pack(expand=True)
        #
        # self.etc_buttons.append(
        #     tk.Button(self.fr_etc_inner, text="알림 테스트", bg=Color.FOCUS, relief="flat", padx=30, pady=5,
        #               command=lambda: self.add_nt({
        #                   "from_id": "e001",
        #                   "from_name": "테스트",
        #                   "type": "appr",
        #                   "msg": {
        #                       "name": "테스트",
        #                       "appr_type": "aa",
        #                       "appr_contents": "bb",
        #                       "sign": []
        #                   },
        #               })))
        # # self.etc_buttons.append(tk.Button(self.fr_etc_inner, text="퇴근", bg=Color.FOCUS, relief="flat", padx=30, pady=5, command=self.add_nt))
        # self.etc_buttons.append(
        #     tk.Button(self.fr_etc_inner, text="e001>e006 결재", bg=Color.FOCUS, relief="flat", padx=30, pady=5,
        #               command=self.appr_r))

        # 하단 우측
        self.fr_footer = tk.Frame(self, width=1300, height=70, bg=Color.WHITE)
        self.fr_footer.grid(row=2, column=1)

        self.current_page = 0
        self.pages = 1
        self.footer_buttons = []

        self.category_tree = Category()
        for first in self.category:
            first_tree = Category(tk.Button(self.fr_menu, text=f"　{first}", anchor="w", bg=Color.WHITE, fg=Color.FOCUS,
                                            font=self.font(16, "bold"), relief="flat",
                                            command=lambda x=first: self.select_category(0, x)))
            self.category_tree.add(first, first_tree)

            for second in self.category[first]:
                second_tree = Category(
                    tk.Button(self.fr_menu, text=f"　　　{second}", anchor="w", bg=Color.WHITE, fg=Color.BLACK,
                              font=self.font(14, "bold"), relief="flat",
                              command=lambda x=second: self.select_category(1, x)))
                first_tree.add(second, second_tree)

                for third in self.category[first][second]:
                    third_tree = Category(
                        tk.Button(self.fr_menu, text=f"　　　　　　{third}", anchor="w", bg=Color.WHITE, fg=Color.BLACK,
                                  font=self.font(12, "bold"), relief="flat",
                                  command=lambda x=third: self.select_category(2, x)))
                    second_tree.add(third, third_tree)

        # sep
        HorizontalLine(self, 300, 130, 1300, Color.BLACK)
        VerticalLine(self, 300, 130, 1300, Color.BLACK)

        # test
        # HorizontalLine(self, 0, 0, 1600, Color.BLACK)
        # HorizontalLine(self, 0, 16, 1600, Color.BLACK)
        # HorizontalLine(self, 0, 88, 1600, Color.BLACK)

        # HorizontalLine(self, 0, 100, 1600, Color.BLACK)

        # logo
        self.im_logo_center = tk.PhotoImage(file="images/logo_center.png")
        self.la_logo_center = tk.Label(self.fr_nav, image=self.im_logo_center, bg=Color.WHITE)
        self.la_logo_center.bind("<Button-1>", lambda e: self.screen_main())
        self.la_logo_center.place(x=0, y=0)

        # 알림
        self.nt_frame = notification.NotificationFrame(self, self.on_nt_delete)
        self.set_nt_button()
        # self.bt_alarm.config(text=self.nt_frame.get_nt_len())
        self.nt_flag = True

        # 채팅
        self.chat_frame = chat_frame.ChattingFrame(self, self.socket)
        self.chat_frame.place(x=1200, y=-950)
        self.chat_visible = False

        # 결재
        self.fr_appr_r = None
        self.fr_appr_p = None

        # self.nt_button = tk.Button(self.fr_notification, text=self.nt_frame.get_nt_len(), command=self.draw_nt)
        # self.nt_button.pack()
        # self.nt_button2 = tk.Button(self.fr_notification, command=self.add_nt)
        # self.nt_button2.pack()

        self.draw_etc()

        self.en_id.insert(0, "e001")
        self.en_pw.insert(0, "1111")

    def on_close(self):
        if callable(getattr(self.app, "on_close", None)):
            self.app.on_close()
        try:
            self.socket.close()
        finally:
            self.destroy()
            self.after(0, lambda x: self.quit(), None)

    def font(self, size, *args):
        return self.font_family, size, *args
    
    def msg_no_login(self):
        msgbox.showinfo("알림", "로그인 후 이용 가능합니다")
    
    # 알림
    def set_nt_button(self):
        self.la_alarm.draw(self.nt_frame.get_nt_len())
        # if self.nt_frame.get_nt_len() > 0:
        #     self.bt_alarm.config(image=self.im_alarm2)
        # else:
        #     self.bt_alarm.config(image=self.im_alarm)

    def draw_nt(self):
        if not self.logged_in:
            self.msg_no_login()
            return
        if self.nt_flag:
            self.nt_frame.place(x=1250, y=130)
            self.nt_frame.deployment()
            self.nt_flag = False
        else:
            self.nt_frame.place_forget()
            self.nt_flag = True

    def add_nt(self, data):
        self.send_(json.dumps({
            "code": 81006,
            "args": {
                "id": self.get_user_id(),
                "msg": json.dumps(data, ensure_ascii=False)
            }
        }, ensure_ascii=False))

    def on_nt_delete(self):
        self.set_nt_button()
    
    # 결재
    def appr_r(self):
        self.fr_appr_r = test_apprreq.ApprovalReqFrame(self)
        self.fr_appr_r.reqAppr()
        # self.fr_appr_r.user_name_entry.delete(0, tk.END)
        # self.fr_appr_r.user_name_entry.insert(0, self.name)
        # self.fr_appr_r.user_name_entry.config(state="disabled")
        self.fr_appr_r.user_name_entry.config(text=self.name)

    def appr_p(self, data):
        print("appr_p")
        self.fr_appr_p = test_apprpaper.ApprovalPaperFrame(self, data)
        self.fr_appr_p.place(x=1250, y=100)
        
    # 채팅
    def toggle_chat(self):
        if not self.logged_in:
            self.msg_no_login()
            return
        if self.chat_visible:
            self.hide_chat()
        else:
            self.show_chat()

    def show_chat(self):
        self.chat_visible = True
        self.animate_chat(visible=True)

    def hide_chat(self):
        self.chat_visible = False
        self.animate_chat(visible=False)

    def animate_chat(self, visible):
        target_y = 130 if visible else -850
        current_y = self.chat_frame.winfo_y()
        step = 70 if visible else -70

        if (visible and current_y < target_y) or (not visible and current_y > target_y):
            self.chat_frame.place(y=current_y + step)
            self.after(10, lambda x: self.animate_chat(visible), None)
        else:
            self.chat_frame.place(y=target_y)

    def set_default(self, app):
        children = app.winfo_children()
        if not children:
            try:
                # app.config(font=self.font(10))
                pass
            except Exception:
                pass
            #
            #     try:
            #         if type(app) == tk.Button:
            #             app.config(bg=Color.FOCUS)
            #         # else:
            #         #     app.config(bg=Color.WHITE)
            #     except Exception:
            #         pass
            #
            return

        for child in children:
            self.set_default(child)
        pass

    # 메인화면(첫화면) 띄우기
    def screen_main(self):
        print("main")
        self.current_category = [None, None, None]

        self.draw_category()

        if self.opened_category is None:
            return
        if self.app is not None:
            self.app.destroy()
        self.app = dashboard.DashboardFrame(self.fr_app)
        self.app.place(x=0, y=0)

        if callable(getattr(self.app, "after_init", None)):
            self.app.after_init()
        self.opened_category = None
        self.draw_tabs()

        for b in self.footer_buttons:
            b.destroy()
        self.footer_buttons.clear()

    # 탭 버튼 선택
    def select_tab(self, tab):
        self.current_category[0] = tab.first
        self.current_category[1] = tab.second
        self.select_category(2, tab.third)

    # 탭 추가
    def append_tab(self, first, second, third):
        # print(first, second, third)
        tab = Tab(first, second, third)
        if tab in self.tabs:
            idx = self.tabs.index(tab)
            self.tabs.append(self.tabs.pop(idx))
            return

        tab.button = tk.Button(self.fr_tabs, text=tab.third, height=30, padx=10, font=self.font(10), relief="flat",
                               command=lambda: self.select_tab(tab))
        self.tabs.append(tab)

        if len(self.tabs) > 12:
            self.tabs.pop(0).button.destroy()

    # 탭 그리기
    def draw_tabs(self):
        for tab in self.tabs:
            tab.button.pack_forget()

        for tab in self.tabs[:-1]:
            tab.button.config(bg=Color.WHITE)
        if self.tabs:
            if self.opened_category is None:
                self.tabs[-1].button.config(bg=Color.WHITE)
            else:
                self.tabs[-1].button.config(bg=Color.FOCUS)

        for tab in self.tabs[::-1]:
            tab.button.pack(side="left", anchor="w")

    # 카테고리 선택
    def select_category(self, depth, key):
        # 이미 선택된 카테고리
        if self.current_category[depth] == key:
            if depth < 2:
                self.current_category[depth] = None
            else:
                return
        else:
            self.current_category[depth] = key
        for i in range(depth + 1, 3):
            self.current_category[i] = None

        if depth == 2:
            print(key)
            # 로그아웃 상태
            if not self.logged_in:
                self.msg_no_login()
                return
            category = self.category[self.current_category[0]][self.current_category[1]][self.current_category[2]]
            # button = self.category_tree.get(self.current_category[0]).get(self.current_category[1]).get(self.current_category[2]).button
            # print(button)
            self.opened_category = category
            self.pages = len(category)

            for key in self.apps:
                if self.apps[key] is not None:
                    self.apps[key].destroy()
                    self.apps[key] = None
            self.app = None

            self.apps = {
                i: None for i in range(self.pages)
            }

            frame = category[0]
            self.current_page = 0

            # 프레임 아직 안만들었을 경우
            if frame is None:
                return

            self.apps[self.current_page] = frame(self.fr_app)
            self.app = self.apps[self.current_page]

            if self.app is None:
                print("App is None")
                return

            self.append_tab(*self.current_category)
            self.set_default(self.app)

            if callable(getattr(self.app, "after_init", None)):
                self.app.after_init()
            else:
                # print("Frame doesnt have after_init()")
                pass
            self.app.place(x=0, y=0)
            self.draw_pages()
            self.draw_tabs()
        self.draw_category()

    # 카테고리 그리기(좌측)
    def draw_category(self):
        y = 0
        dy = 40
        for first in self.category:
            first_tree = self.category_tree.get(first)
            first_tree.button.place(y=y, width=300, height=dy)
            y += dy

            for second in self.category[first]:
                second_tree = first_tree.get(second)
                if self.current_category[0] == first:
                    second_tree.button.place(y=y, width=300, height=dy)
                    y += dy
                else:
                    second_tree.button.place_forget()

                for third in self.category[first][second]:
                    third_tree = second_tree.get(third)
                    if self.current_category[1] == second:
                        third_tree.button.place(y=y, width=300, height=dy)
                        y += dy
                    else:
                        third_tree.button.place_forget()

    # 페이지 버튼 그리기
    def draw_pages(self):
        for b in self.footer_buttons:
            b.destroy()
        self.footer_buttons.clear()
        self.footer_buttons.append(tk.Button(self.fr_footer, text="<", bg=Color.WHITE, padx=10, pady=10, relief="flat",
                                             command=self.prev_page))
        for i in range(self.pages):
            self.footer_buttons.append(
                tk.Button(self.fr_footer, text=str(i + 1), bg=Color.WHITE, padx=10, pady=10, relief="flat",
                          command=lambda x=i: self.select_page(x)))
            if self.current_page == i:
                self.footer_buttons[-1].config(bg=Color.GRAY)
            else:
                self.footer_buttons[-1].config(bg=Color.WHITE)
        self.footer_buttons.append(tk.Button(self.fr_footer, text=">", bg=Color.WHITE, padx=10, pady=10, relief="flat",
                                             command=self.next_page))

        for b in self.footer_buttons:
            b.pack(side="left")

    # 이전 페이지
    def prev_page(self):
        if self.current_page <= 0:
            return

        self.select_page(self.current_page - 1)

    # 다음 페이지
    def next_page(self):
        if self.current_page >= self.pages - 1:
            return

        self.select_page(self.current_page + 1)

    # 페이지 선택
    def select_page(self, page):
        print(page + 1, "page")
        first_load = False
        if (self.current_page == page) or (page not in self.apps):
            return

        self.current_page = page
        if self.apps[page] is None:
            self.apps[page] = self.opened_category[page](self.fr_app)
            first_load = True

        self.app.place_forget()
        self.app = self.apps[page]

        if first_load and callable(getattr(self.app, "after_init", None)):
            self.app.after_init()

        self.app.place(x=0, y=0)
        self.draw_pages()

    def draw_etc(self):
        for button in self.etc_buttons:
            button.pack_forget()
        if self.logged_in:
            for button in self.etc_buttons:
                button.pack(side="left", padx=5)

    def login(self):
        msg = {
            "code": 81001,
            "args": {
                "id": self.en_id.get(),
                "pw": self.en_pw.get()
            }
        }
        self.send_(json.dumps(msg, ensure_ascii=False))

    def logout(self):
        msg = {
            "code": 81002,
            "args": {
                "id": self.get_user_id()
            }
        }
        self.send_(json.dumps(msg, ensure_ascii=False))
    #
    # def start_work(self):
    #     if not self.logged_in:
    #         return
    #     # msg = {
    #     #     "code": 71003,
    #     #     "args": {
    #     #         "from_id": self.en_id.get(),
    #     #         "type": "user",
    #     #         "to_id": "e002",
    #     #         "msg": "hello"
    #     #     }
    #     # }
    #     # self.send_(json.dumps(msg, ensure_ascii=False))
    #     # print("start_work")
    #
    #     if self.id_ == "e006":
    #         self.add_nt({
    #             "from_id": "e001",
    #             "from_name": "성진하",
    #             "type": "appr",
    #             "msg": {
    #                 "name": "성진하",
    #                 "appr_type": "aa",
    #                 "appr_contents": "bb",
    #                 "sign": []
    #             },
    #         })
    #
    # def finish_work(self):
    #     if not self.logged_in:
    #         return
    #     print("finish_work")

    def get_user_id(self): # 사원 코드
        return self.id_

    def get_user_name(self): # 사원명
        return self.name
    
    def get_user_dept(self): # 부서
        return self.dept

    def get_user_grade(self): # 직급
        return self.grade
    

    # 메세지 보내기
    def send_(self, msg):
        try:
            if not msg or self.socket is None:
                return
            encoded = msg.encode()
            self.socket.send(str(len(encoded)).ljust(16).encode())
            self.socket.send(encoded)
            print("send:", msg)
        except Exception as e:
            print(f"Error in send_(): {e}")

    # 메세지 받기
    def recv(self):
        def recv_all(count):
            buf = b""
            while count:
                new_buf = self.socket.recv(count)
                if not new_buf:
                    return None
                buf += new_buf
                count -= len(new_buf)
            return buf

        while True:
            try:
                if self.socket is None:
                    return
                length = recv_all(16)
                data = recv_all(int(length)).decode()

                if not data:
                    break
                print("recv:", json.loads(data))
                d = json.loads(data)
                if type(d) is str:
                    d = json.loads(d)

                code = d.get("code")
                sign = d.get("sign")
                data = d.get("data")

                if code == 81001:  # login
                    if sign == 1:
                        self.logged_in = True
                        self.id_ = data.get("id")
                        self.name = data.get("name")
                        self.grade = data.get("grade")
                        self.dept = data.get("dept")
                        pic = data.get("pic")
                        self.en_id.config(state="disabled")
                        self.bt_login.place_forget()
                        # self.bt_logout.place(x=1050, y=35)
                        self.bt_logout.place(x=1090, y=97)
                        self.screen_main()
                        self.draw_etc()

                        self.la_photo.place(x=920, y=17)
                        self.la_info.config(text=f"{self.name} {self.grade} ({self.dept})")
                        self.la_info.place(x=900, y=97)
                        self.hl_id.hide()
                        self.hl_pw.hide()
                        self.en_id.place_forget()
                        self.en_pw.place_forget()

                        self.chat_frame.show_main()


                        if pic:
                            try:
                                first_encode = base64.b64decode(pic)
                                img_binary = base64.b64decode(first_encode)

                                image = Image.open(BytesIO(img_binary)).resize((60, 60))
                                # image_chat = Image.open(BytesIO(img_binary)).resize((50, 50))
                                self.chat_info = ImageTk.PhotoImage(image)
                                self.im_info = ImageTk.PhotoImage(image)
                                self.la_photo.config(image=self.im_info)
                            except Exception as e:
                                print("사진 불러오기 오류", e)
                                self.im_info = ImageTk.PhotoImage(self.default_img)
                                self.la_photo.config(image=self.im_info)
                        else:
                            try:
                                self.default_img = Image.open("default_profile.jpg").resize((60, 60))
                            except FileNotFoundError:
                                self.default_img = Image.new("RGB", (60, 60), (200, 200, 200))
                            self.im_info = ImageTk.PhotoImage(self.default_img)
                            self.la_photo.config(image=self.im_info)



                        self.chat_frame.update_top_info(self.im_info)

                        # 과거 알람
                        self.send_(json.dumps({
                            "code": 81008,
                            "args": {
                                "code": self.id_
                            }
                        }, ensure_ascii=False))
                    else:
                        msgbox.showinfo("알림", "로그인에 실패했습니다")
                        print("login failed")
                        pass
                elif code == 81002:  # logout
                    if sign == 1:
                        self.logged_in = False
                        self.id_ = None
                        self.name = None
                        self.en_id.config(state="normal")
                        self.bt_logout.place_forget()
                        # self.bt_login.place(x=1050, y=35)
                        self.bt_login.place(x=1090, y=97)
                        for tab in self.tabs:
                            tab.button.destroy()
                        self.tabs.clear()
                        self.draw_tabs()
                        self.screen_main()
                        self.draw_etc()

                        self.nt_frame.place_forget()
                        self.nt_frame.delete_all()
                        self.nt_flag = True
                        # self.bt_alarm.config(image=self.im_alarm)
                        self.set_nt_button()

                        self.la_photo.place_forget()
                        self.la_info.place_forget()
                        self.hl_id.show()
                        self.hl_pw.show()
                        self.en_id.place(x=920, y=17)
                        self.en_pw.place(x=920, y=57)

                        self.hide_chat()

                    else:
                        msgbox.showinfo("알림", "로그아웃에 실패했습니다")
                        print("logout failed")
                        pass
                elif code == 71003:  # um > msg
                    type_ = data.get("type")
                    if type_ == "appr":  # 결재 알림
                        self.add_nt(data)
                        self.set_nt_button()
                        pass
                    elif type_ == "user":
                        # chat_frame.recv()
                        pass
                    print("msg:", data)
                elif code in [81004, 71005]:  # appr
                    if self.fr_appr_r is not None:
                        self.fr_appr_r.recv(**d)
                    if self.fr_appr_p is not None:
                        self.fr_appr_p.recv(**d)
                elif code in [81006, 81008]: # add noti
                    self.nt_frame.recv(**d)
                    self.set_nt_button()
                elif code == 81007: # remove noti
                    self.nt_frame.recv(**d)
                elif 85010 <= code <= 85100:
                    if self.logged_in:
                        self.chat_frame.recv(**d)
                    else:
                        from tkinter import messagebox
                        messagebox.showerror("경고", "로그인 하세요")

                if callable(getattr(self.app, "recv", None)):
                    self.app.recv(**d)
                else:
                    print("★ 프레임에 recv()가 없음")
            except OSError:
                print("recv(): Connection closed")
                break
            except ConnectionResetError:
                print("recv(): Connection failed")
                break
            except Exception as e:
                print(traceback.format_exc())
                continue
        self.socket = None

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                self.socket = sock
                # self.socket.connect(("localhost", 12345))
                self.socket.connect(("192.168.0.29", 12345))
                self.screen_main()

                t = threading.Thread(target=self.recv, args=())
                t.daemon = True
                t.start()
                self.mainloop()

        except Exception as e:
            print(traceback.format_exc())


if __name__ == "__main__":
    main = Main()
    main.run()