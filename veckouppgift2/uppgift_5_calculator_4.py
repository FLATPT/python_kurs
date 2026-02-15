###5 Miniräknare
#4 Programmet ska tala om vilket som är det mellersta talet.
# Observera att det bara finns ett mellersta tal om alla tre är olika, eller alla tre är lika.
# (Om talen skulle vara till exempel 2, 2, 5 så räknas inget av dem som mellerst i den här uppgiften.)

#För att testa systematiskt kan du göra en tabell. Kör sedan programmet. Kontrollera att programmet skriver ut samma saker som du har skrivit in i tabellen. Vi kallar talen t1, t2 och t3.
#Förslag på värden att testa med:  1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16

tal1=float(input("Ange tal 1: "))
tal2=float(input("Ange tal 2: "))
tal3=float(input("Ange tal 3: "))

 # Kolla om precis två tal är lika (otillåtet enligt uppgiften)
if (tal1 == tal2 or tal2 == tal3 or tal1 == tal3) and not (tal1 == tal2 == tal3):
    print("Inget mellersta tal.")
else:
# Hitta det mellersta talet om alla tre är olika eller alla tre är lika
    if (tal2 <= tal1 <= tal3) or (tal3 <= tal1 <= tal2):
        mellersta = tal1
    elif (tal1 <= tal2 <= tal3) or (tal3 <= tal2 <= tal1):
        mellersta = tal2
    else:
        mellersta = tal3

    print("Mellersta talet är:", mellersta)