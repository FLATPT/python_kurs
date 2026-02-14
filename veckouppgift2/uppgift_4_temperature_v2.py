#4 Temperaturomvandling
#Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit. Sedan räknar programmet om till den andra temperaturen.
#Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i Fahrenheit. Använd sedan if + else.

# Formel för konvertering mellan temperaturenheter:
#  C = (F - 32) / 1.8
#  F = 1.8 * C + 32

#Förslag på värden att testa med:
#° Celsius: 0, -17.777…, 37.777…, 100
#° Fahrenheit: 32, 0, 100, 212


print("\n*** Temperatur omvandlare from Celsius till Fahrenheit ***\n")


temperature_type = input("Skriv 'C' for att ange temperatur i Celsius eller 'F' for att ange temperatur i Fahrenheit: ")
temperature_value =  float(input("Skriv in en temperaturen: "))


#Räkna temperaturen till grader Fahrenheit


if temperature_type == "C":
    fahrenheit_calc = float(1.8 * temperature_value + 32)
    print("Det blir " + str(fahrenheit_calc)+ " grader Fahrenheit.")
elif temperature_type == "F":
    celsius_calculation = float(temperature_value - 32) / 1.8
    print("Det blir " + str(celsius_calculation) + " grader Celsius.")
