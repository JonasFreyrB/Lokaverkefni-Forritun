#Jónas Freyr Bjarnason
#Alexander Kári Ragnarsson
#Forritun
#26.04.2017
import random
#sæki random
import time
#sæki time
class spil:
    #Bý til klasa
    def __init__(self,nafn,thyngd,mjolk,ull,born,laeri,frjo,bak,malir):
        #bý til fall með smið
        self.nafn = nafn
        #skilgreini self.nafn sem nafn
        self.thyngd = thyngd
        #skilgreini self.thyngd sem thyngd
        self.mjolk = mjolk
        #skilgreini self.mjolk sem mjolk
        self.ull = ull
        #skilgreini self.ull sem ull
        self.born = born
        #skilgreini self.born sem born
        self.laeri = laeri
        #skilgreini self.laeri sem laeri
        self.frjo = frjo
        #skilgreini self.frjo sem frjo
        self.bak = bak
        #skilgreini self.bak sem bak 
        self.malir = malir
        #skilgreini self.malir sem malir
    def lysing(self):
        #bý til fall sem prentar upplýsingar
        print("Nafn:",self.nafn)
        #prentar út nafnið
        print("Þyngd:",self.thyngd)
        #prentar út thyngd
        print("Mjólkurlagni dætra:",self.mjolk)
        #prentar út mjolk
        print("Einkunn ullar:",self.ull)
        #prentar út ull
        print("Földi afkæma:",self.born)
        #prentar út born
        print("Einkunn læris:",self.laeri)
        #prentar út laeri
        print("Frjósemi:",self.frjo)
        #prentar út frjo
        print("Gerð/þykkt bakvöðva:",self.bak)
        #prentar út bak
        print("Einkunn malir:",self.malir)
        #prentar út malir

