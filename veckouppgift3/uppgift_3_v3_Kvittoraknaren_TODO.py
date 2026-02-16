# Version 3: programmet ska fråga hur många procent dricks man vill lägga på. Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.
#
# Nice to have: prova att använda try+except eller isdigit för att hantera de fall när användaren skriver ett felaktigt värde. Python Try Except , isdigit | StackOverflow
# ("Nice to have" handlar om funktionalitet som inte är nödvändig, men som är bra att ha. Gå gärna vidare till nästa uppgift och återvänd till den här om du vill lära dig mer.)


print("Uppgift 3 - Version 2")

number= input("\nHur många procent dricks man vill lägga på notan? ")
procentsats= int(number)
pris = 100

if str(procentsats) != "":
    dricks= pris * (procentsats / 100)
    att_betala = pris + dricks
    print("Det blir: " + str(att_betala) + " inklusive " + str(dricks) + "% dricks")
else:
    att_betala = pris * (10 / 100)
    print("Vi har lagt på vår base dricks på 10%. Det blir: " + str(att_betala))


#TODO: kontrollera att användaren lägger en tom string med try/except istället