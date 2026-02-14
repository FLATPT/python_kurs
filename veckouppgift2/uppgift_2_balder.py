#2 Balder
#För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!
#Fråga användaren hur lång man är (i cm)
#Skriv ut antingen "Du får åka!" eller "Du får inte åka"

#Skriv in följande värden för att testa att ditt program gjort rätt:
#121 cm (får inte åka)
#130 cm (får åka)
#155 cm (får åka)

#Diskutera:
#Varför just tre värden?
#De tre värden testar de tre möjliga fallen då åkaren kan vara kortare, lika lång eller längre än den lägsta tillåtna längd på 130 cm.
#Varför dessa värden?
# De är exemple längd värde på de tre olika fallen. Om den lägsta tillåtna längd är 130 cm, 121 cm är kortare, 130 cm är lika lång och 155 cm är längre.
#Skulle det vara bra att lägga till testvärdet 129 cm?
# Det skulle inte skada men det skulle inte tillföra en annorlunda resultat än värde 121 cm. Testet om värden är < 130 är täcks med test värde 121 cm.

height = float(input("Hur lång är du i cm? "))

if height >= 130:
    print("Du får åka!")
elif height < 130:
    print("Du får inte åka")