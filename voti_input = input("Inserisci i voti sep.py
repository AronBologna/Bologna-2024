voti_input = input("Inserisci i voti: ")
voti = voti_input()

num_voti_sufficienti = 0
num_voti_validi = 0

for voto in voti:
voto = int(voto)
if voto >= 1 and voto <= 10:
num_voti_validi += 1
if voto >= 6:
num_voti_sufficienti += 1

print("Voti sufficienti:", num_voti_sufficienti)
print("Voti validi:", num_voti_validi)

