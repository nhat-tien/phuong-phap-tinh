from tkinter import *
from tkinter import ttk
import math

class TinhChuSoDangTin():
    def __init__(self, root):
        root.title("Tính toán chữ số đáng tin")
        root.geometry("320x200+100+100") 

        mainframe = ttk.Frame(root, padding="3 3 12 12 ")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        
        self.soGanDung = StringVar()
        ttk.Label(mainframe, text="Số gần đúng:").grid(column=0, row=0)
        ttk.Entry(mainframe, width=20, textvariable=self.soGanDung).grid(column=1, row=0, sticky=(W, E))

        self.saiSoTuyetDoi = StringVar()
        ttk.Label(mainframe, text="Sai số tuyệt đối:").grid(column=0, row=1)
        ttk.Entry(mainframe, width=20, textvariable=self.saiSoTuyetDoi).grid(column=1, row=1, sticky=(W, E))

        self.nghiaHep = BooleanVar()
        self.nghiaHep.set(True)
        ttk.Radiobutton(mainframe, text="Nghĩa hẹp", value=True, variable=self.nghiaHep).grid(column=0, row=2)
        ttk.Radiobutton(mainframe, text="Nghĩa rộng", value=False, variable=self.nghiaHep).grid(column=1, row=2)


        ttk.Button(mainframe, text="Chạy", command=self.tinhToan).grid(column=1, row=3, sticky=E)
        

        self.message = StringVar()
        ttk.Label(mainframe, textvariable=self.message, wraplength=250).grid(column=0, row=4, columnspan=2)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)


    def tinhToan(self):
        try:
            saiSoTuyetDoi = float(self.saiSoTuyetDoi.get())

            omega = 0.5 if self.nghiaHep.get() else 1
            n = int(math.log10(saiSoTuyetDoi/omega))

            arrOfSoGanDung = list(self.soGanDung.get())

            result = ""

            flag = False
            for i in range(0,arrOfSoGanDung.index(".")-n+1):
                # Loai bo nhung chu so 0 nam o phan dau
                if not flag:
                    if arrOfSoGanDung[i] == "0" or arrOfSoGanDung[i] == ".":
                        continue
                    else:
                        flag = True
                if arrOfSoGanDung[i] == ".": continue
                result = result + "," +arrOfSoGanDung[i]

            self.message.set("Các số đáng tin là: " + result[1:])

        except ValueError:
            self.message.set("Cần nhập đầy đủ các thông tin")