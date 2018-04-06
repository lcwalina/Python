def lista_korzysci():
    return ["Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby"]

def buduj_zdanie(info):
    return info + " jest zaleta funkcji!"

tablica=lista_korzysci()

for element in tablica:
    print(buduj_zdanie(element))
