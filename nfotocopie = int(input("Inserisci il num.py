nfotocopie = int(input("Inserisci il numero di fotocopie: "))
Nome_cliente = input("Inserisci il nome del cliente : ")
Rilegatura = input("Le fotocopie sono da rilegare? : ")

if Rilegatura == "s":
Costo_rilegatura = 1.80
else:
Costo_rilegatura = 0

if nfotocopie >= 1 and nfotocopie <= 19:
Costo_unitario = 0.10
elif nfotocopie >= 20 and nfotocopie <= 100:
Costo_unitario = 0.08
else:
Costo_unitario = 0.05

Costo_totale = (Costo_unitario * nfotocopie) + Costo_rilegatura

print("Gentile Sig. " + Nome_cliente + ", Il suo preventivo è di " + str(Costo_totale) + " euro", end =" ")
if Rilegatura == "s":
print("Compresa la rilegatura.")
else:
print(".")