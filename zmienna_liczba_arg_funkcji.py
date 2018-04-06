##funkcja dzielenie z Exc1. Dodatkwoy argument "reszta" jest listą(!)
def dzielenie(dzielna, dzielnik, *pozostale):
    if(dzielnik == 0):
        return f"SZIT, CHAMIE! {pozostale}"
    else:
        return dzielna / dzielnik

#print(dzielenie(5,0,1))
#print(dzielenie(5,5))

##słowa-jako argument - tutaj **opcje(też lista!)
def dzielenie(dzielna, dzielnik, **opcje):
    if(dzielnik == 0):
        return f"SZIT, CHAMIE!"
    if(opcje.get("jak_dzielic") == "z reszta"):
        return f"{int(dzielna / dzielnik)} reszta: {dzielna % dzielnik}"
    else:
     return dzielna / dzielnik

print(dzielenie(19,6, jak_dzielic = "z reszta"))
print(dzielenie(19,6))

###inny przykład (smaczek - formatownie napisów bez f-stringa)

def funkcja(pierwszy, drugi, trzeci, **opcje):
    if opcje.get("akcja") == "dodaj":
        print("Suma to: %d" % (pierwszy + drugi + trzeci))

    if opcje.get("zwroc") == "pierwszy":
        return pierwszy

wynik = funkcja(1, 2, 3, akcja = "dodaj", zwroc = "pierwszy")
print("Wynik: %d" % wynik)
