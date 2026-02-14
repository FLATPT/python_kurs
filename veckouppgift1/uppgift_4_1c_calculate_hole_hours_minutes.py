# 4.1c (svårare) Nu ska programmet svara i hela timmar och minuter.
# Tips: använd operatorerna // och %. Heltalsdivision // dividerar och avrundar nedåt till närmaste heltal. Procent % räknar ut resten vid division med heltal.

km_stockholm_goteborg =470
hastighet = float(input("Skriv hur fort du vill köra mellan Stockholm till Göteborg i km/h: "))

# Räkna ut antal minuter totalt
minuter_total= (km_stockholm_goteborg / hastighet) * 60
# Räkna ut tid i hela timmar
timmar= int (minuter_total // 60)
# Räkna ut tid i hela minuter
minuter= int(minuter_total % 60)
# Svar till användare i minuter
print("Det tar cirka " + str(timmar) + " timmar och " + str(minuter) + " minuter att köra från Stockholm till Göteborg med en hastighet på " + str(hastighet) +" km/h.")




