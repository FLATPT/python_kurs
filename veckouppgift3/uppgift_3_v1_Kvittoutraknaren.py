#Gör ett program som upprepade gånger ber användaren skriva in ett tal. När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen. Exempel:
#Välkommen till Kvittokompis! Avsluta genom att skriva: quit
# Skriv in ett belopp: 25
# Skriv in ett belopp: 50
# Skriv in ett belopp: quit
# Det blir 75 kr totalt. Välkommen åter!
#
# Tips! För att lösa uppgiften behöver du: flera variabler, input, while-loop.
# Testa programmet med följande inputs:
# Version 1:
# 100
# 10, 20, 15


print("Uppgift 3")

print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
number= input("Skriv in ett belopp: ")
summa= 0

while number != "quit" and number != "avsluta":
    summa += int(number)
    number= input("Skriv in ett belopp: ")
print("Det blir " + str(summa) +" kr totalt. Välkommen åter!")


