dip1 = {
    "Nome" : "Fabrizio",
    "Ruolo" : "Attore",
    "Stipendio" : 6500
}
dip2 = {
    "Nome" : "Malena",
    "Ruolo" : "Attrice",
    "Stipendio" : 7900
}
dip3 = {
    "Nome" : "Mauro",
    "Ruolo" : "Camera Man",
    "Stipendio" : 4700
}
dip4 = {
    "Nome" : "il MARO",
    "Ruolo" : "Nessuno",
    "Stipendio" : 0.40
}

x = dip1["Nome"]
y = dip2["Nome"]
z = dip3["Nome"]
a = dip4["Nome"]
print("",x,"\n",y,"\n",z,"\n",a)

progetto = {
    "Budget iniziale" : 50000,
    "Costo orario" : 50
}
azienda = [dip1,dip2,dip3,dip4,progetto]

ore_disponibili = progetto["Budget iniziale"] / progetto["Costo orario"]

nome_dip1 = dip1["Nome"]
tot_ore1 = int(input(f"Inserire la quantità di ore lavorative di {nome_dip1}:"))
nome_dip2 = dip2["Nome"]
tot_ore2 = int(input(f"Inserire la quantità di ore lavorative di {nome_dip2}:"))
nome_dip3 = dip3["Nome"]
tot_ore3 = int(input(f"Inserire la quantità di ore lavorative di {nome_dip3}:"))
nome_dip4 = dip4["Nome"]
tot_ore4 = int(input(f"Inserire la quantità di ore lavorative di {nome_dip4}:"))

budget_rim = progetto["Budget iniziale"] - (tot_ore1 + tot_ore2 + tot_ore3 + tot_ore4)* progetto["Costo orario"]

progetto["Budget rimanente"] = budget_rim

dip1["Stipendio"] = dip1["Stipendio"] + tot_ore1 * progetto["Costo orario"]
dip1["Ore aggiuntive"] = tot_ore1
dip2["Stipendio"] = dip2["Stipendio"] + tot_ore2 * progetto["Costo orario"]
dip2["Ore aggiuntive"] = tot_ore2
dip3["Stipendio"] = dip3["Stipendio"] + tot_ore3 * progetto["Costo orario"]
dip3["Ore aggiuntive"] = tot_ore3
dip4["Stipendio"] = dip4["Stipendio"] + tot_ore4 * progetto["Costo orario"]
dip4["Ore aggiuntive"] = tot_ore4

if progetto["Budget rimanente"] < 0:
    print("Il budget del progetto è stato superato\ndi conseguenza il progetto non potrà essere sviluppato.")
else:
    for i in azienda:
        print(i)