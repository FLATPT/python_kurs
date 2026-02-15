#1 Diskutera i grupp
#Ni kan göra den här uppgiften antingen direkt, eller senare i veckan. Om ni gör den senare, passa på att kombinera med code review.
#1. Vad är syftet med koden?
# Koden beräknar rabatt baserat på köpbelopp: Inköp över 100 kr ger +10%, och över 300 kr ger ytterligare +25% rabatt.
#Original kod

# is_member = False
# level1 = 100
# level2 = 300
# discount = 0
# price = input("Välkommen,köp något dyrt: ")
# price = float(price)
# if price > level1:
#     print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
#     discount = discount + 10
# if price > level2:
#     print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
#     discount = discount + 25
# final_price = price * (100 - discount) / 100
# print("Efter rabatter blir priset.... " + final_price)


#2. Test kör koden med några olika värden.
# price = 80 discount= 20, result = Efter rabatter blir priset .... 80.0
# price = 110 discount= 20, result = Grattis! Du har avancerat till nivå 1 och får 20% rabatt.  Efter rabatter blir priset .... 88.0
# price = 301 discount= 20, result = Grattis! Du har avancerat till nivå 1 och får 20% rabatt. Grattis! Du har avancerat till nivå 2 och får 25% rabatt.  Efter rabatter blir priset .... 165.55

#3. Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
# Variabel final_price är en float behöver omvandlas till str i raden print("Efter rabatter blir priset .... " + final_price).
# Kod revision print("Efter rabatter blir priset .... " + str(final_price))

#4. Finns det logiska fel? (programmet gör något annat än det är tänkt)
# Om priset är över 300 kr, så kommer både nivå 1 och nivå 2 att aktiveras, total rabatt blir på 35% istället för 25%.
# Om är < = 100 kr, så kommer ingen rabatt att ges, slut text bör visa att det ingår inte rabatt i köpet för tydlighetens skull.

#5. Diskutera möjliga lösningar på felen ni hittat.
# Programmet skall endast visa värde vid varje nivå och inte summera rabatt verden för nivå 1 och 2
#6. Diskutera möjliga förbättringar på koden.
# När priset inte når någon rabatt nivå, programmet bör visa det
# Visa hur mycket rabatt beloppet är

is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen,köp något dyrt: ")
price = float(price)
if level1 < price < level2:  # Kod revision: Om priset är < level 2 och <level1 programmet skriver endast värdet för rabatt nivå 1.
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
elif price > level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25
else:
    # print("Det blev tyvärr ingen rabatt på just det här köpet. \nSlut priset är: "  + str(price))
    print("Det blev tyvärr ingen rabatt på just det här köpet.\nPris: " + str(price) + "\nRabatt: " + str(discount) + "\nSlutpris: " + str(price))

if discount > 0:
    discount_amount =  price * discount / 100
    final_price = price * (100 - discount) / 100
   # print("Efter rabatt på " + str(discount_amount) + ", slut priset är: " + str(final_price))  # Kode revision: str(final_price) för att undvika TypeError när man försöker konkatenera en float med en str.
    print("Pris: " +  str(price) + "\nRabatt: " + str(discount_amount) + "\nSlutpris: " + str(final_price))


