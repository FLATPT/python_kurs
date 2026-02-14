# 3.2b Gör om programmet så att användaren kan skriva in en procentsats.
#  Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, innan du kör det.
#  Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.

pris = 2000
procentsats=float(input("Skriv in en procentsats:  "))
# Räkna ut priset efter procentsatsavdrag
rabatt = pris * (procentsats/100)
att_betala = pris - rabatt

print("Då jackan kostar "+ str(pris) + "kr vid " + str(int(procentsats))+ "% avdrag, kostar jackan " + str(int(att_betala)) + "kr")

