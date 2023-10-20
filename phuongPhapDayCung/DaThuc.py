import re

class DaThuc():
    def __init__(self):
        self.__bacCuaDaThuc = 0
        self.__mangHeSo = []

    def get__mangHeSo(self):
        return self.__mangHeSo
    
    def setChuoiBieuThuc(self, chuoiBieuThuc, bacCuaDaThuc):
        chuoiBieuThuc = re.sub("\s","",chuoiBieuThuc)
        self.__bacCuaDaThuc = bacCuaDaThuc
        self.__mangHeSo = [0] * (self.__bacCuaDaThuc + 1)
        for i in range(self.__bacCuaDaThuc+1,-1,-1):
            heSo = chuoiBieuThuc if i==0 else re.findall("[-\+]?[0-9]*?\.?[0-9]*?(?=x" + str(i) + ")",chuoiBieuThuc)
            if len(heSo) != 0:
                self.__mangHeSo[i] = float(heSo) if i==0 else float(heSo[0])
                if(i!=0):
                    subString = re.findall("[-\+]?[0-9]*?\.?[0-9]*?x" + str(i),chuoiBieuThuc)
                    chuoiBieuThuc = chuoiBieuThuc.replace(subString[0], "")

    def tinhGiaTri(self,x):
        ketQua = self.__mangHeSo[self.__bacCuaDaThuc]
        for i in range(self.__bacCuaDaThuc - 1, -1, -1):
            ketQua = ketQua*x + self.__mangHeSo[i]
        return ketQua

    def daoHam(self):
        daThuc = DaThuc()
        daThuc.__bacCuaDaThuc = self.__bacCuaDaThuc - 1
        daThuc.__mangHeSo = [0] * (daThuc.__bacCuaDaThuc+1)
        for i in range(self.__bacCuaDaThuc, 0, -1):
            daThuc.__mangHeSo[i-1] = self.__mangHeSo[i]*i
        return daThuc

"""
dathuc = DaThuc()
dathuc.setChuoiBieuThuc("0.234x3 + 0.1x2 - 1.2x1 +3",3)
print(dathuc.get__mangHeSo())  
"""   

