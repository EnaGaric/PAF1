from decimal import Decimal

a = 5.0 - 4.935
b = 0.1 + 0.2 + 0.3
print(a)
print(b)

if b == 0.6:
    print("Dobijena je očekivana vrijednost")
else:
    print("Python koristi binarnu reprezentaciju brojeva. Mi dobivamo aproksimaciju matematičku, a ne precizan broj.")
print("Postoji način da se ovo zaobiđe pomoću import decimal.")

c = Decimal("0.1") + Decimal("0.2") + Decimal("0.3")
if c == Decimal("0.6"):
    print("Dobijen je točan rezultat.")
else:
    print("Greška u kodu")

print("---------")
print("---------")

from decimal import Decimal

def f(N):
    x = Decimal("5")
    one_third = Decimal("1") / Decimal("3")

    for i in range(N):
        x += one_third
        x -= one_third   # odmah poništi u istom koraku

    return x

for N in [200, 2000, 20000]:
    print(f(N))