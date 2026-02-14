#3 Sportresultat
#Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
#Exempel på output:
#Matchen är över, nu ska vi räkna ut resultatet!
#Hur många mål gjorde Tottenham? 2
#Hur många mål gjorde Liverpool? 1
#Tottenham vann!

#Version 2: programmet ska tala om ifall det blev oavgjort.

#Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
#Tottenham vann med 1 mål!

#Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.
print("******************************************")
print("Champions League: Tottenham - Liverpool")
print("******************************************\n")

print("Matchen är över, nu ska vi räkna ut resultatet!\n")
lag_1= int(input("Hur många mål gjorde Tottenham? "))
lag_2 = int(input("Hur många mål gjorde Liverpool? "))

if lag_1 > lag_2:
    print ("Tottenham vann!")
    tottenham_goals_difference = (print("Tottenham vann med " + str(lag_1 - lag_2) + " mål!"))
elif lag_1 < lag_2:
    print ("Liverpool vann!")
    liverpool_goals_difference = (print("Liverpool vann med " + str(lag_2 - lag_1) + " mål!"))
elif lag_1 == lag_2:
    print("Resultatet blev oavgjort!")


#Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.
#lag_1 = 2, lag_2 = 1, expected result = Tottenham vann! Tottenham vann med 1 mål!
#lag_1 = 2, lag_2 = 3, expected result = Liverpool vann! Liverpool vann med 1 mål!

#lag_1 = 1, lag_2 = 1, expected result = Resultatet blev oavgjort!