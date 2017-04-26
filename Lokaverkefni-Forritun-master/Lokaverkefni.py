#Jónas Freyr Bjarnason
#Alexander Kári Ragnarsson
#Forritun
#26.04.2017

class spil:
    def __init__(self,nafn,thyngd,mjolk,ull,born,laeri,frjo,bak,malir):
        self.nafn = nafn
        self.thyngd = thyngd
        self.mjolk = mjolk
        self.ull = ull
        self.born = born
        self.laeri = laeri
        self.frjo = frjo
        self.bak = bak
        self.malir = malir
    def lysing(self):
        print("Nafn:",self.nafn)
        print("Þyngd:",self.thyngd)
        print("Mjólkurlagni dætra:",self.mjolk)
        print("Einkunn ullar:",self.ull)
        print("Földi afkæma:",self.born)
        print("Einkunn læris:",self.laeri)
        print("Frjósemi:",self.frjo)
        print("Gerð/þykkt bakvöðva:",self.bak)
        print("Einkunn malir:",self.malir)
ollspil=[]
with open("spil.txt","r",encoding = 'utf-8') as f:
    for a in range(52):
        nafn = eval(f.readline())
        thyngd = eval(f.readline())
        mjolk = eval(f.readline())
        ull = eval(f.readline())
        born = eval(f.readline())
        laeri = eval(f.readline())
        frjo = eval(f.readline())
        bak = eval(f.readline())
        malir = eval(f.readline())
        f.readline()
        hrutur = spil(nafn,thyngd,mjolk,ull,born,laeri,frjo,bak,malir)
        ollspil.append(hrutur)
print(ollspil)
for a in ollspil:
    a.lysing()
    print("---")
