# 3.2a- Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor.
#  Jackan är på rea och kostar 75% av originalpriset.
#  Skriv ett program som räknar ut hur mycket du behöver betala.
#  Använd variabeln:  rea_procent = 75.0

jacka_original_pris = 2000
rea_procent = 75.0
# Räkna ut rabattens belopp
rabatt_belopp = jacka_original_pris * (rea_procent/100)
# Räkna ut belopp att betala efter rea avdrag
belopp_att_betala=jacka_original_pris - rabatt_belopp
print("Belopp att betala för jackan efter rabattavdrag = " + str(belopp_att_betala))


