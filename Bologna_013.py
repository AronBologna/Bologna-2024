for _ in range(10):
    print("ciao") 

    somma = 0
for numero in range(10, 21):
    somma += numero
print(somma)

somma_pari = 0
for numero in range(0, 31, 2):
    if numero % 2 == 0:
        somma_pari += numero
print(somma_pari)

prodotto = 1
for numero in range(1, 11):
    prodotto *= numero
print(prodotto)
