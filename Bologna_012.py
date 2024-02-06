n = int(input("Quanti valori si desidera inserire? "))
somma = 0

for i in range(n):
    valore = int(input("Inserire il valore: "))
    somma += valore

print("La somma dei valori è", somma)