#5 Miniräknare
#2 Programmet ska tala om vilket som är det största talet, utan att använda Python-funktionen max.
# Använd i stället if/elif/else. Fundera på om man kan lösa uppgiften på olika sätt.

tal1=float(input("Ange tal 1: "))
tal2=float(input("Ange tal 2: "))
tal3=float(input("Ange tal 3: "))

if tal1 > tal2 and tal1 > tal3:
    print("Tal 1 är det största talet")
elif tal2 > tal1 and tal2 > tal3:
    print("Tal 2 är det största talet")
elif tal3 > tal1 and tal3 > tal2:
    print("Tal 3 är det största talet")
else:
    print("Inget tal är störst")
