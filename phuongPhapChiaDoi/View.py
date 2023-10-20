from tkinter import *
from tkinter import ttk
from DaThuc import DaThuc

class View():
    def __init__(self, root):
        root.title("Phương pháp chia đôi")
        root.geometry("650x500+500+90") 

        mainframe = ttk.Frame(root, padding="3 3 12 12 ")
        # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.pack(padx=10,fill=BOTH ,anchor=W)

        tableframe = ttk.Frame(root, padding="3 3 12 12 ")
        # tableframe.grid(column=0, row=1, sticky=(N, W, E, S))
        tableframe.pack()
        #root.columnconfigure(0, weight=1)
        #root.rowconfigure(0, weight=1)

        self.chuoiBieuThuc = StringVar()
        self.bac = StringVar()
        ttk.Label(mainframe, text="Nhập đa thức:").pack(padx=5, pady=2, anchor=W)
        ttk.Entry(mainframe, width=25, textvariable=self.chuoiBieuThuc).pack(padx=5,anchor=W)
        ttk.Label(mainframe, text="Bậc:").pack(padx=5, pady=2,anchor=W)
        ttk.Entry(mainframe, width=5, textvariable=self.bac).pack(padx=5,anchor=W)

        self.mocDuoi = StringVar()
        self.mocTren = StringVar()
        ttk.Label(mainframe, text="Đoạn").pack(padx=5, pady=2,anchor=W)
        ttk.Entry(mainframe, width=5, textvariable=self.mocDuoi).pack(padx=5,anchor=W)
        ttk.Entry(mainframe, width=5, textvariable=self.mocTren).pack(padx=5,anchor=W)

        self.epsilon = StringVar()
        ttk.Label(mainframe, text="Sai số:").pack(padx=5, pady=2,anchor=W)
        ttk.Entry(mainframe, width=15, textvariable=self.epsilon).pack(padx=5,anchor=W)

        ttk.Button(mainframe, text="Chạy", command=lambda: self.calculate(tableframe)).pack(padx=5, pady=8,anchor=CENTER)

        self.result = StringVar()
        ttk.Label(mainframe, textvariable=self.result).pack(padx=5, pady=2,anchor=W)

    def create_table(self,tableframe):
        columns = ('n', 'a_n', 'b_n', 'c_n','f(c_n)','sai_so')

        tree = ttk.Treeview(tableframe, columns=columns, show='headings')

        tree.heading('n', text='n')
        tree.heading('a_n', text='a_n')
        tree.heading('b_n', text='b_n')
        tree.heading('c_n', text='c_n')
        tree.heading('f(c_n)', text='f(c_n)')
        tree.heading('sai_so', text='Sai số')

        tree.column('n', width=20)
        tree.column('a_n',width=120)
        tree.column('b_n',width=120)
        tree.column('c_n',width=120)
        tree.column('f(c_n)',width=120)
        tree.column('sai_so',width=120)


        for row in self.table:
            tree.insert('', END, values=row)
        
        tree.grid(row=0, column=0, sticky=N)

        scrollbar = ttk.Scrollbar(tableframe, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def calculate(self,tableframe):
        bieuThuc = self.chuoiBieuThuc.get()
        bac = int(self.bac.get())
        daThuc = DaThuc(bieuThuc,bac)
        a = float(self.mocDuoi.get())
        b = float(self.mocTren.get())  

        if daThuc.tinhGiaTri(a)*daThuc.tinhGiaTri(b) >= 0:
            self.result.set("Phương trình không có nghiệm trong khoảng [a,b]")
            return

        self.table = []  
        
        n = 0
        while True:
            saiSo = round(b - a,6)
            c = round((a+b)/2,6)
            self.table.append((n,a,b,c,round(daThuc.tinhGiaTri(c),5),saiSo))
            if daThuc.tinhGiaTri(c) == 0:
                self.nghiemGanDung = c
                self.saiSoMacPhai = saiSo
                break
            if daThuc.tinhGiaTri(a)*daThuc.tinhGiaTri(c) < 0:
                b = c
            else:
                a = c
            n+=1
            if saiSo < float(self.epsilon.get()):
                self.nghiemGanDung = c
                self.saiSoMacPhai = saiSo
                break
        
        self.result.set("Tính được nghiệm gần đúng x=" + str(self.nghiemGanDung) + " với sai số mắc phải =" + str(self.saiSoMacPhai))
        self.create_table(tableframe)



