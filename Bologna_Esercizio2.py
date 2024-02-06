anno = int(input("Inserisci un anno: "))
if anno > 0 and anno < 2100:

if anno % 400 == 0:
 print("L'anno", anno, "E' Bisestile")

elif anno % 4 == 0 and anno % 100 != 0:
 print("L'anno", anno, "E' Bisestile")

else:
 print("L'anno", anno, "Non é Bisestile")
    
else:
 print("Input non accettato. Riprova, inserendo un anno che è compreso fra 1 e 2099.")