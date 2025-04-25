import tkinter as tk
import traceback
from tkinter import ttk, messagebox

from PIL import ImageTk
from tkcalendar import DateEntry
import json


class Color:
   WHITE = "#FFFFFF"
   GRAY = "#DDDDDD"
   BLACK = "#000000"
   BUTTON = "#333333"
   FOCUS = "#555555"


# 전역 데이터
employees_data = []  # 직원 목록 (dict 리스트)
chatrooms_data = []  # 채팅방 목록 (dict 리스트)


test_socket = None


class ChattingFrame(ttk.Frame):
   def __init__(self, root, sock):
       super().__init__(root, width=400, height=800)
       self.root = root
       self.sock = sock
       self.current_chat_target = None
       self.current_room_id = None


       # ---------------------------
       # 1) ttk.Style 설정
       # ---------------------------
       self.style = ttk.Style()
       self.style.configure("ChatFrame.TFrame", background="#F5F5F5")
       self.style.configure("TopFrame.TFrame", background="#2F2F2F")
       self.style.configure("TitleLabel.TLabel", font=("맑은 고딕", 16, "bold"),
                            foreground="#FFFFFF", background="#2F2F2F")
       self.style.configure("SubTitleLabel.TLabel", font=("맑은 고딕", 14),
                            foreground="#EEEEEE", background="#2F2F2F")
       self.style.configure("SearchFrame.TFrame", background="#3A3A3A")


       # 이 예시에서는 ttk.Button로 배경색을 바꾸기 어려우므로 tk.Button 사용 권장
       self.style.configure("Main.TButton",
                            font=("맑은 고딕", 12, "bold"),
                            padding=6,
                            # foreground="#FFFFFF",
                            background="#333333")
       self.style.map("Main.TButton",
           background=[("active", "#444444")],
           relief=[("pressed", "sunken"), ("!pressed", "flat")]
       )
       self.style.configure("Search.TEntry", font=("맑은 고딕", 12))


       self.configure(style="ChatFrame.TFrame")


       # ---------------------------
       # 상단 프레임 (사용자 정보 + 검색)
       # ---------------------------
       self.fr_top = ttk.Frame(self, width=400, height=130, style="TopFrame.TFrame")
       self.fr_top.grid(row=0, column=0, sticky="nsew")
       self.fr_top.grid_propagate(False)
       self.create_top_frame()


       # ---------------------------
       # 중앙 프레임 (메인/채팅목록/그룹생성/채팅화면)
       # ---------------------------
       self.fr_middle = ttk.Frame(self, width=400, height=590, style="ChatFrame.TFrame")
       self.fr_middle.grid(row=1, column=0, sticky="nsew")
       self.fr_middle.grid_propagate(False)


       self.fr_main = ttk.Frame(self.fr_middle, style="ChatFrame.TFrame")
       self.fr_chatList = ttk.Frame(self.fr_middle, style="ChatFrame.TFrame")
       self.fr_group = ttk.Frame(self.fr_middle, style="ChatFrame.TFrame")
       self.fr_chat = ttk.Frame(self.fr_middle, style="ChatFrame.TFrame")
       for frame in (self.fr_main, self.fr_chatList, self.fr_group, self.fr_chat):
           frame.place(relx=0, rely=0, relwidth=1, relheight=1)


       # ---------------------------
       # 하단 버튼 프레임
       # ---------------------------
       # 높이를 넉넉하게 조정하여 버튼이 잘리지 않도록 함
       self.fr_bottom = ttk.Frame(self, width=400, height=50, style="ChatFrame.TFrame")
       self.fr_bottom.grid(row=2, column=0, sticky="nsew")
       self.fr_bottom.grid_propagate(False)
       self.create_bottom_buttons()


       # 초기 화면: 메인
       self.show_main()


   def create_top_frame(self):
       """
       상단 사용자 정보와 검색창 영역
       """
       # 사용자 정보 영역
       self.fr_top_user = ttk.Frame(self.fr_top, style="TopFrame.TFrame")
       self.fr_top_user.pack(fill=tk.X, side=tk.TOP)


       # 사진 영역
       self.photo_label = tk.Label(self.fr_top_user, bg="#2F2F2F", relief="ridge")
       self.photo_label.pack(side=tk.LEFT, padx=10, pady=5)


       # 사용자 정보 (사원코드, 사원이름)
       self.user_id_var = tk.StringVar(value="사원코드")
       self.user_name_var = tk.StringVar(value="이름")
       text_frame = ttk.Frame(self.fr_top_user, style="TopFrame.TFrame")
       text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       self.lbl_employee = ttk.Label(text_frame, textvariable=self.user_id_var, style="TitleLabel.TLabel")
       self.lbl_employee.pack(anchor="w")
       self.lbl_name = ttk.Label(text_frame, textvariable=self.user_name_var, style="SubTitleLabel.TLabel")
       self.lbl_name.pack(anchor="w")


       # 검색창 영역
       self.fr_top_search = ttk.Frame(self.fr_top, style="SearchFrame.TFrame")
       self.fr_top_search.pack(fill=tk.BOTH, expand=True, side=tk.TOP)


       # ★ tk.Button으로 변경해서 하늘색 적용
       self.search_entry = ttk.Entry(self.fr_top_search, style="Search.TEntry")
       self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)


       self.search_btn = tk.Button(
           self.fr_top_search,
           text="🔍",
           font=("맑은 고딕", 12, "bold"),
           bg="#87CEEB",       # 하늘색
           fg="#FFFFFF",
           activebackground="#87CEFA",
           command=self.search_employees
       )
       self.search_btn.pack(side=tk.RIGHT, padx=10, pady=10)


   def update_top_info(self, img):
       """
       로그인 후 사용자 정보와 사진 업데이트
       """
       # print(img)
       # if type(img) == ImageTk.PhotoImage:
       #     img = img.zoom(4).subsample(7)
       # else:
       #     img = img.resize((40, 40))

       self.user_id_var.set(self.root.get_user_id())
       self.user_name_var.set(self.root.get_user_name())
       # self.photo_label.config(image=self.root.im_info)
       print(img)
       self.photo_label.config(image=img)


   def create_bottom_buttons(self):
       """
       하단의 [메인], [채팅방목록], [채팅방 만들기] 버튼 생성 (tk.Button으로 하늘색)
       """
       for widget in self.fr_bottom.winfo_children():
           widget.destroy()


       btn_main = tk.Button(
           self.fr_bottom,
           text="메인",
           font=("맑은 고딕", 12, "bold"),
           bg="#87CEEB",          # 하늘색
           fg="#FFFFFF",
           activebackground="#87CEFA",
           command=self.show_main
       )
       btn_chatList = tk.Button(
           self.fr_bottom,
           text="채팅방목록",
           font=("맑은 고딕", 12, "bold"),
           bg="#87CEEB",
           fg="#FFFFFF",
           activebackground="#87CEFA",
           command=self.show_chatlist
       )
       btn_group = tk.Button(
           self.fr_bottom,
           text="채팅방 만들기",
           font=("맑은 고딕", 12, "bold"),
           bg="#87CEEB",
           fg="#FFFFFF",
           activebackground="#87CEFA",
           command=self.show_group
       )


       btn_main.grid(row=0, column=0, sticky="nsew", padx=1, pady=5)
       btn_chatList.grid(row=0, column=1, sticky="nsew", padx=1, pady=5)
       btn_group.grid(row=0, column=2, sticky="nsew", padx=1, pady=5)


       for i in range(3):
           self.fr_bottom.columnconfigure(i, weight=1)
       self.fr_bottom.rowconfigure(0, weight=1)


   def show_main(self):
       self.fr_main.lift()
       req = {"code": 85010, "args": {"사원이름": self.search_entry.get()}}
       self.send_(json.dumps(req, ensure_ascii=False))


   def show_chatlist(self):
       self.fr_chatList.lift()
       req = {"code": 85014, "args": {}}
       self.send_(json.dumps(req, ensure_ascii=False))


   def show_group(self):
       self.fr_group.lift()
       self.update_group()


   def show_chat(self, room_id, chat_target):
       self.current_room_id = int(room_id)
       self.current_chat_target = chat_target
       self.fr_chat.lift()
       self.update_chat()
       self.load_chat_history()
       self.chat_history.see("end")


   def update_main(self, employees=None):
       for widget in self.fr_main.winfo_children():
           widget.destroy()
       container = ttk.Frame(self.fr_main, style="ChatFrame.TFrame")
       container.pack(fill=tk.BOTH, expand=True)
       tree = ttk.Treeview(container, columns=("이름", "부서", "직급"), show="headings")
       tree.heading("이름", text="이름")
       tree.heading("부서", text="부서")
       tree.heading("직급", text="직급")
       tree.column("이름", width=80, anchor="center")
       tree.column("부서", width=80, anchor="center")
       tree.column("직급", width=80, anchor="center")
       tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
       scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       tree.configure(yscrollcommand=scrollbar.set)
       data = employees if employees is not None else employees_data
       for emp in data:
           tree.insert("", tk.END, values=(emp.get("사원명"), emp.get("소속부서"), emp.get("직급")))
       tree.bind("<Double-1>", lambda e: self.open_one_to_one_chat(tree))


   def search_employees(self):
       self.show_main()


   def open_one_to_one_chat(self, tree):
       selected = tree.selection()
       if selected:
           values = tree.item(selected[0], "values")
           target_emp_code = values[0]
           personal_room_name = f"개인톡: {values[1]}"
           existing = [room for room in chatrooms_data if room.get("room_name") == personal_room_name]
           if existing:
               room_id = existing[0].get("room_id")
               self.show_chat(room_id, personal_room_name)
           else:
               req = {
                   "code": 85012,
                   "args": {
                       "room_name": personal_room_name,
                       "members": [target_emp_code, self.root.id_]
                   }
               }
               self.send_(json.dumps(req, ensure_ascii=False))


   def update_group(self):
       for widget in self.fr_group.winfo_children():
           widget.destroy()
       lbl = tk.Label(self.fr_group, text="단체 채팅방 만들기 - 초대할 사람 선택",
                      font=('맑은 고딕', 12, 'bold'), bg=Color.WHITE, fg=Color.BLACK)
       lbl.pack(pady=5)
       self.custom_room_name_entry = tk.Entry(self.fr_group, font=('맑은 고딕', 10), width=30, relief=tk.GROOVE, bd=1)
       self.custom_room_name_entry.insert(0, "단체방 이름을 입력하세요")
       self.custom_room_name_entry.bind("<FocusIn>", self.clear_placeholder)
       self.custom_room_name_entry.bind("<FocusOut>", self.add_placeholder)
       self.custom_room_name_entry.pack(pady=5)
       container = tk.Frame(self.fr_group, bg=Color.WHITE, height=300, width=300)
       container.pack(pady=5)
       container.pack_propagate(False)
       canvas = tk.Canvas(container, bg=Color.WHITE, highlightthickness=0, width=280)
       canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
       scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       canvas.configure(yscrollcommand=scrollbar.set)
       inner_frame = tk.Frame(canvas, bg=Color.WHITE)
       canvas.create_window((0, 0), window=inner_frame, anchor="nw")
       def on_configure(event):
           canvas.configure(scrollregion=canvas.bbox("all"))
       inner_frame.bind("<Configure>", on_configure)
       self.group_vars = {}
       for emp in employees_data:
           var = tk.IntVar()
           self.group_vars[emp["사원코드"]] = var
           chk = tk.Checkbutton(inner_frame, text=f"{emp['사원명']} ({emp['소속부서']})",
                                variable=var, bg=Color.WHITE, fg=Color.BLACK)
           chk.pack(anchor="w", padx=10)
       btn_create = ttk.Button(self.fr_group, text="채팅방 만들기", style="Main.TButton", command=self.create_group_chat)
       btn_create.pack(pady=10)


   def clear_placeholder(self, event):
       if self.custom_room_name_entry.get() == "단체방 이름을 입력하세요":
           self.custom_room_name_entry.delete(0, tk.END)


   def add_placeholder(self, event):
       if not self.custom_room_name_entry.get():
           self.custom_room_name_entry.insert(0, "단체방 이름을 입력하세요")


   def create_group_chat(self):
       selected_members = [emp["사원코드"] for emp in employees_data if self.group_vars[emp["사원코드"]].get() == 1]
       if self.root.id_ not in selected_members:
           selected_members.append(self.root.id_)
       if not selected_members:
           messagebox.showwarning("경고", "초대할 사람을 선택하세요.")
           return
       custom_name = ""
       if hasattr(self, "custom_room_name_entry"):
           custom_name = self.custom_room_name_entry.get().strip()
           if custom_name == "단체방 이름을 입력하세요":
               custom_name = ""
       if custom_name:
           room_name = custom_name
       else:
           first_member_code = selected_members[0]
           first_member_name = None
           for emp in employees_data:
               if emp.get("사원코드") == first_member_code:
                   first_member_name = emp.get("사원명")
                   break
           if first_member_name is None:
               first_member_name = first_member_code
           if len(selected_members) > 1:
               room_name = f"단체방: {first_member_name} (외 {len(selected_members) - 1}명)"
           else:
               room_name = f"단체방: {first_member_name}"
       req = {
           "code": 85012,
           "args": {
               "room_name": room_name,
               "members": selected_members
           }
       }
       self.send_(json.dumps(req, ensure_ascii=False))


   def update_chatlist(self):
       for widget in self.fr_chatList.winfo_children():
           widget.destroy()
       container = ttk.Frame(self.fr_chatList, style="ChatFrame.TFrame", height=300)
       container.pack(fill=tk.BOTH, expand=True)
       container.pack_propagate(False)
       tree = ttk.Treeview(container, columns=("room_id", "채팅방", "마지막 메시지"), show="headings")
       tree.heading("채팅방", text="채팅방")
       tree.heading("마지막 메시지", text="마지막 메시지")
       tree.column("room_id", width=0, stretch=False)
       tree.column("채팅방", width=150, anchor="center")
       tree.column("마지막 메시지", width=200, anchor="center")
       tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
       scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       tree.configure(yscrollcommand=scrollbar.set)
       data = chatrooms_data if chatrooms_data else []
       filtered_data = []
       for room in data:
           members = room.get("members")
           if isinstance(members, str):
               try:
                   members_list = json.loads(members)
               except Exception as e:
                   print("멤버 파싱 오류:", e)
                   members_list = []
           else:
               members_list = members
           if self.root.id_ in members_list:
               filtered_data.append(room)
       for room in filtered_data:
           tree.insert("", tk.END, values=(room.get("room_id"), room.get("room_name"), room.get("last_message")))
       tree.bind("<Double-1>", lambda e: self.open_group_chat(tree))


   def open_group_chat(self, tree):
       selected = tree.selection()
       if selected:
           item = tree.item(selected[0], "values")
           room_id = item[0]
           room_name = item[1]
           req_join = {
               "code": 85015,
               "args": {
                   "room_id": int(room_id),
                   "employee_code": self.root.id_
               }
           }
           self.send_(json.dumps(req_join, ensure_ascii=False))
           self.show_chat(room_id, room_name)


   def update_chat(self):
       for widget in self.fr_chat.winfo_children():
           widget.destroy()
       self.fr_chat.grid_rowconfigure(0, weight=0)
       self.fr_chat.grid_rowconfigure(1, weight=1)
       self.fr_chat.grid_rowconfigure(2, weight=0)
       self.fr_chat.grid_columnconfigure(0, weight=1)
       header_frame = ttk.Frame(self.fr_chat, style="ChatFrame.TFrame")
       header_frame.grid(row=0, column=0, sticky="nsew", pady=5)
       lbl = ttk.Label(header_frame, text=f"채팅: {self.current_chat_target}",
                       style="TitleLabel.TLabel")
       lbl.pack(side=tk.LEFT, padx=10)
       btn_leave = ttk.Button(header_frame, text="나가기", style="Main.TButton", command=self.leave_chat)
       btn_leave.pack(side=tk.RIGHT, padx=10)
       text_frame = ttk.Frame(self.fr_chat, style="ChatFrame.TFrame")
       text_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
       text_frame.grid_rowconfigure(0, weight=1)
       text_frame.grid_columnconfigure(0, weight=1)
       self.chat_history = tk.Text(text_frame, font=('맑은 고딕', 12),
                                   state="disabled", bg=Color.WHITE, fg=Color.BLACK, wrap="word")
       self.chat_history.grid(row=0, column=0, sticky="nsew")
       scrollbar = ttk.Scrollbar(text_frame, command=self.chat_history.yview)
       scrollbar.grid(row=0, column=1, sticky="ns")
       self.chat_history['yscrollcommand'] = scrollbar.set
       chat_input_frame = ttk.Frame(self.fr_chat, style="ChatFrame.TFrame", height=40)
       chat_input_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
       chat_input_frame.grid_propagate(False)
       self.chat_input = ttk.Entry(chat_input_frame, font=('맑은 고딕', 12))
       self.chat_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
       self.chat_input.bind("<Return>", self.sendMessage)
       send_btn = ttk.Button(chat_input_frame, text="전송", style="Main.TButton", command=self.sendMessage)
       send_btn.pack(side=tk.RIGHT, padx=5)


   def sendMessage(self, event=None):
       message = self.chat_input.get().strip()
       if message:
           self.chat_input.delete(0, tk.END)
           self.append_message(self.root.name, message)
           req = {
               "code": 75013,
               "args": {
                   "room_id": self.current_room_id,
                   "sender_id": self.root.id_,
                   "sender_name": self.root.name,
                   "message": message
               }
           }
           self.send_(json.dumps(req, ensure_ascii=False))
           self.chat_history.see("end")
       else:
           return


   def leave_chat(self):
       req = {
           "code": 85017,
           "args": {
               "room_id": self.current_room_id,
               "employee_code": self.root.id_
           }
       }
       self.send_(json.dumps(req, ensure_ascii=False))
       messagebox.showinfo("알림", "채팅방에서 나갔습니다.")
       self.show_chatlist()


   def append_message(self, sender, message):
       self.chat_history.config(state="normal")
       self.chat_history.insert(tk.END, f"{sender}: {message}\n")
       self.chat_history.see("end")
       self.chat_history.config(state="disabled")


   def load_chat_history(self):
       req = {"code": 85016, "args": {"room_id": self.current_room_id}}
       self.send_(json.dumps(req, ensure_ascii=False))


   def send_(self, msg):
       try:
           self.root.send_(msg)
       except Exception as e:
           print(traceback.format_exc())
           print(e)


   def recv(self, **kwargs):
       code = kwargs.get("code")
       sign = kwargs.get("sign")
       data = kwargs.get("data")
       if code == 85012:
           if sign == 1:
               messagebox.showinfo("채팅방 생성", "채팅방이 생성되었습니다.")
               req = {"code": 85014, "args": {}}
               self.send_(json.dumps(req, ensure_ascii=False))
           else:
               messagebox.showerror("채팅방 생성 실패", str(data))
       elif code == 85013:
           if sign == 1:
               inner_data = data
               try:
                   received_room_id = int(inner_data.get("room_id"))
               except Exception as e:
                   print("room_id 변환 오류:", e)
                   return
               if received_room_id != self.current_room_id:
                   return
               if inner_data.get("sender_id") == self.root.id_:
                   return
               self.append_message(inner_data.get("sender_name"), inner_data.get("message"))
               self.chat_history.see("end")
               self.show_chat(self.current_room_id, self.current_chat_target)
           else:
               messagebox.showerror("채팅 전송 실패", str(data))
       elif code == 85014:
           if sign == 1 and data:
               global chatrooms_data
               chatrooms_data = data
               self.update_chatlist()
           else:
               messagebox.showinfo("알림", "채팅방 목록 조회 실패")
       elif code == 85010:
           if sign == 1:
               global employees_data
               employees_data = data
               self.update_main()
           else:
               messagebox.showinfo("알림", "직원 목록 조회 실패")
       elif code == 85016:
           if sign == 1:
               self.chat_history.config(state="normal")
               self.chat_history.delete("1.0", tk.END)
               for msg in data:
                   sender_name = msg.get("sender_name")
                   message = msg.get("message")
                   self.chat_history.insert(tk.END, f"{sender_name}: {message}\n")
               self.chat_history.config(state="disabled")
           else:
               messagebox.showinfo("알림", "채팅 내역 조회 실패")


# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title("Chatting Application")
#     root.geometry("400x800")
#
#     # 예시로, 메인 쪽에 사진 객체를 만들어 둔다.
#     # 실제 PNG/GIF 파일 경로로 변경. JPG는 tk.PhotoImage로 안 됩니다.
#     try:
#         root.im_info = tk.PhotoImage(file="your_image.png")
#     except Exception as e:
#         print("이미지 로드 실패:", e)
#         root.im_info = None
#
#     # 사용자 정보 설정
#     root.id_ = "001"
#     root.name = "John Doe"
#     root.get_user_id = lambda: root.id_
#     root.get_user_name = lambda: root.name
#
#     # 가짜 send_ 함수
#     def dummy_send(msg):
#         print("전송된 메시지:", msg)
#     root.send_ = dummy_send
#
#     chat_frame = ChattingFrame(root, None)
#     chat_frame.pack(fill="both", expand=True)
#     chat_frame.update_top_info()  # 로그인 후 사용자 정보와 사진 업데이트
#
#     root.mainloop()



