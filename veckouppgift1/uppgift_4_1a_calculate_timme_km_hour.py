#4.1a- Det är ca 470 km mellan Stockholm och Göteborg.
#   Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.
#   Du behöver fråga användaren hur fort man ska köra, i km/h. Svara i timmar.

km_stockholm_goteborg =470
hastighet = float(input("Skriv hur fort du vill köra mellan Stockholm till Göteborg i km/h: "))
# Räkna ut tid i timmar
timmar= km_stockholm_goteborg / hastighet
# Svar till användaren i timmar
print("Det tar " + str(timmar) + " timmar att köra från Stockholm till Göteborg med en hastighet på " + str(int(hastighet)) +" km/h.")
