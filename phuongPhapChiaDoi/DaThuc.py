import re

class DaThuc():
    def __init__(self, chuoiBieuThuc, bacCuaDaThuc):
        chuoiBieuThuc = re.sub("\s","",chuoiBieuThuc)
        self.bacCuaDaThuc = bacCuaDaThuc
        self.mangHeSo = [0] * (self.bacCuaDaThuc + 1)
        for i in range(0,self.bacCuaDaThuc+1):
            heSo = re.findall("[-\+]?[0-9]*?(?=x" + str(i) + ")",chuoiBieuThuc)
            if len(heSo) != 0:
                self.mangHeSo[i] = int(heSo[0])  
    def tinhGiaTri(self,x):
        ketQua = self.mangHeSo[self.bacCuaDaThuc]
        
        for i in range(self.bacCuaDaThuc - 1, -1, -1):
            ketQua = ketQua*x + self.mangHeSo[i]

        return ketQua
