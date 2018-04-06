#Obsluz wszystkie wyjatki
aktor = {"imie": "Piotr Fronczewski", "opinia": "swietny"}

#Musisz ta funkcje zmodyfikowac tak, aby zwracala nazwisko aktora.
# W razie potrzeby przypomnij sobie poprzednie lekcje
def zwroc_nazwisko():
    try:
        return aktor["nazwisko"]
    except KeyError:
        try:
            imie_nazwisko = aktor["imie"].split()
            return imie_nazwisko[1]
        except IndexError:
            print("Error: Tylko imię dostępne")
            return IndexError
        except KeyError:
            print("Error: Brak klucza 'imie'")
            return KeyError
#Test kodu
#zwroc_nazwisko()
#print("Wszystkie wyjatki obsluzone! Dobra robota!")
print("Nazwisko aktora brzmi %s" % zwroc_nazwisko())
