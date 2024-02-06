voti_validi = 0

for i in range(5):
    voto = int(input("Inserisci il voto: "))
    
    if voto >= 1 and voto <= 10:
        voti_validi += 1
        
        if voto >= 6:
            print("Il voto", voto, "è sufficiente.")

print("Voti validi:", voti_validi)