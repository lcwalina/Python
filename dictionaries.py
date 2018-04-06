kontakty = {
"Stefan" : 111111111,
"John" : 222222222,
"Kamila" : 333333333
}

for imie in kontakty:
    print(f"{imie} ma numer telefonu: {kontakty[imie]}")

print("\n\n")
kontakty["Jakub"] = 938273443
del kontakty["Kamila"]

for imie in kontakty:
    print(f"{imie} ma numer telefonu: {kontakty[imie]}")
