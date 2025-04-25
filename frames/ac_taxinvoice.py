import tkinter as tk
from tkinter import ttk
import tablewidget
# import naviframe
# import dbManager as dbm
import json
import traceback
import math
import datetime
import tkinter.messagebox as msgbox
from tkinter import font


class TaxInvoiceFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root

        self.jrSendData = {}
        self.currentJrData = [["" for i in range(9)]]

        self.coInfo = {}
        self.clientData = {}
        self.selClientInfo = {}

        self.frameX = 300
        self.frameY = 130

        self.tiFrame = tk.Frame(self, width=1300, height=700)

        # 버튼 기능
        def saveTi():
            rowData = self.tiTable.get_data()
            data = []
            for i in range(len(rowData)):
                if rowData[i][0] != "" and rowData[i][1] != "" and rowData[i][3] != "" and rowData[i][5] != "" and \
                        rowData[i][10] != "":
                    # print("tiTableData :", rowData)
                    # print("rowData[i]",rowData[i])
                    if type(rowData[i][0]) is datetime.date:
                        rowData[i][0] = f"{str(rowData[i][0])}"
                        # print("row",rowData[i])
                    data.append(rowData[i])
                else:
                    pass

            print("save data:", data)
            if self.jrSendData and data:
                # print("save jrdata:",self.jrSendData)
                reqjrsave = {'code': 40206, 'args': self.jrSendData}
                self.send_(reqjrsave)
                reqtisave = {'code': 40202, 'args': {"data": data}}
                self.send_(reqtisave)

            else:
                print("분개 데이터가 없습니다.")
                return  # 함수 종료

        # 발행하기
        def publishTi():
            row = self.tiTable.checked_data()

            if 0 < len(row) <= 1:
                tiId = row[0][10]

                reqpublishTi = {'code': 40203, 'args': {'data': {"작성번호": tiId}}}
                self.send_(reqpublishTi)

        # 세금계산서 프레임
        self.tiY1 = 12  # 조회조건 필드 1행
        self.tiY2 = 32  # 조회조건 필드 2행

        # 조회조건 및 버튼 필드
        self.tiControlFrame = tk.Frame(self.tiFrame, width=1300, height=92)

        self.tiDateLb = tk.Label(self.tiControlFrame, text='작성일자')
        self.tiDateLb.place(x=5, y=self.tiY1)
        self.tiDateEnt = ttk.Entry(self.tiControlFrame, width=10)
        self.tiDateEnt.place(x=60, y=self.tiY1)

        self.tiDateLb2 = tk.Label(self.tiControlFrame, text='~')
        self.tiDateLb2.place(x=140, y=self.tiY1)
        self.tiDateEnt2 = ttk.Entry(self.tiControlFrame, width=10)
        self.tiDateEnt2.place(x=155, y=self.tiY1)

        self.tiStatusLb = tk.Label(self.tiControlFrame, text='발행상태')
        self.tiStatusLb.place(x=690, y=self.tiY1)
        self.tiStatusItem = ['', '발행']
        self.tiStatusCbbox = ttk.Combobox(self.tiControlFrame, width=4, values=self.tiStatusItem)
        self.tiStatusCbbox.place(x=750, y=self.tiY1)
        self.tiClientLb = tk.Label(self.tiControlFrame, text='거래처')
        self.tiClientLb.place(x=390, y=self.tiY1)
        self.tiClientEnt = ttk.Entry(self.tiControlFrame, width=8)
        self.tiClientEnt.place(x=435, y=self.tiY1)
        self.tiClientEnt.bind('<F2>', lambda e: self.drawScTable('client','cont'))

        self.tiClientContent = ttk.Entry(self.tiControlFrame, width=25)
        self.tiClientContent.place(x=500, y=self.tiY1)

        self.tiTypeLb = tk.Label(self.tiControlFrame, text='작성유형')
        self.tiTypeLb.place(x=240, y=self.tiY1)
        self.tiTypeItem = ['', '매출', '매입']
        self.tiTypeCbbox = ttk.Combobox(self.tiControlFrame, width=8, values=self.tiTypeItem)
        self.tiTypeCbbox.place(x=300, y=self.tiY1)
        self.tiIdLb = tk.Label(self.tiControlFrame, text='세금계산서 작성번호')
        self.tiIdLb.place(x=810, y=self.tiY1)
        self.tiIdEnt = ttk.Entry(self.tiControlFrame, width=20)
        self.tiIdEnt.place(x=930, y=self.tiY1)

        self.tiSearchBtn = ttk.Button(self.tiControlFrame, text='조회하기', command=self.searchBtn)
        self.tiSearchBtn.place(x=1200, y=10)

        self.tiSaveBtn = ttk.Button(self.tiControlFrame, text='저장하기', command=saveTi)
        self.tiSaveBtn.place(x=1200, y=37)

        self.tiPublishBtn = ttk.Button(self.tiControlFrame, text='발행하기', command=publishTi)
        self.tiPublishBtn.place(x=1200, y=64)
        self.tiControlFrame.pack()

        # 세금계산서 필드
        self.tiTableFrame = tk.Frame(self.tiFrame, width=1300, height=330)

        # DB 데이터 불러올곳
        # after init
        self.tiData = [["" for i in range(11)]]

        self.tiTable = tablewidget.TableWidget(self.tiTableFrame,
                                               data=self.tiData,
                                               col_name=["작성일자", "유형", "거래처명", "사업자번호", "적요", "공급가액", "세율", "세액", "합계액",
                                                         "발행여부", "작성번호"],
                                               col_width=[80, 40, 170, 100, 230, 110, 60, 110, 110, 70, 129],
                                               col_align=['center', 'center', 'left', 'center', 'left', 'right',
                                                          'center', 'right', 'right', 'center', 'center'],
                                               editable=[True, True, True, True, True, True, False, True, False, False,
                                                         False],
                                               width=1300, height=330, padding=10)
        self.tiTable.place(x=0, y=0)
        self.tiTable.bind('<Key>', lambda e: self.onTiTableKey(e))
        self.tiTableFrame.pack()

        # 분개 필드
        self.jrTableFrame = tk.Frame(self.tiFrame, width=1300, height=273)
        self.jrTableFrame.pack()
        self.tiFrame.pack()
        # self.place(x=self.frameX, y=self.frameY)

    def after_init(self):
        # 세금계산서 데이터 처음 불러오기
        reqtidata = {'code': 40201, 'args': {}}
        self.send_(reqtidata)
        # 회사 정보 불러오기
        reqcoinfo = {'code': 10103, 'args': {}}
        self.send_(reqcoinfo)

    def send_(self, data):
        self.root.send_(json.dumps(data, ensure_ascii=False))
        # self.send_test(json.dumps(data, ensure_ascii=False))

    # 서버 없이 인코딩 디코딩 잘되는지 테스트용
    # def send_test(self, msg):
    #     try:
    #         encoded = msg.encode()
    #         # print(str(len(encoded)).ljust(16).encode())
    #         # print(encoded)
    #         self.recv_data(encoded)
    #     except Exception as e:
    #         print(traceback.format_exc())
    #         # print(e)
    #
    # def recv_data(self, data):
    #     r = json.loads(data.decode())
    #     if type(r) is str:
    #         r = json.loads(r)
    #     print("recv r:", r)
    #     code = r['code']
    #     args = r['args']
    #     result = {}
    #     if code == 40201:
    #         result = TaxInvoiceFrame.f40201(**args)
    #         result['code'] = code
    #
    #     elif code == 40202:
    #         result = TaxInvoiceFrame.f40202(**args)
    #         result['code'] = code
    #
    #     elif code == 40203:
    #         result = TaxInvoiceFrame.f40203(**args)
    #         result['code'] = code
    #
    #     elif code == 40204:
    #         result = TaxInvoiceFrame.f40204(**args)
    #         result['code'] = code
    #
    #     elif code == 40205:
    #         result = TaxInvoiceFrame.f40205(**args)
    #         result['code'] = code
    #
    #     elif code == 40206:
    #         result = TaxInvoiceFrame.f40206(**args)
    #         result['code'] = code
    #
    #     elif code == 40207:
    #         result = TaxInvoiceFrame.f40207(**args)
    #         result['code'] = code
    #
    #     # print(result)
    #     self.recv(**result)

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

    # 이거만 살려두면 됨
    def recv(self, **kwargs):
        code = kwargs.get('code')
        data = kwargs.get('data')
        sign = kwargs.get('sign')
        # print("code :", code)
        # print("data =", data)
        # print("sign :", sign)
        # 세금계산서 조회
        if code == 40201 and sign == 1:
            def formatting(text):
                if "-" in text:
                    text.replace("-", "")
                    return text
                else:
                    t = ""
                    t += f"{text[:3]}-"
                    t += f"{text[3:5]}-"
                    t += f"{text[5:]}"
                    return t

            # print(f"{code} data:",data)
            if data:
                titdata = data
                tmpdata = []
                for i in range(len(titdata)):
                    row = titdata[i]
                    # print("row data",row)
                    for j in range(len(row)):
                        if type(row[j]) == datetime.date:
                            pass
                        else:
                            if row[j] == "None" or row[j] is None or row[j] == 0:
                                row[j] = ""
                    tmp = [row[1], row[2], row[3], formatting(row[4]), row[6], format(int(row[7]), ","), "10%",
                           format(int(row[9]), ","), format(int(row[10]), ","), row[11], row[0]]
                    # print("tmp :",tmp)
                    tmpdata.append(tmp)

                titdata = tmpdata
                # print("titdata :",titdata)
                self.tiData = titdata
            else:
                self.tiData = [["" for i in range(11)] for j in range(6)]

            self.tiTable.refresh(self.tiData)


        # 세금계산서 저장
        elif code == 40202 and sign == 1:
            # print(f"{code} recv:", data)
            self.searchBtn()

        # 세금계산서 발행
        elif code == 40203 and sign == 1:
            # print(f"{code} recv:", data)
            self.searchBtn()

        # 세금계산서 삭제
        elif code == 40204 and sign == 1:
            # print(f"{code} recv:", data)
            tabledata = self.tiTable.checked_data()
            if tabledata:
                keys = []
                for i in range(len(tabledata)):
                    if tabledata[i][10] != "" and tabledata[i][9] != "발행":
                        keys.append(tabledata[i][10])

                reqdeljr = {'code': 40207, 'args': {'data': keys}}
                self.send_(reqdeljr)
            self.searchBtn()

        # 세금계산서 분개조회
        elif code == 40205 and sign == 1:
            print(f"{code} recv:", data)
            if data:
                jrtdata = data
                tmpData = []
                for i in range(len(jrtdata)):
                    row = jrtdata[i]
                    row.pop(0)
                    row.pop(-1)
                    row.pop(-1)
                    row.pop(-1)
                    for j in range(len(row)):
                        if row[j] == "None" or row[j] is None or row[j] == 0 or row[j] == "0":
                            row[j] = ""
                    # print(row)
                    cr = ""
                    dr = ""
                    if row[5] != "":
                        cr = format(int(row[5]), ",")
                    elif row[6] != "":
                        dr = format(int(row[6]), ",")

                    tmp = [row[0], row[1], row[2], "", row[3], cr, dr, row[7], row[8]]
                    tmpData.append(tmp)

                jrtdata = tmpData
                # print("jrtdata :", jrtdata)
                self.currentJrData = jrtdata
            else:
                self.currentJrData = [["" for i in range(9)]]

            self.jrTable.refresh(self.currentJrData)

        # 세금계산서 분개저장
        elif code == 40206 and sign == 1:
            pass

        # 세금계산서 분개삭제
        elif code == 40207 and sign == 1:
            # print(f"{code} recv:", data)
            self.searchBtn()

        elif code == 40702 and sign == 1:
            if data:
                self.scData = data
            else:
                self.scData = [["", "", ""]]

            self.scTable.refresh(self.scData)

        elif code == 30102 and sign == 1:
            self.clientData = data
            self.scTable.refresh(self.clientData)

        elif code == 10103 and sign==1:
            self.coInfo = data
            # print("10103 data:",self.coInfo)

    def drawJrFrame(self, tiId):
        # # DB 데이터 불러올곳
        # self.jrData = [["차변", "101", "현금", "00001", "이상한과자가게전천당", 3300000, "", "과자팔아서돈들어옴", "세금계산서"],
        #                ["대변", "401", "매출", "00001", "이상한과자가게전천당", "", 3000000, "과자팔아서돈들어옴", "세금계산서"],
        #                ["대변", "301", "부가세예수금", "07000", "국세청", "", 300000, "부가세예수금", "세금계산서"]
        #                ]

        # print("jrdata f40201 :",d)

        self.jrData = self.currentJrData

        # 테이블 출력 및 설정
        self.jrTable = tablewidget.TableWidget(self.jrTableFrame,
                                               data=self.jrData,
                                               col_name=["구분", "계정코드", "계정과목명", "거래처코드", "거래처명", "차변금액", "대변금액", "적요",
                                                         "증빙"],
                                               col_width=[50, 80, 130, 90, 170, 170, 170, 259, 90],
                                               col_align=['center', 'center', 'left', 'center', 'left', 'right',
                                                          'right', 'left', 'center'],
                                               width=1300, height=240,padding=10)
        self.jrTable.place(x=0, y=0)
        reqtijrdata = {'code': 40205, 'args': {"세금계산서번호": tiId}}
        self.send_(reqtijrdata)

        self.jrTable.bind('<Key>', lambda e: self.onJrTableKey(e))

    def getTiCond(self):
        result = {}
        result['시작일자'] = self.tiDateEnt.get()
        result['종료일자'] = self.tiDateEnt2.get()
        result['작성유형'] = self.tiTypeCbbox.get()
        result['발행상태'] = self.tiStatusCbbox.get()
        result['작성번호'] = self.tiIdEnt.get()
        return result

    def searchBtn(self):
        cond = self.getTiCond()

        reqtitdata = {'code': 40201, 'args': cond}
        self.send_(reqtitdata)

    # 현재 포커스된 행의 데이터 받아오기
    def getRow(self, table):
        if table == "ti":
            return self.tiTable.data[self.tiTable.get_key(self.tiTable.selected_row)]
        elif table == "jr":
            return self.jrTable.data[self.jrTable.get_key(self.jrTable.selected_row)]
        elif table == "sc":
            return self.scTable.data[self.scTable.get_key(self.scTable.selected_row)]

    # 내가 지정한 열의 데이터 받아오기
    def getCol(self, table, colIndex):
        colData = []
        if table == "ti":
            for i in range(len(self.tiTable.get_data())):
                colData.append(self.tiTable.get_data()[i][colIndex])
            return colData

        elif table == "jr":
            for i in range(len(self.jrTable.get_data())):
                colData.append(self.jrTable.get_data()[i][colIndex])
            return colData

    # 세금계산서 테이블 에서 F3 누르면 분개필드 출력 및 세금계산서번호 생성
    def onTiTableKey(self, e):
        # F3
        if e.keycode == 114:
            rowData = self.getRow('ti')['data']
            if rowData[0] == "" or rowData[1] == "" or rowData[2] == "" or rowData[3] == "" or rowData[5] == "":
                print("작성일자, 유형, 거래처명, 사업자번호, 공급가액 중 입력되지 않은 값이 있습니다.")
                msgbox.showerror("오류",
                                 "작성일자, 유형, 사업자번호, 공급가액 중 입력되지 않은 값이 있습니다.\n yyyy-mm-dd, 매출or매입, nnn-nn-nnnnn, 숫자 형식으로 입력해주세요")

                if len(rowData[3].replace('-', "")) != 10:
                    print("사업자번호 형식 오류")

                try:
                    self.currentJrData = [["" for i in range(9)]]
                    self.jrTable.place_forget()
                except:
                    pass

            else:
                tiId = ""
                date = str(rowData[0])
                if '-' in date: tiId += date.replace('-', "")
                if rowData[1] == "매출":
                    tiId += "11"
                elif rowData[1] == "매입":
                    tiId += "12"

                colData = self.getCol("ti", 0)
                colData2 = self.getCol("ti", 10)
                tiCount = 1
                for i in range(len(colData)):
                    if colData2[i] == (tiId + str(tiCount).zfill(4)) and rowData[10] != (tiId + str(tiCount).zfill(4)):
                        tiCount += 1
                    elif colData2[i] == (tiId + str(tiCount).zfill(4)) and rowData[10] == (
                            tiId + str(tiCount).zfill(4)):
                        continue

                tiId += str(tiCount).zfill(4)
                taxRate = 0.1
                tax = format(math.trunc(int(rowData[5].replace(',', "")) * taxRate), ',')
                totalAmount = format(int(rowData[5].replace(',', "")) + int(tax.replace(',', "")), ',')

                self.tiTable.data[self.tiTable.get_key(self.tiTable.selected_row)]['data'][6] = "10%"
                self.tiTable.data[self.tiTable.get_key(self.tiTable.selected_row)]['data'][7] = tax
                self.tiTable.data[self.tiTable.get_key(self.tiTable.selected_row)]['data'][8] = totalAmount
                self.tiTable.data[self.tiTable.get_key(self.tiTable.selected_row)]['data'][10] = tiId
                self.tiTable.draw_table()
                # print(self.getRow('ti'))
                # print(int(tax.replace(',',"")),int(totalAmount.replace(',',"")))
                self.drawJrFrame(tiId)

        # f5 누르면 선택된 세금계산서 삭제
        elif e.keycode == 116:
            tabledata = self.tiTable.checked_data()
            if tabledata:
                keys = []
                for i in range(len(tabledata)):
                    if tabledata[i][10] != "" and tabledata[i][9] != "발행":
                        keys.append(tabledata[i][10])

                reqdelti = {'code': 40204, 'args': {'data': keys}}
                self.send_(reqdelti)
            else:
                pass

        # F2
        elif e.keycode == 113:
            selCol = self.tiTable.selected_col
            if selCol == 2 or selCol == 3:
                self.drawScTable('client','ti')

        # F10
        elif e.keycode == 121:
            if self.getRow('ti')['data'][9] == "발행":
                self.selClientInfo

                row = self.getRow('ti')['data']
                print("row :",row)
                # print("coInfo :", self.coInfo)

                data = {'date':row[0],'amount':row[5],'tax':row[7],
                        'desc':row[4],'total':row[8],'tiId':row[10]}
                if row[1] == '매출':
                    data['suplNum'] = self.coInfo["등록번호"]
                    data['suplCom'] = self.coInfo["회사이름"]
                    data['suplName'] = self.coInfo["대표자"]
                    data['supAddr'] = self.coInfo["주소"]
                    data['recvNum'] = row[3]
                    data['recvCom'] = row[2]
                    data['recvName'] = ""
                    data['recvAddr'] = ""
                elif row[1] == '매입':
                    data['suplNum'] = row[3]
                    data['suplCom'] = row[2]
                    data['suplName'] = ""
                    data['supAddr'] = ""
                    data['recvNum'] = self.coInfo["등록번호"]
                    data['recvCom'] = self.coInfo["회사이름"]
                    data['recvName'] = self.coInfo["대표자"]
                    data['recvAddr'] = self.coInfo["주소"]

                self.drawTiPaper(data)
            else:
                pass

    def onJrTableKey(self, e):
        # f4 누르면 해당 세금계산서 유형에 맞게 부가세 분개(구분,계정코드, 계정과목명, 차변 or 대변 금액 적요, 증빙) 들어가짐
        if e.keycode == 115:
            rowData = self.getRow('jr')['data']
            # print("f4 data:",rowData)
            col = []
            base = []
            titabledata = self.getRow('ti')['data']
            if titabledata[1] == '매출':
                col = [0, 1, 2, 6, 8]
                base = ["대변", "255", "부가세예수금", titabledata[7], "세금계산서"]
            elif titabledata[1] == "매입":
                col = [0, 1, 2, 5, 8]
                base = ["차변", "135", "부가세대급금", titabledata[7], "세금계산서"]

            for i in range(len(col)):
                rowData[col[i]] = base[i]

            self.jrTable.draw_table()

        # f3 누르면 현재 분개 데이터 임시로 저장 ( DB는 안감, 저장하기 버튼 눌렀을 때 DB로 저장 )
        elif e.keycode == 114:
            rawData = self.jrTable.get_data()
            data = []
            debit = []
            credit = []
            sendData = {}
            # print(f"data[0]:{rawData}")
            for i in range(len(rawData)):
                if rawData[i][0] == "차변":
                    if (rawData[i][1] != "0" and rawData[i][5] != "0" and rawData[i][6] == "0") or (
                            rawData[i][1] != "" and rawData[i][5] != "" and rawData[i][6] == ""):
                        if "," in str(rawData[i][5]):
                            rawData[i][5] = int(rawData[i][5].replace(",", ""))
                        elif "," in str(rawData[i][6]):
                            rawData[i][6] = int(rawData[i][6].replace(",", ""))
                        data.append(rawData[i])
                        debit.append(rawData[i][5])
                    else:
                        pass

                elif rawData[i][0] == "대변":
                    if (rawData[i][1] != "0" and rawData[i][6] != "0" and rawData[i][5] == "0") or (
                            rawData[i][1] != "" and rawData[i][6] != "" and rawData[i][5] == ""):
                        if "," in str(rawData[i][5]):
                            rawData[i][5] = int(rawData[i][5].replace(",", ""))
                        elif "," in str(rawData[i][6]):
                            rawData[i][6] = int(rawData[i][6].replace(",", ""))
                        data.append(rawData[i])
                        credit.append(rawData[i][6])
                    else:
                        pass
            # print("data:",data)
            debit = [int(i) for i in debit]
            credit = [int(i) for i in credit]
            print(f"차변 : {debit}")
            print(f"대변 : {credit}")
            # print(f"차변합 : {sum(debit)}")
            # print(f"대변합 : {sum(credit)}")
            totalAmount = int((self.getRow('ti')['data'][8]).replace(',', ""))
            if sum(debit) == sum(credit) and sum(debit) == totalAmount:
                tiId = self.getRow("ti")['data'][10]
                for i in range(len(data)):
                    sendData[tiId] = data
                # print(f"sendData : {sendData}")
                self.jrSendData = sendData

            else:
                print("차변과 대변의 합계 또는 값이 올바르지 않습니다.")

        # F2 누르면 계정과목
        elif e.keycode == 113:
            selCol = self.jrTable.selected_col
            if selCol == 1:
                self.drawScTable('subject',"")
            elif selCol == 3:
                self.drawScTable('client',"jr")

    def drawScTable(self, key, cont):
        if key == 'subject':
            # 확인버튼
            def confirm():
                row = self.getRow('sc')['data']
                selRow = self.jrTable.selected_row
                # print("sc row :", row)
                data = self.jrTable.get_data()
                # print("sc data :", data)
                for i in range(len(data)):
                    if i == selRow:
                        data[i][1] = row[0]
                        data[i][2] = row[1]
                    if data[i][0] == "":
                        data.pop(i)

                cancel()
                self.jrTable.refresh(data)

            def cancel():
                self.scFrame.place_forget()
                self.jrTable.focus_set()

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
            self.choiceBtn = ttk.Button(self.scFrame, text='확인', command=confirm)
            self.choiceBtn.place(x=220, y=400)
            self.cancelBtn = ttk.Button(self.scFrame, text='취소', command=cancel)
            self.cancelBtn.place(x=130, y=400)
            self.scFrame.place(x=300, y=70)
            self.scTable.focus_set()
            self.scTable.bind('<Escape>', lambda e: cancel())
            self.scTable.bind('<Button-1>', lambda e: self.scTable.focus_set())
            self.scTable.bind('<Return>', lambda e: confirm())

        elif key == 'client':
            def confirm():
                if cont=='cont':
                    row = self.getRow('sc')['data']
                    # print("row",row)
                    cancel()
                    self.tiClientEnt.delete(0,tk.END)
                    self.tiClientEnt.insert(0,row[0])
                    self.tiClientContent.delete(0,tk.END)
                    self.tiClientContent.insert(0,row[1])

                elif cont=='jr':
                    row = self.getRow('sc')['data']
                    selRow = self.jrTable.selected_row
                    # print("sc row :", row)
                    data = self.jrTable.get_data()
                    # print("sc data :", data)
                    for i in range(len(data)):
                        if i == selRow:
                            data[i][3] = row[0]
                            data[i][4] = row[1]
                        if data[i][0] == "":
                            data.pop(i)

                    cancel()
                    self.jrTable.refresh(data)

                elif cont=='ti':
                    row = self.getRow('sc')['data']
                    selRow = self.tiTable.selected_row
                    data = self.tiTable.get_data()
                    for i in range(len(data)):
                        if i == selRow:
                            data[i][2] = row[1]
                            data[i][3] = row[2]
                        if data[i][0] == "":
                            data.pop(i)
                    cancel()
                    self.tiTable.refresh(data)

            def cancel():
                self.scFrame.place_forget()

            self.scFrame = tk.Frame(self, width=602, height=440, borderwidth=1, relief='solid')
            self.scData = [["", "", "", ""]]
            self.scTable = tablewidget.TableWidget(self.scFrame,
                                                   data=self.scData,
                                                   has_checkbox=False,
                                                   cols=4,
                                                   new_row=False,
                                                   col_name=['거래처코드', '거래처명', '사업자등록번호', '대표자'],
                                                   col_width=[80, 220, 125, 101],
                                                   col_align=['center', 'left', 'center', 'center'],
                                                   editable=[False, False, False, False],
                                                   width=598, height=380, padding=10
                                                   )
            self.scTable.place(x=0, y=0)
            reqsctable = {'code': 30102, 'args': {}}
            self.send_(reqsctable)
            self.choiceBtn = ttk.Button(self.scFrame, text='확인',command=confirm)
            self.choiceBtn.place(x=500, y=400)
            self.cancelBtn = ttk.Button(self.scFrame, text='취소',command=cancel)
            self.cancelBtn.place(x=410, y=400)
            self.scFrame.place(x=300, y=70)
            self.scTable.focus_set()
            self.scTable.bind('<Escape>', lambda e: cancel())
            self.scTable.bind('<Button-1>', lambda e:self.scTable.focus_set())
            self.scTable.bind('<Return>',lambda  e:confirm())

    def drawTiPaper(self,data):
        def cancel():
            self.cvs.place_forget()
            self.tiTable.focus_set()

        cvsWidth = 900
        cvsHeight = 620
        x = 10
        y = 10
        endX = cvsWidth-x
        endY = cvsHeight-y
        midX = (cvsWidth - x) / 2
        midY = (cvsHeight - y) / 2

        print("data :",data)
        # 안에 들어가야 할 정보
        tpinfo = {"tiId": data['tiId'],
                  "suplNum": data['suplNum'], "recvNum":data['recvNum'],
                  "suplCom":data['suplCom'],"recvCom":data['recvCom'],
                  "suplName":data['suplName'],"recvName":data['recvName'],
                  "supAddr":data['supAddr'],"recvAddr":data['recvAddr'],
                  "supBizCond":"","recvBizCond":"",
                  "supBizCond2":"","recvBizCond2":"",
                  "supEmail":"","recvEmail":"",
                  "date":data['date'],"amount":data['amount'],"tax":data['tax'],
                  "desc":data['desc'],"total":data['total']
                  }

        self.cvs = tk.Canvas(self, bg='white', bd=2, width=cvsWidth, height=cvsHeight)
        self.cvs.place(x=160, y=60)

        tpNameFont = font.Font(size=20)
        tpTiIdLbFont = font.Font(size=16)
        tpSubjectFont = font.Font(size=11)

        # 선
        self.cvs.create_rectangle(x, y, endX, endY)  # 전체

        # 머릿글
        self.cvs.create_rectangle(x, y, midX, y + 50)  # 상단
        self.cvs.create_text(x + 210, y + 25, text='세 금 계 산 서', font=tpNameFont)

        # 작성번호
        self.cvs.create_rectangle(midX, y, midX + 150, y + 50)  # 라벨 작성번호
        self.cvs.create_text(midX + 70, y + 25, text='작성번호', font=tpTiIdLbFont)

        self.cvs.create_rectangle(midX + 150, y, endX, y + 50)  # 작성번호 들어갈곳
        self.cvs.create_text(midX + 300, y + 25, text=tpinfo['tiId'], font=tpTiIdLbFont)

        # 상단
        H = 40
        X1 = x + 40
        X2 = X1 + 70
        X3 = X2 + 150
        X4 = X3 + 70

        Y1 = y + 50
        Y2 = Y1 + H
        Y3 = Y2 + H
        Y4 = Y3 + H
        Y5 = Y4 + H
        pX = 8
        self.cvs.create_rectangle(x, Y1, X1, midY)
        self.cvs.create_text(x + 20, y + 110, text='공', font=tpTiIdLbFont)
        self.cvs.create_text(x + 20, y + 160, text='급', font=tpTiIdLbFont)
        self.cvs.create_text(x + 20, y + 210, text='자', font=tpTiIdLbFont)
        self.cvs.create_rectangle(midX, Y1, midX+X1-x, midY)
        self.cvs.create_text(midX + 20, y + 80, text='공', font=tpTiIdLbFont)
        self.cvs.create_text(midX + 20, y + 120, text='급', font=tpTiIdLbFont)
        self.cvs.create_text(midX + 20, y + 160, text='받', font=tpTiIdLbFont)
        self.cvs.create_text(midX + 20, y + 200, text='는', font=tpTiIdLbFont)
        self.cvs.create_text(midX + 20, y + 240, text='자', font=tpTiIdLbFont)
        # 라인 1
        self.cvs.create_rectangle(X1, Y1, X2, Y2)
        self.cvs.create_rectangle(X2, Y1, X3, Y2)
        self.cvs.create_rectangle(X3, Y1, X4, Y2)
        self.cvs.create_rectangle(X4, Y1, midX, Y2)
        self.cvs.create_text(X1 + 35, Y1 + 20, text='등록번호', font=tpSubjectFont)
        self.cvs.create_text(X2 + 75, Y1 + 20, text=tpinfo['suplNum'], font=tpSubjectFont)
        self.cvs.create_text(X3 + 35, Y1 + 12, text='종사업장', font=tpSubjectFont)
        self.cvs.create_text(X3 + 35, Y1 + 27, text='번호', font=tpSubjectFont)
        self.cvs.create_rectangle(midX+X1-x, Y1, midX+X2-x, Y2)
        self.cvs.create_rectangle(midX+X2-x, Y1, midX+X3-x, Y2)
        self.cvs.create_rectangle(midX+X3-x, Y1, midX+X4-x, Y2)
        self.cvs.create_rectangle(midX+X4-x, Y1, endX, Y2)
        self.cvs.create_text(midX-x+X1 + 35, Y1 + 20, text='등록번호', font=tpSubjectFont)
        self.cvs.create_text(midX-x+X2 + 75, Y1 + 20, text=tpinfo['suplNum'], font=tpSubjectFont)
        self.cvs.create_text(midX-x+X3 + 35, Y1 + 12, text='종사업장', font=tpSubjectFont)
        self.cvs.create_text(midX-x+X3 + 35, Y1 + 27, text='번호', font=tpSubjectFont)

        # 라인2
        self.cvs.create_rectangle(X1, Y2, X2, Y3)
        self.cvs.create_rectangle(X2, Y2, X3, Y3)
        self.cvs.create_rectangle(X3, Y2, X4, Y3)
        self.cvs.create_rectangle(X4, Y2, midX, Y3)
        self.cvs.create_text(X1+35,Y2 + 12, text='상호',font=tpSubjectFont)
        self.cvs.create_text(X1 + 35, Y2 + 27, text='(법인명)', font=tpSubjectFont)
        self.cvs.create_text(X2+pX, Y2 + 20, text=tpinfo['suplCom'], font=tpSubjectFont,anchor='w')
        self.cvs.create_text(X3 + 35, Y2 + 20, text='성명', font=tpSubjectFont)
        self.cvs.create_text(X4 + pX, Y2 + 20, text=tpinfo['suplName'], font=tpSubjectFont,anchor='w')
        self.cvs.create_rectangle(midX + X1 - x, Y2, midX + X2 - x, Y3)
        self.cvs.create_rectangle(midX + X2 - x, Y2, midX + X3 - x, Y3)
        self.cvs.create_rectangle(midX + X3 - x, Y2, midX + X4 - x, Y3)
        self.cvs.create_rectangle(midX + X4 - x, Y2, endX, Y3)
        self.cvs.create_text(midX-x+X1 + 35, Y2 + 12, text='상호', font=tpSubjectFont)
        self.cvs.create_text(midX-x+X1 + 35, Y2 + 27, text='(법인명)', font=tpSubjectFont)
        self.cvs.create_text(midX-x+X2+pX, Y2 + 20, text=tpinfo['recvCom'], font=tpSubjectFont,anchor='w')
        self.cvs.create_text(midX-x+X3 + 35, Y2 + 20, text='성명', font=tpSubjectFont)
        self.cvs.create_text(midX-x+X4 + pX, Y2 + 20, text=tpinfo['recvName'], font=tpSubjectFont,anchor='w')

        # 라인3
        self.cvs.create_rectangle(X1, Y3, X2, Y4)
        self.cvs.create_rectangle(X2, Y3, midX, Y4)
        self.cvs.create_text(X1 + 35, Y3 + 20, text='주소', font=tpSubjectFont)
        self.cvs.create_text(X2 + pX, Y3 + 20, text=tpinfo["supAddr"], font=tpSubjectFont, anchor='w')
        self.cvs.create_rectangle(midX-x+X1, Y3, midX-x+X2, Y4)
        self.cvs.create_rectangle(midX-x+X2, Y3, endX, Y4)
        self.cvs.create_text(midX-x+X1 + 35, Y3 + 20, text='주소', font=tpSubjectFont)
        self.cvs.create_text(midX-x+X2 + pX, Y3 + 20, text=tpinfo["recvAddr"], font=tpSubjectFont, anchor='w')

        # 라인4
        l4 = X2+100
        l5 = l4+70
        self.cvs.create_rectangle(X1, Y4, X2, Y5)
        self.cvs.create_rectangle(X2, Y4, l4, Y5)
        self.cvs.create_rectangle(l4, Y4, l5, Y5)
        self.cvs.create_rectangle(l5, Y4, midX, Y5)
        self.cvs.create_text(X1 + 35, Y4 + 20, text='업태', font=tpSubjectFont)
        self.cvs.create_text(X2 + pX, Y4 + 20, text=tpinfo['supBizCond'], font=tpSubjectFont, anchor='w')
        self.cvs.create_text(l4 + 35, Y4 + 20, text='종목', font=tpSubjectFont)
        self.cvs.create_text(l5 + pX, Y4 + 20, text=tpinfo['supBizCond2'],font=tpSubjectFont, anchor='w')
        self.cvs.create_rectangle(midX-x+X1, Y4, midX-x+X2, Y5)
        self.cvs.create_rectangle(midX-x+X2, Y4, midX-x+l4, Y5)
        self.cvs.create_rectangle(midX-x+l4, Y4, midX-x+l5, Y5)
        self.cvs.create_rectangle(midX-x+l5, Y4, endX, Y5)
        self.cvs.create_text(midX-x+X1 + 35, Y4 + 20, text='업태', font=tpSubjectFont)
        self.cvs.create_text(midX-x+X2 + pX, Y4 + 20, text=tpinfo['recvBizCond'], font=tpSubjectFont, anchor='w')
        self.cvs.create_text(midX-x+l4 + 35, Y4 + 20, text='종목', font=tpSubjectFont)
        self.cvs.create_text(midX-x+l5 + pX, Y4 + 20, text=tpinfo['recvBizCond2'], font=tpSubjectFont, anchor='w')

        # 라인5
        self.cvs.create_rectangle(X1, Y5, X2, midY)
        self.cvs.create_rectangle(X2, Y5, midX, midY)
        self.cvs.create_text(X1 + 35, Y5 + 35, text='이메일', font=tpSubjectFont)
        self.cvs.create_text(X2 + pX, Y5 + 35, text=tpinfo['supEmail'], font=tpSubjectFont,anchor='w')
        self.cvs.create_rectangle(midX-x+X1, Y5, midX-x+X2, midY)
        self.cvs.create_rectangle(midX-x+X2, Y5, endX, midY)
        self.cvs.create_text(midX-x+X1 + 35, Y5 + 35, text='이메일', font=tpSubjectFont)
        self.cvs.create_text(midX-x+X2 + pX, Y5 + 35, text=tpinfo['recvEmail'], font=tpSubjectFont, anchor='w')

        # 하단
        bH = 30
        bY1 = midY+ bH
        bY2 = bY1 + bH
        # 라인6
        self.cvs.create_rectangle(x,midY,X2,bY1)
        self.cvs.create_rectangle(X2,midY,X2+160,bY1)
        self.cvs.create_rectangle(X2+160,midY, midX, bY1)
        self.cvs.create_text(x+50, midY+15,text='작성일자',font=tpSubjectFont)
        self.cvs.create_text(X2+80, midY+15,text='공급가액',font=tpSubjectFont)
        self.cvs.create_text(X2+240, midY+15,text='세액',font=tpSubjectFont)

        self.cvs.create_rectangle(midX, midY, midX-x+X2, bY1)
        self.cvs.create_rectangle(midX-x+X2,midY,endX,bY1)
        self.cvs.create_text(midX+50, midY+15, text='수정사유',font=tpSubjectFont)
        self.cvs.create_text(midX+270, midY+15, text='비고',font=tpSubjectFont)

        # 라인7
        self.cvs.create_rectangle(x,bY1,X2,bY2)
        self.cvs.create_rectangle(X2,bY1,X2+160,bY2)
        self.cvs.create_rectangle(X2+160,bY1, midX, bY2)
        self.cvs.create_text(x+pX,bY1+15, text=f"{tpinfo['tiId'][:4]}-{tpinfo['tiId'][4:6]}-{tpinfo['tiId'][6:8]}",font=tpSubjectFont,anchor='w')
        self.cvs.create_text(X2+160-pX, bY1 + 15, text=tpinfo['amount'], font=tpSubjectFont, anchor='e')
        self.cvs.create_text(midX-pX, bY1 + 15, text=tpinfo['tax'], font=tpSubjectFont, anchor='e')

        self.cvs.create_rectangle(midX, bY1, midX-x+X2, bY2)
        self.cvs.create_rectangle(midX-x+X2,bY1,endX,bY2)

        # 라인8
        dw = 40
        dx = x+dw
        dx2 = dx+dw
        dx3 = dx2+210
        dx4 = dx3+72.5
        dx5 = dx4+72.5
        dx6 = midX-x+X2
        dx7 = dx6+130
        dx8 = dx7+110
        dh = 35
        dy = bY2+dh
        dy2 = dy+dh
        dy3 = dy2+dh
        dy4 = dy3+dh
        dy5 = dy4+dh
        dy6 = dy5+30
        self.cvs.create_rectangle(x,bY2,dx,dy)
        self.cvs.create_text(x+18, bY2+16, text='월',font=tpSubjectFont)
        self.cvs.create_rectangle(dx, bY2, dx2, dy)
        self.cvs.create_text(dx + 18, bY2 + 16, text='일', font=tpSubjectFont)
        self.cvs.create_rectangle(dx2, bY2, dx3, dy)
        self.cvs.create_text(dx2 + 100, bY2 + 16, text='품목', font=tpSubjectFont)
        self.cvs.create_rectangle(dx3, bY2, dx4, dy)
        self.cvs.create_text(dx3 + 35, bY2 + 16, text='규격', font=tpSubjectFont)
        self.cvs.create_rectangle(dx4, bY2, dx5, dy)
        self.cvs.create_text(dx4 + 35, bY2 + 16, text='수량', font=tpSubjectFont)
        self.cvs.create_rectangle(dx5, bY2, dx6, dy)
        self.cvs.create_text(dx5 + 55, bY2 + 16, text='단가', font=tpSubjectFont)
        self.cvs.create_rectangle(dx6, bY2, dx7, dy)
        self.cvs.create_text(dx6 + 70, bY2 + 16, text='공급가액', font=tpSubjectFont)
        self.cvs.create_rectangle(dx7, bY2, dx8, dy)
        self.cvs.create_text(dx7 + 55, bY2 + 16, text='세액', font=tpSubjectFont)
        self.cvs.create_rectangle(dx8, bY2, endX, dy)
        self.cvs.create_text(dx8 + 50, bY2 + 16, text='비고', font=tpSubjectFont)

        # 라인9
        self.cvs.create_rectangle(x, dy, dx, dy2)
        self.cvs.create_text(x+18,dy+16,text=tpinfo['tiId'][4:6],font=tpSubjectFont)
        self.cvs.create_rectangle(dx, dy, dx2, dy2)
        self.cvs.create_text(dx + 18, dy + 16, text=tpinfo['tiId'][6:8], font=tpSubjectFont)
        self.cvs.create_rectangle(dx2, dy, dx3, dy2)
        self.cvs.create_text(dx2+pX, dy + 16, text=tpinfo['desc'], font=tpSubjectFont,anchor='w')
        self.cvs.create_rectangle(dx3, dy, dx4, dy2)
        self.cvs.create_rectangle(dx4, dy, dx5, dy2)
        self.cvs.create_rectangle(dx5, dy, dx6, dy2)
        self.cvs.create_rectangle(dx6, dy, dx7, dy2)
        self.cvs.create_text(dx7 - pX, dy + 16, text=tpinfo['amount'], font=tpSubjectFont, anchor='e')
        self.cvs.create_rectangle(dx7, dy, dx8, dy2)
        self.cvs.create_text(dx8 - pX, dy + 16, text=tpinfo['tax'], font=tpSubjectFont, anchor='e')
        self.cvs.create_rectangle(dx8, dy, endX, dy2)

        # 라인10
        self.cvs.create_rectangle(x, dy2, dx, dy3)
        self.cvs.create_rectangle(dx, dy2, dx2, dy3)
        self.cvs.create_rectangle(dx2, dy2, dx3, dy3)
        self.cvs.create_rectangle(dx3, dy2, dx4, dy3)
        self.cvs.create_rectangle(dx4, dy2, dx5, dy3)
        self.cvs.create_rectangle(dx5, dy2, dx6, dy3)
        self.cvs.create_rectangle(dx6, dy2, dx7, dy3)
        self.cvs.create_rectangle(dx7, dy2, dx8, dy3)
        self.cvs.create_rectangle(dx8, dy2, endX, dy3)

        # 라인11
        self.cvs.create_rectangle(x, dy3, dx, dy4)
        self.cvs.create_rectangle(dx, dy3, dx2, dy4)
        self.cvs.create_rectangle(dx2, dy3, dx3, dy4)
        self.cvs.create_rectangle(dx3, dy3, dx4, dy4)
        self.cvs.create_rectangle(dx4, dy3, dx5, dy4)
        self.cvs.create_rectangle(dx5, dy3, dx6, dy4)
        self.cvs.create_rectangle(dx6, dy3, dx7, dy4)
        self.cvs.create_rectangle(dx7, dy3, dx8, dy4)
        self.cvs.create_rectangle(dx8, dy3, endX, dy4)

        # 라인12
        self.cvs.create_rectangle(x, dy4, dx, dy5)
        self.cvs.create_rectangle(dx, dy4, dx2, dy5)
        self.cvs.create_rectangle(dx2, dy4, dx3, dy5)
        self.cvs.create_rectangle(dx3, dy4, dx4, dy5)
        self.cvs.create_rectangle(dx4, dy4, dx5, dy5)
        self.cvs.create_rectangle(dx5, dy4, dx6, dy5)
        self.cvs.create_rectangle(dx6, dy4, dx7, dy5)
        self.cvs.create_rectangle(dx7, dy4, dx8, dy5)
        self.cvs.create_rectangle(dx8, dy4, endX, dy5)

        # 라인13
        bx = x+170
        bx2 = bx+126
        bx3 = bx2+126
        bx4 = bx3+126
        bx5 = bx4+126
        self.cvs.create_rectangle(x,dy5,bx,dy6)
        self.cvs.create_text(x+90, dy5+16, text='합계금액', font=tpSubjectFont)
        self.cvs.create_rectangle(bx, dy5, bx2, dy6)
        self.cvs.create_text(bx + 65, dy5 + 16, text='현금', font=tpSubjectFont)
        self.cvs.create_rectangle(bx2, dy5, bx3, dy6)
        self.cvs.create_text(bx2 + 65, dy5 + 16, text='수표', font=tpSubjectFont)
        self.cvs.create_rectangle(bx3, dy5, bx4, dy6)
        self.cvs.create_text(bx3 + 65, dy5 + 16, text='어음', font=tpSubjectFont)
        self.cvs.create_rectangle(bx4, dy5, bx5, dy6)
        self.cvs.create_text(bx4 + 65, dy5 + 16, text='외상미수금', font=tpSubjectFont)
        self.cvs.create_rectangle(bx5, dy5, endX, endY)
        self.cvs.create_text(bx5+100,dy5+35,text='이 금액을 영수 함',font=tpTiIdLbFont)

        # 라인14
        self.cvs.create_rectangle(x,dy6,bx,endY)
        self.cvs.create_text(bx-pX, dy6 + 20, text=tpinfo['total'], font=tpSubjectFont,anchor='e')
        self.cvs.create_rectangle(bx, dy6, bx2, endY)
        self.cvs.create_rectangle(bx2, dy6, bx3, endY)
        self.cvs.create_rectangle(bx3, dy6,bx4, endY)
        self.cvs.create_rectangle(bx4, dy6,bx5, endY)

        self.cvs.bind('<Escape>', lambda e: cancel())
        self.cvs.bind('<Button-1>', lambda e: self.cvs.focus_set())

    # msgHandler
    # # 세금계산서 조회
    # @staticmethod
    # @MsgProcessor
    # def f40201(**kwargs):
    #     result = {}
    #     print("f40201 kwargs :", kwargs)
    #     condQue = 'select * from taxinvoice'
    #
    #     conditions = []
    #     params = []
    #
    #     if (kwargs.get("시작일자") and kwargs["시작일자"] != "") and (kwargs.get("종료일자") and kwargs["종료일자"] != ""):
    #         conditions.append("ti_create_date between %s and %s")
    #         params.append(kwargs["시작일자"])
    #         params.append(kwargs["종료일자"])
    #
    #     elif (kwargs.get("시작일자") and kwargs["시작일자"] != "") and kwargs.get("종료일자") == "":
    #         conditions.append("ti_create_date between %s and '2099-12-31'")
    #         params.append(kwargs["시작일자"])
    #
    #     elif kwargs.get("시작일자") == "" and (kwargs.get("종료일자") and kwargs["종료일자"] != ""):
    #         conditions.append("ti_create_date between '1900-01-01' and %s")
    #         params.append(kwargs["종료일자"])
    #
    #     if kwargs.get("작성유형") and kwargs["작성유형"] != "":
    #         conditions.append("ti_type = %s")
    #         params.append(kwargs["작성유형"])
    #
    #     if kwargs.get("발행상태") and kwargs["발행상태"] != "":
    #         conditions.append("ti_publish_state = %s")
    #         params.append(kwargs["발행상태"])
    #
    #     if kwargs.get("작성번호") and kwargs["작성번호"] != "":
    #         conditions.append("ti_id = %s")
    #         params.append(kwargs["작성번호"])
    #
    #     # 조건이 있는 경우 WHERE 절 추가
    #     if conditions:
    #         condQue += " WHERE " + " AND ".join(conditions)
    #
    #     try:
    #         db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
    #         db.query('use erp_db;')
    #         rawData = db.query(condQue, params)
    #         aData = [list(ele) for ele in list(rawData)]
    #         for i in range(len(aData)):
    #             if type(aData[i][1]) is datetime.date:
    #                 aData[i][1] = str(aData[i][1])
    #         result = {'sign': 1, 'data': aData}
    #     except Exception as e:
    #         result = {'sign': 0, 'data': {}}
    #         print("f40201 error")
    #         raise e
    #     finally:
    #         return result
    #
    # # 세금계산서 - 저장
    # @staticmethod
    # @MsgProcessor
    # def f40202(**kwargs):
    #     result = {}
    #     data = kwargs['data']
    #     print("f40202 data", data)
    #
    #     try:
    #         db = dbm #.DBManager('localhost', 'root', '0000', 3306)
    #         db.query('use erp_db;')
    #         keys = []
    #         for i in range(len(data)):
    #             keys.append(data[i][10])
    #
    #         for k in keys:
    #             db.query(f'delete from taxinvoice where ti_id = "{k}";')
    #
    #         for i in range(len(data)):
    #             row = data[i]
    #             db.query(
    #                 f"insert into taxinvoice (ti_id, ti_create_date, ti_type, business_client, business_number, ti_description, ti_ori_amount,ti_tax_rate,ti_vat,ti_amount,ti_publish_state) values ('{row[10]}','{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{int(row[5].replace(",", ""))}','{row[6]}','{int(row[7].replace(",", ""))}','{int(row[8].replace(",", ""))}','{row[9]}');")
    #         result = {'sign': 1, 'data': {}}
    #     except Exception as e:
    #         result = {'sign': 0, 'data': {}}
    #         print("f40202 error")
    #         raise e
    #     finally:
    #         return result
    #
    # # 세금계산서 - 발행
    # @staticmethod
    # @MsgProcessor
    # def f40203(**kwargs):
    #     result = {}
    #
    #     data = kwargs['data']
    #     # print("f40203.data", data)
    #     key = data["작성번호"]
    #     print("f40203.key :", key)
    #
    #     try:
    #         db = dbm #.DBManager('localhost', 'root', '0000', 3306)
    #         db.query('use erp_db;')
    #         db.query(f'update taxinvoice set ti_publish_state = "발행" where ti_id = "{key}";')
    #         result = {'sign': 1, 'data': {}}
    #     except Exception as e:
    #         result = {'sign': 0, 'data': {}}
    #         print("f40203 error")
    #         raise e
    #     finally:
    #         return result
    #
    # # 세금계산서 - 세금계산서삭제
    # @staticmethod
    # @MsgProcessor
    # def f40204(**kwargs):
    #     result = {}
    #     data = kwargs["data"]
    #     print("f40204", data)
    #     try:
    #         db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
    #         db.query('use erp_db;')
    #         for key in data:
    #             db.query(f'delete from taxinvoice where ti_id = "{key}";')  # and ti_publish_state = "None"
    #         result = {'sign': 1, 'data': {}}
    #     except Exception as e:
    #         print("f40204 error")
    #         result = {'sign': 0, 'data': {}}
    #         raise e
    #     finally:
    #         return result
    #
    # # 세금계산서 - 세금계산서삭제
    # @staticmethod
    # @MsgProcessor
    # def f40204(**kwargs):
    #     result = {}
    #     data = kwargs["data"]
    #     print("f40204", data)
    #     try:
    #         db = dbm  # .DBManager('localhost', 'root', '0000', 3306)
    #         db.query('use erp_db;')
    #         for key in data:
    #             db.query(f'delete from taxinvoice where ti_id = "{key}";')  # and ti_publish_state = "None"
    #         result = {'sign': 1, 'data': {}}
    #     except Exception as e:
    #         print("f40204 error")
    #         result = {'sign': 0, 'data': {}}
    #         raise e
    #     finally:
    #         return result
    #
    # # 세금계산서 - 분개삭제
    # @staticmethod
    # @MsgProcessor
    # def f40205(**kwargs):
    #     result = {}
    #     # print("f40205 data:",kwargs)
    #     cond = kwargs["세금계산서번호"]
    #     try:
    #         db = dbm #.DBManager('localhost', 'root', '0000', 3306)
    #         db.query('use erp_db;')
    #         rawData = db.query(f'select * from journalizingbook where ti_id = "{cond}";')
    #         aData = [list(ele) for ele in list(rawData)]
    #         result = {'sign': 1, 'data': aData}
    #     except Exception as e:
    #         result = {'sign': 0, 'data': {}}
    #         print("f40201 error")
    #         raise e
    #     finally:
    #         return result
    #
    # # 세금계산서 분개 저장
    # @staticmethod
    # @MsgProcessor
    # def f40206(**kwargs):
    #     result = {}
    #     # print("f40206 kwargs", kwargs)
    #     key = None
    #     values = []
    #     for k, v in kwargs.items():
    #         key = k
    #         values = v
    #
    #     print(key, " / ", values)
    #     try:
    #         db = dbm #.DBManager('localhost', 'root', '0000', 3306)
    #         db.query('use erp_db;')
    #         db.query(f'delete from journalizingbook where ti_id = "{key}";')
    #
    #         for row in range(len(values)):
    #             db.query(
    #                 f'insert into journalizingbook (jr_type, account_code, account_name, business_code, business_client, jr_dr, jr_cr, jr_description, jr_evidence,ti_id, jr_base) values ("{values[row][0]}","{values[row][1]}","{values[row][2]}","{values[row][3]}","{values[row][4]}","{values[row][5]}","{values[row][6]}","{values[row][7]}","{values[row][8]}","{key}","ti");')
    #
    #         result = {'sign': 1, 'data': {}}
    #     except Exception as e:
    #         print("f40206 errer")
    #         result = {'sign': 0, 'data': {}}
    #         raise e
    #     finally:
    #         return result
    #
    # # 세금계산서 분개 삭제
    # @staticmethod
    # @MsgProcessor
    # def f40207(**kwargs):
    #     result = {}
    #     data = kwargs["data"]
    #     print("f40207", data)
    #     try:
    #         db = dbm #.DBManager('localhost', 'root', '0000', 3306)
    #         db.query('use erp_db;')
    #         for key in data:
    #             db.query(f"DELETE FROM journalizingbook WHERE ti_id = '{key}';")
    #         result = {"sign": 1, "data": {}}
    #     except Exception as e:
    #         print("f40207 error")
    #         result = {"sign": 0, "data": {}}
    #         raise e
    #
    #     finally:
    #         return result

    # @staticmethod
    # @MsgProcessor
    # def f30102(**kwargs):
    #     if kwargs:
    #         data = dbm.query(
    #             f"SELECT Customer_name, business_number, Customer_code, Type_business, business_adress, ContactPerson_name, ContactPerson_phone, e_mail from Customer_management WHERE Customer_name LIKE '%{kwargs.get("Customer_name")}%'")
    #     else:
    #         data = dbm.query(
    #             'select Customer_code, Customer_name, business_number, ContactPerson_name from Customer_management;')
    #     # result=dbm.query(f"SELECT Customer_name, business_number, Customer_code, Type_business, business_adress, ContactPerson_name, ContactPerson_phone, e_mail from Customer_management WHERE Customer_name LIKE '%{kwargs.get("Customer_name")}%' or business_number LIKE '%{kwargs.get("business_number")}%' or Customer_code LIKE '%{kwargs.get("Customer_code")}%' or Country LIKE '%{kwargs.get("Country")}%'")
    #     print("결과 : ", data)
    #     if data is not None:
    #         result = {"sign": 1, "data": data}
    #     else:
    #         result = {"sign": 0, "data": None}
    #
    #     return result

    # @staticmethod
    # @MsgProcessor
    # def f10103(**kwargs):
    # # 등록번호 : corporation_registration_number 123-12-12345
    # # 회사이름 :
    # # 대표자이름 :
    # # 주소 : address
    #     result = {'sign':1,'data':{"등록번호":"123-12-99999","주소":"대전 서구 계룡로 491번길 86","회사이름":"대전인더스트리","대표자":"성진하"}}
    #     return result


test_socket = None

if __name__ == "__main__":
    # r = tk.Tk()
    # r.geometry('1600x900')
    #
    # fr = TaxInvoiceFrame(r)
    #
    # r.mainloop()

    import socket
    from threading import Thread

    root = tk.Tk()  # 부모 창
    root.geometry("1600x900")
    test_frame = TaxInvoiceFrame(root)
    test_frame.place(x=300, y=130)

    # HOST = "192.168.0.29"
    HOST = 'localhost'
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        test_socket = sock
        sock.connect((HOST, PORT))
        t = Thread(target=test_frame.recv_test, args=())
        t.daemon = True
        t.start()
        root.mainloop()