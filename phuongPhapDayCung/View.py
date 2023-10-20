from tkinter import *
from tkinter import ttk
from DaThuc import DaThuc

class View():
    def __init__(self, root):
        root.title("Phương pháp dây cung")
        root.geometry("650x500+500+90") 

        mainframe = ttk.Frame(root, padding="3 3 12 12 ")
        mainframe.pack(padx=10,fill=BOTH ,anchor=W)

        tableframe = ttk.Frame(root, padding="3 3 12 12 ")
        tableframe.pack()
    
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
        columns = ('n','x_n','sai_so')

        tree = ttk.Treeview(tableframe, columns=columns, show='headings')

        tree.heading('n', text='n')
        tree.heading('x_n', text='x_n')
        tree.heading('sai_so', text='Sai số')

        tree.column('n', width=20)
        tree.column('x_n',width=120)
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
        fn = DaThuc()
        fn.setChuoiBieuThuc(bieuThuc,bac)
        a = float(self.mocDuoi.get())
        b = float(self.mocTren.get())  

        if fn.tinhGiaTri(a)*fn.tinhGiaTri(b) >= 0:
            self.result.set("Phương trình không có nghiệm trong khoảng [a,b]")
            return

        self.table = []  
        
        i = 1
        x_n = a if fn.tinhGiaTri(a) < 0 else b
        n = b if fn.tinhGiaTri(a) < 0 else a

        daThucDaoHam = fn.daoHam()
        m = daThucDaoHam.tinhGiaTri(a)
        M = daThucDaoHam.tinhGiaTri(b)

        self.table.append((0, x_n))
        while True:
            x_n1 = x_n
            x_n = x_n - ((fn.tinhGiaTri(x_n)/(fn.tinhGiaTri(x_n)-fn.tinhGiaTri(n))) * (x_n - n))            
            saiSo = ((M-m)/m)*abs(x_n - x_n1)
            self.table.append((i,round(x_n,5),round(saiSo,5)))
            if fn.tinhGiaTri(x_n) == 0:
                self.nghiemGanDung = round(x_n,5)
                self.saiSoMacPhai = round(saiSo,5)
                break
            i+=1
            if saiSo < float(self.epsilon.get()):
                self.nghiemGanDung = round(x_n,5)
                self.saiSoMacPhai = round(saiSo,5)
                break

        self.result.set("Tính được nghiệm gần đúng x=" + str(self.nghiemGanDung) + " với sai số mắc phải =" + str(self.saiSoMacPhai))
        self.create_table(tableframe)



