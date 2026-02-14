#4 Temperaturomvandling
#Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
#Version 1, exempel på output:
#Skriv in en temperatur i grader Celsius: 22
#Det blir 71.6 grader Fahrenheit.

#Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit. Sedan räknar programmet om till den andra temperaturen.
#Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i Fahrenheit. Använd sedan if + else.

#Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta på sig vinterkläder.
# Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.

# Formel för konvertering mellan temperaturenheter:
#  C = (F - 32) / 1.8
#  F = 1.8 * C + 32

#Förslag på värden att testa med:
#° Celsius: 0, -17.777…, 37.777…, 100
#° Fahrenheit: 32, 0, 100, 212


print("\n*** Temperatur omvandlare from Celsius till Fahrenheit ***\n")

celsius = float(input("Skriv in en temperatur i grader Celsius: "))
#Räkna temperaturen till grader Fahrenheit
fahrenheit = float(1.8 * celsius + 32)

print("Det blir " + str(fahrenheit)+ " grader Fahrenheit.")

