# Napisz funkcje "foo" i "bar" tak, aby mogły otrzymywać zmienną
# liczbę argumentów (3 lub więcej). Funkcja foo musi zwracać
# liczbę dodatkowych argumentów jakie otrzymała. Funkcja bar
# musi zwracać True, jeśli argument przypisany słowu kluczowemu
# magiczna_liczba jest równy 7, oraz False w przeciwnym razie.

def foo(a, b, c, *wiecej):
    return len(wiecej)

def bar(a, b, c, **wiecej):
    if(wiecej.get("magiczna_liczba") == 7):
        return True
    else:
        return False

# test kodu
if foo(1,2,3,4) == 1:
    print("Dobrze.")
if foo(1,2,3,4,5) == 2:
    print("Lepiej.")
if bar(1,2,3,magiczna_liczba = 6) == False:
    print("Bardzo dobrze.")
if bar(1,2,3,magiczna_liczba = 7) == True:
    print("Doskonale!")
