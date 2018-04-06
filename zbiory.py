#W ćwiczeniu poniżej utwórz zbiory A, B, C z odpowiednich tablic i wypisz następujące zbiory imion:

#Imiona, które są w przynajmniej w jednym ze zbiorów A, B i C (czyli zwykła suma);

#Imiona, które są jednocześnie w zbiorach A, B i C;

#Imiona, które są albo w zbiorze A, albo w sumie zbiorów B i C.

tablica_a = ['Anna', 'Monika', 'Joanna', 'Ewa', 'Karolina', 'Kacper', 'Dawid', 'Mateusz', 'Ewa', 'Bartosz']
tablica_b = ['Kuba', 'Paulina', 'Marzena', 'Zuza', 'Tomek', 'Ewa', 'Bartek', 'Olek', 'Jacek', 'Magda', 'Paulina']
tablica_c = ['Anastazja', 'Ewa', 'Monika', 'Anna', 'Karolina', 'Ola', 'Ula', 'Maciek', 'Paulina']

A=set(tablica_a)
B=set(tablica_b)
C=set(tablica_c)

print(A.union(B).union(C))
print("\n\n\n")
print(A.intersection(B.intersection(C)))
print("\n\n\n")
print(A.symmetric_difference(B.union(C)))
