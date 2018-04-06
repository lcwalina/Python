from functools import partial

def mnozenie(x, y):
    return x * y

def potegowanie(x,y):
    return y**x

podwojenie = partial(mnozenie, 2)
do_piatej=partial(potegowanie,5)


print(podwojenie(6))  # 12
print(podwojenie(11)) # 22
print(podwojenie(7))  # 14

print(do_piatej(2)) #32
