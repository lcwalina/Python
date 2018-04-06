# przyklad
import re
# Ponizej jest dokonywana lekka optymalizacja naszego wyrazenia
pattern = re.compile(r"\[(on|off)\]")

# Teraz szukamy
re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")
# Zwroci obiekt Match
re.search(pattern, "Nada...:-(")
# Nic nie zwroci
# koniec przykladu

# Cwiczenie: skonstruj wyrazenie odpowiadajace adresowi email

def test_email(twoje_wyrazenie):
    wyrazenie = re.compile(twoje_wyrazenie)
    adresy = ["john@example.com", "python-list@python.org", '"wha.t.`1an?ug{}ly@email.com"']
    adresy_new =[ addr.strip("\"\'") for addr in adresy ]
    for adres in adresy_new:
        if not re.match(wyrazenie, adres):
            print("Nie udalo ci sie przyporzadkowac %s" % (adres))
        elif not twoje_wyrazenie:
            print("Nie wprowadziles wyrazenia do funkcji test_email")
        else:
            print("Dobrze")

#celowo dopasowałem tylko perwszy adres (za pomoca {4} - liczba znaków)
wyrazenie = r".{4}@.*\..*"
test_email(wyrazenie)
#mały eksperyment
wyrazenie = r"(.{4}|.{11}|.{17})@.*\..*"
test_email(wyrazenie)
