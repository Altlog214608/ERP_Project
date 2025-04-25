import json
import threading
lock = threading.Lock()

# class User:
#     def __init__(self, req, id_, name):
#         self.req = req
#         self.id = id_
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.req} {self.id} {self.name}"
#
# class Room:
#     def __init__(self):
#         self.users = {} # user_id : User
#
#     def add_user(self, user):
#         self.users[user.id] = user
#
# class UserManager:
#     def __init__(self, dbm):
#         self.dbm = dbm
#         self.users = {} # (online users) user_id : User
#         self.rooms = {} # (on+offline users) room_id : Room
#
#         info = self.dbm.query("SELECT employee.employee_code, employee.name, chat_room.room_code from employee left outer join chat_room on employee.employee_code = chat_room.employee_code")
#         if not info:
#             return
#         for i in info:
#             code = i[0]
#             name = i[1]
#             room = i[2]
#
#             if code not in self.users:
#                 self.users[code] = User(None, code, name)
#
#             if room not in self.rooms:
#                 self.rooms[room] = Room()
#             self.rooms[room].add_user(self.users[code])
#
#         # print(self.users)
#         # print(self.rooms)
#         # todo: new user
#
#     def login(self, req, user_id, name):
#         if not user_id in self.users:
#             return False
#
#         if self.users[user_id].req is not None:
#             return False
#
#         self.users[user_id].req = req
#         self.users[user_id] = User(req, user_id, name)
#
#         return True
#
#     def logout(self, user_id):
#         if not user_id in self.users:
#             return
#
#         self.users[user_id].req = None
#
#     def send_to(self, user_id, msg):
#         if user_id not in self.users:
#             return
#         req = self.users[user_id].req
#         print("send to:", user_id, msg)
#         self.send_(req, msg)
#
#     def send_to_all(self, msg):
#         for user in self.users:
#             self.send_(user.req, msg)
#
#     def send_to_room(self, room_id, msg):
#         users = self.rooms[room_id].users
#         for user in users:
#             if user.req is not None:
#                 self.send_(user.req, msg)
#
#     def send_(self, req, msg):
#         if req is None:
#             return
#         encoded = msg.encode()
#         req.send(str(len(encoded)).ljust(16).encode())
#         req.send(encoded)



class UserManager:
    def __init__(self, dbm):
        self.dbm = dbm
        self.users = {}  # { request_id : User }
        self.rooms = {}  # { room_id : Room }
        test_result = dbm.query(
            """
                             SELECT cr.room_id, cr.room_name, cr.created_at,
                            (SELECT cm.message FROM chat_messages cm 
                             WHERE cm.room_id = cr.room_id 
                             ORDER BY cm.send_time DESC LIMIT 1) AS last_message,
                            cr.members
                     FROM chat_rooms cr
                     ORDER BY cr.created_at DESC
            """
        )

        for row in test_result:
            room_id = row[0]
            room_name = row[1]
            room_created_at = row[2]
            room_last_message = row[3]
            room_members = json.loads(row[4])

            self.rooms[room_id] = Room(room_id, room_name)

            for user in room_members:
                if user not in self.users:
                    self.users[user] = User(user, None)

                self.rooms[room_id].add_user(self.users[user])
        # print(self.users.keys())
        # self.rooms["all"] = Room("all", "전체 채팅방")
        # self.rooms = test_result
        # print(self.rooms)

    def login(self, request_id, employee_code, sock=None):
        """
        로그인 기능:
        - request_id를 기준으로 User 객체를 생성/갱신
        """
        # print(self.users.keys())
        # 만약 이미 해당 request_id가 있으면 갱신, 없으면 새 객체 생성
        if request_id not in self.users:
            user = User(request_id, sock)
            self.users[request_id] = user
        else: # 중복 로그인
            user = self.users[request_id]
            # 소켓 정보 업데이트
            if sock:
                user.sock = sock
            # return False
        # 예시로, 이름은 "User {employee_code}"로 설정합니다.
        user.login(employee_code, f"User {employee_code}")
        return {"sign": 1, "data": {"id": user.id, "name": user.name}}
        # return True

    def logout(self, user_id):
        if not user_id in self.users:
            return

        self.users[user_id].sock = None

    def join_room(self, request_id, employee_code, room_id):
        """
        채팅방 참여
        """
        if request_id not in self.users:
            return {"sign": 0, "data": "사용자가 로그인되어 있지 않습니다."}
        user = self.users[request_id]
        # 만약 방이 없으면 새로 생성합니다.
        if room_id not in self.rooms:
            self.rooms[room_id] = Room(room_id, f"Room {room_id}")
        room = self.rooms[room_id]
        room.add_user(user)
        return {"sign": 1, "data": f"{employee_code}가 방 {room_id}에 참여했습니다."}

    def send_to(self, request_id, msg):
        if request_id not in self.users:
            return
        sock = self.users[request_id].sock
        self.send_(sock, msg)

    @staticmethod
    def send_(req, msg):
        if req is None:
            return
        encoded = msg.encode()
        req.send(str(len(encoded)).ljust(16).encode())
        req.send(encoded)


    def broadcast_room(self, room_id, msg):
        """
        특정 채팅방에 속한 모든 사용자에게 msg를 전송합니다.
        """
        print("지금 룸아이디:", room_id)
        print("있는 방들:", self.rooms)

        if room_id not in self.rooms:
            print("broadcast_room: 해당 방이 없습니다.")
            return
        room = self.rooms[room_id]
        room.send_all(msg)

# Room 클래스: 하나의 채팅방을 관리합니다.
class Room:
    def __init__(self, room_id, room_name, members=None):
        self.room_id = room_id
        self.room_name = room_name
        self.users = []  # 이 방에 연결된 User 객체들
        # members는 채팅방에 참여한 사원 코드들의 리스트
        self.members = members if members is not None else []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        # 멤버 목록에도 추가 (중복되지 않도록)
        if user.id not in self.members:
            self.members.append(user.id)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
        if user.id in self.members:
            self.members.remove(user.id)

    def send_all(self, msg):
        """
        이 방에 연결된 모든 사용자에게 메시지를 전송
        """
        for user in self.users:
            print("test", user, msg)
            if user.sock:
                try:
                    UserManager.send_(user.sock, json.dumps(msg))
                    # user.sock.send(json.dumps(msg).encode())
                except Exception as e:
                    print("Broadcast error to", user.id, ":", e)
            else:
                print(f"Broadcast to {user.id}: {msg}")

class User:
    def __init__(self, req_id, sock=None):
        self.req_id = req_id
        self.id = None
        self.name = None
        self.logged_in = False
        self.sock = sock  # 클라이언트 소켓 연결 (있으면 메시지 전송에 사용)

    def login(self, id_, name):
        self.id = id_
        self.name = name
        self.logged_in = True

    def logout(self):
        self.id = None
        self.name = None
        self.logged_in = False