spilari1=[]
spilari2=[]
while True:
    ollspil = []
    #Bý til lista sem kallast ollspil
    spilari1 = []
    spilari2 = []
    with open("spil.txt", "r") as f:
        #opna textaskrá sem read og skilgreini hana sem f
        for a in range(52):
            #læt textaskrá í forlykkju sem keyrir 52 sinnum
            nafn = eval(f.readline())
            #les línu fyrir nafn
            thyngd = eval(f.readline())
            #les línu fyrir thyngd
            mjolk = eval(f.readline())
            #les línu fyrir mjolk
            ull = eval(f.readline())
            #les línu fyrir ull
            born = eval(f.readline())
            #les línu fyrir born
            laeri = eval(f.readline())
            #les línu fyrir laeri
            frjo = eval(f.readline())
            #les línu fyrir frjo
            bak = eval(f.readline())
            #les línu fyrir bak
            malir = eval(f.readline())
            #les línu fyrir malir
            f.readline()
            #les tóma línu 
            hrutur = spil(nafn,thyngd,mjolk,ull,born,laeri,frjo,bak,malir)
            #kallar á klasann spil og bý til hrút
            ollspil.append(hrutur)
            #bæti hrút í lista
    print("1. Spila á móti tölvu")
    print("2. Skoða spil")
    #Birti valmöguleika
    val=int(input(">> "))
    #Bið notandan um að velja
    if val == 1:

        for a in range(26):
            #Bý til for lykkju
            spil1 = random.choice(ollspil)
            #spil1 er random val í ollspil
            spilari1.append(spil1)
            #bæti spil1 í spilari1
            ollspil.remove(spil1)
            #eyði spil1 úr ollspil
            spil2 = random.choice(ollspil)
            #spil2 er random val í ollspil
            spilari2.append(spil2)
            #bæti spil 2 í spilari2
            ollspil.remove(spil2)
            #eyði spil2 úr ollspil
        win=[]
        #bý til liksta sem kallast win
        turn = 1
        #bý til teljara
        while len(spilari1) !=0 and len(spilari2) != 0:
        #meðan lengd spilara1 er ekki 0 og lengd spilara2 er ekki 0
            #input("sláðu á enter fyrir næstu umferð")
            #a = spilari1[0] Virkaði ekki tölvan stundum sleppti því
            b = spilari2[0]
            #staki b er spilari2
            aflokkar = [spilari1[0].thyngd, spilari1[0].mjolk, spilari1[0].ull, spilari1[0].born, spilari1[0].laeri, spilari1[0].frjo, spilari1[0].bak, spilari1[0].malir,spilari1[0].nafn]
            #Bý til lista með öllum aðgerðum spilara1
            bflokkar=[b.thyngd,b.mjolk,b.ull,b.born,b.laeri,b.frjo,b.bak,b.malir,b.nafn]
            #Bý til lista með öllum aðgerðum spilara2
            if turn % 2 != 0:
            #ef turn er módulus 12 og er ekki deilanlegur með 0
                print("Þú átt leik")
                #þá prentast þú att leik
                spilari1[0].lysing()
                #sýni spil
                print("1. Þyngd")
                print("2. Mjólkurlagni dætra")
                print("3. Einkunn ullar")
                print("4. Földi afkæma")
                print("5. Einkunn læris")
                print("6. Frjósemi")
                print("7. Gerð/þykkt bakvöðva")
                print("8. Einkunn malir")
                #birti valmöguleika
                val = int(input(">> "))
                #bið notandan um að velja
                val -= 1
                #dreg einn frá val
            elif turn % 2 == 0:
            #annars ef turn er módulus 2 og ef hann er deilanlegur með 0
                for a in range(random.randint(5,8)):
                #bý til for lykkju sem keyrir fra random 5-8
                    print("Tölvan er að hugsa...")
                    #Birti tölvan er að hugsa
                    time.sleep(1)
                    #læt forritið biða i eina sekúndu
                val=random.randint(0,7)
                #val er random tala frá 0-7
            if  aflokkar[val]> bflokkar[val]:
            #ef aflokkur er stærri en bflokkur
                print("Þú vannst")
                print("Þú varst með",aflokkar[val],"en tölvan var með",bflokkar[val])
                print(bflokkar[-1],"bætisti í þinn stokk")
                #prentast útkommur
                spilari1.append(spilari1[0])
                #bæti staki úr spilara1 í spilara1
                spilari1.append(b)
                #bæti b í spilara1
                if len(win) > 0:
                #ef lengd win er stærri en 0
                    for c in win:
                        spilari1.append(c)
                        #bæti c í spilara1
                    win.clear()
                    #tæmi listann win
            elif aflokkar[val]< bflokkar[val]:
            #ef aflokkar eru minni en bflokkar
                print("Þú tapaðir")
                print("Þú varst með", aflokkar[val], "en tölvan var með", bflokkar[val])
                print(aflokkar[-1], "bætisti í stokk tölvu")
                #birti útkommu
                spilari2.append(spilari1[0])
                #bæti staki úr spilara1 í spilara2 
                spilari2.append(b)
                #bæti b i spilara2
                if len(win) > 0:
                #ef lengd win er stærri en 0
                    for c in win:
                        spilari2.append(c)
                        #bæti c í spilara2
                    win.clear()
                    #tæmi listann win
            else:
            #annars
                print("Jafntefli")
                print("Þú varst með", aflokkar[val], "og tölvan var með", bflokkar[val])
                print("Spilin ykkar fer í vinnings búnka og þið reynið aftur")
                #birtist útkomma
                win.append(spilari1[0])
                #bæti staki úr spilara1 í win
                win.append(b)
                #bæti b in win
            spilari1.remove(spilari1[0])
            #eyði staki úr spilara1 
            spilari2.remove(b)
            #eyði b úr spilara2
            print("Spilabúnki þinn",len(spilari1))
            #birti lengd spilara1
            print("Spilabúnki tölvu",len(spilari2))
            #birti lengd spilara2
            turn += 1
            #bæti einum við turn
        if len(spilari1) > len(spilari2):
        #ef lengd spilara1 er stærri en lengd spilara2
            print("Þú vannst")
            #birtist þú vannst
        elif len(spilari2) > len(spilari1):
        #ef lengd spilara2 er stærri en lengd spilara1
            print("Tölvan vann")
            #birtist tölvan vann
    if val == 2:
    #ef val er 2
        ollspil = []
        #Bý til lista sem kallast ollspil
        spilari1 = []
        spilari2 = []
        with open("spil.txt", "r") as f:
        #opna textaskrá sem read og skilgreini hana sem f
            for a in range(52):
                #læt textaskrá í forlykkju sem keyrir 52 sinnum
                nafn = eval(f.readline())
                #les línu fyrir nafn
                thyngd = eval(f.readline())
                #les línu fyrir thyngd
                mjolk = eval(f.readline())
                #les línu fyrir mjolk
                ull = eval(f.readline())
                #les línu fyrir ull
                born = eval(f.readline())
                #les línu fyrir born
                laeri = eval(f.readline())
                #les línu fyrir laeri
                frjo = eval(f.readline())
                #les línu fyrir frjo
                bak = eval(f.readline())
                #les línu fyrir bak
                malir = eval(f.readline())
                #les línu fyrir malir
                f.readline()
                #les tóma línu 
                hrutur = spil(nafn,thyngd,mjolk,ull,born,laeri,frjo,bak,malir)
                #kallar á klasann spil og bý til hrút
                ollspil.append(hrutur)
                #bæti hrút í lista
        for a in ollspil:
            #for lykkja sem keyrir i gengum ollspil
            print("---")
            a.lysing()
            #birti upplýsingar um spil
