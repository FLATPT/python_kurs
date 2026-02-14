#1 Diskutera i grupp
#Ni kan göra den här uppgiften antingen direkt, eller senare i veckan. Om ni gör den senare, passa på att kombinera med code review.
#1. Vad är syftet med koden?
# Koden beräknar rabatt baserat på köpbelopp: Över 100 kr ger +10%, och över 300 kr ger ytterligare +25% rabatt (totalt 35%).

#2. Testkör koden med några olika värden.
# price = 80 discount= 20, result = Efter rabatter blir priset .... 64.0
# price = 110 discount= 20, result = Grattis! Du har avancerat till nivå 1 och får 10% rabatt.  Efter rabatter blir priset .... 77.0
# price = 301 discount= 20, result = Grattis! Du har avancerat till nivå 1 och får 10% rabatt. Grattis! Du har avancerat till nivå 2 och får 25% rabatt.  Efter rabatter blir priset .... 135.45

#3. Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
# Variabel final_price är en float behöver omvandlas till str i raden print("Efter rabatter blir priset .... " + final_price).
# Kod revision print("Efter rabatter blir priset .... " + str(final_price))

#4. Finns det logiska fel? (programmet gör något annat än det är tänkt)
#5. Diskutera möjliga lösningar på felen ni hittat.
#6. Diskutera möjliga förbättringar på koden.

is_member = False
level1 = 100
level2 = 300
discount =0

price = input("Välkommen,köp något dyrt: ")
price = float(price)
if price > level1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
if price > level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset .... " + str(final_price))

