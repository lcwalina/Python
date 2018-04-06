class Pojazd:
    def __init__(self):
        self.__kolor="Nie ustawiono"
        self.__rodzaj="Nie ustawiono"
        self.__wartosc="Nie ustawiono"
        self.__nazwa="Nie ustawiono"

    def setKolor(self, value):
        self.__kolor = value
    def setRodzaj(self, value):
        self.__rodzaj = value
    def setWartosc(self, value):
        self.__wartosc = value
    def setNazwa(self, value):
        self.__nazwa = value

    def getKolor(self):
        return self.__kolor
    def getRodzaj(self):
        return self.__rodzaj
    def getWartosc(self):
        return self.__wartosc
    def getNazwa(self):
        return self.__nazwa

Auto1 = Pojazd()
Auto2 = Pojazd()

Auto1.setKolor("czerwony")
Auto1.setNazwa("Ferrari")
Auto1.setWartosc(60000)
Auto1.setRodzaj("kabriolet")

print(f"Auto1:\nKolor:{Auto1.getKolor()}\nNazwa:{Auto1.getNazwa()}\nWartość:{Auto1.getWartosc()}\nRodzaj:{Auto1.getRodzaj()}")
print("\n\n\n")

Auto2.setKolor("niebieski")
Auto2.setNazwa("Ikarus")
Auto2.setWartosc(10000)
Auto2.setRodzaj("autobus")

print(f"Auto2:\nKolor:{Auto2.getKolor()}\nNazwa:{Auto2.getNazwa()}\nWartość:{Auto2.getWartosc()}\nRodzaj:{Auto2.getRodzaj()}")
