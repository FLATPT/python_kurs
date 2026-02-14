##5 Miniräknare
#3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.

tal1=float(input("Ange tal 1: "))
tal2=float(input("Ange tal 2: "))
tal3=float(input("Ange tal 3: "))

if tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
    print("Två av talen är lika")
if tal1 == tal2 == tal3:
    print("Alla tre talen är lika")
