# Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
# Hur många är ni? 3
# Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!

# Testa programmet med följande inputs:
# Version 2:
# 100, 1 person
# 100, 2 personer
# 10, 10, 40 personer
# 30, 20, 30, 1 person


print("Uppgift 3 - Version 2")

number= input("\nHur många är ni? ")
antal_personer= int(number)
#print(antal_personer)

if antal_personer > 0:
    belopp = 10
    att_betala= belopp/antal_personer
    print("Det blir " + str(belopp) +" alltså " + str(att_betala) + " kr per person. Välkommen åter!")


