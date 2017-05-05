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

spilari1=[]
spilari2=[]
while True:
    ollspil = []
    spilari1 = []
    spilari2 = []
    with open("spil.txt", "r") as f:
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
            hrutur = spil(nafn, thyngd, mjolk, ull, born, laeri, frjo, bak, malir)
            ollspil.append(hrutur)
    print("1. Spila á móti tölvu")
    print("3. Skoða spil")
    val=int(input(">> "))
    if val == 1:

        for a in range(26):
            spil1 = random.choice(ollspil)
            spilari1.append(spil1)
            ollspil.remove(spil1)
            spil2 = random.choice(ollspil)
            spilari2.append(spil2)
            ollspil.remove(spil2)
        win=[]
        turn = 1
        while len(spilari1) !=0 and len(spilari2) != 0:
            #input("sláðu á enter fyrir næstu umferð")
            #a = spilari1[0] Virkaði ekki tölvan stundum sleppti því
            b = spilari2[0]
            aflokkar = [spilari1[0].thyngd, spilari1[0].mjolk, spilari1[0].ull, spilari1[0].born, spilari1[0].laeri, spilari1[0].frjo, spilari1[0].bak, spilari1[0].malir,spilari1[0].nafn]
            bflokkar=[b.thyngd,b.mjolk,b.ull,b.born,b.laeri,b.frjo,b.bak,b.malir,b.nafn]
            if turn % 2 != 0:
                print("Þú átt leik")
                spilari1[0].lysing()
                print("1. Þyngd")
                print("2. Mjólkurlagni dætra")
                print("3. Einkunn ullar")
                print("4. Földi afkæma")
                print("5. Einkunn læris")
                print("6. Frjósemi")
                print("7. Gerð/þykkt bakvöðva")
                print("8. Einkunn malir")
                val = int(input(">> "))
                val -= 1
            elif turn % 2 == 0:
                for a in range(random.randint(5,8)):
                    print("Tölvan er að hugsa...")
                    time.sleep(1)
                val=random.randint(0,7)
            if  aflokkar[val]> bflokkar[val]:
                print("Þú vannst")
                print("Þú varst með",aflokkar[val],"en tölvan var með",bflokkar[val])
                print(bflokkar[-1],"bætisti í þinn stokk")
                spilari1.append(spilari1[0])
                spilari1.append(b)
                if len(win) > 0:
                    for c in win:
                        spilari1.append(c)
                    win.clear()
            elif aflokkar[val]< bflokkar[val]:
                print("Þú tapaðir")
                print("Þú varst með", aflokkar[val], "en tölvan var með", bflokkar[val])
                print(aflokkar[-1], "bætisti í stokk tölvu")
                spilari2.append(spilari1[0])
                spilari2.append(b)
                if len(win) > 0:
                    for c in win:
                        spilari2.append(c)
                    win.clear()
            else:
                print("Jafntefli")
                print("Þú varst með", aflokkar[val], "og tölvan var með", bflokkar[val])
                print("Spilin ykkar fer í vinnings búnka og þið reynið aftur")
                win.append(spilari1[0])
                win.append(b)
            spilari1.remove(spilari1[0])
            spilari2.remove(b)
            print("Spilabúnki þinn",len(spilari1))
            print("Spilabúnki tölvu",len(spilari2))
            turn += 1
        if len(spilari1) > len(spilari2):
            print("Þú vannst")
        elif len(spilari2) > len(spilari1):
            print("Tölvan vann")
    if val == 2:
        for a in ollspil:
            print("---")
            a.lysing()
