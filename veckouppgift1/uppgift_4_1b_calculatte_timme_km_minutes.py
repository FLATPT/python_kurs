#  4.1b Gör så att programmet svarar i minuter i stället för timmar.


km_stockholm_goteborg =470
hastighet = float(input("Skriv hur fort du vill köra mellan Stockholm till Göteborg i km/h: "))
# Räkna ut tid i timmar
timmar= km_stockholm_goteborg / hastighet
# Räkna ut tid i minuter
minuter= timmar * 60

# Svar till användare i minuter
print("Det tar " + str(int(minuter)) + " minuter att köra från Stockholm till Göteborg med en hastighet på " + str(int(hastighet)) +" km/h.")

