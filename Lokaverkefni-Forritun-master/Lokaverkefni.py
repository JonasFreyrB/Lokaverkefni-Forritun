#Jónas Freyr Bjarnason
#Alexander Kári Ragnarsson
#Forritun
#26.04.2017
import random
import time
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
with open("spil.txt","r") as f:
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
spilari1=[]
spilari2=[]
while True:
    print("1. Spila á móti tölvu")
    print("2. Spila á móti öðrum leikmann")
    print("3. Skoða spil")
    val=int(input(">> "))
    if val == 1:
        print(ollspil)
        for a in range(26):
            spil1 = random.choice(ollspil)
            spilari1.append(spil1)
            ollspil.remove(spil1)
            spil2 = random.choice(ollspil)
            spilari2.append(spil2)
            ollspil.remove(spil2)
        print(ollspil)
        print(len(spilari1))
        print(len(spilari2))
        input()
        win=[]
        while len(spilari1 != 0) and len(spilari2 != 0):
            turn = 1
            for a in spilari1:
                for b in spilari2:
                    if turn == 1:
                        print("Þú átt leik")
                        a.lysing
                        print("1. Þyngd")
                        print("2. Mjólkurlagni dætra")
                        print("3. Einkunn ullar")
                        print("4. Földi afkæma")
                        print("5. Einkunn læris")
                        print("6. Frjósemi")
                        print("7. Gerð/þykkt bakvöðva")
                        print("8. Einkunn malir")
                        val = int(input(">> "))
                        if val == 1:
                            talaa = a.thyngd
                            talab = b.thyngd
                        elif val == 2:
                            talaa = a.mjolk
                            talab = b.mjolk
                        elif val == 3:
                            talaa = a.ull
                            talab = b.ull
                        elif val == 4:
                            talaa = a.born
                            talab = b.born
                        elif val == 5:
                            talaa = a.laeri
                            talab = b.laeri
                        elif val == 6:
                            talaa = a.frjo
                            talab = b.frjo
                        elif val == 7:
                            talaa = a.bak
                            talab = b.bak
                        elif val == 8:
                            talaa = a.malir
                            talab = b.malir
                        if talaa > talab:
                            print("Þú vannst")
                            print("Þú varst með",talaa,"en tölvan var með",talab)
                            print(b.nafn,"bætisti í þinn stokk")
                            spilari1.insert(-1, b)
                            spilari2.remove(b)
                        elif talaa < talab:
                            print("Þú tapaðir")
                            print("Þú varst með", talaa, "en tölvan var með", talab)
                            print(a.nafn, "bætisti í stokk tölvu")
                            spilari2.insert(-1, a)
                            spilari1.remove(a)
                        else:
                            print("Jafntefli")
                            print("Þú varst með", talaa, "en tölvan var með", talab)
                            print("Spilin ykkar fer í vinnings búnka og þið reynið aftur")
                            win.append(a)
                            win.append(b)
                            spilari1.remove(a)
                            spilari2.remove(b)
    if val == 3:
        for a in ollspil:
            print("---")
            a.lysing
