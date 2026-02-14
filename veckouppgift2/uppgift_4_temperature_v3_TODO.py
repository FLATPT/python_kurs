#4 Temperaturomvandling
#Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta på sig vinterkläder.
# Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.

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
celsius_calculation = float(temperature_value -32)/1.8
fahrenheit_calculation = float(1.8 * temperature_value + 32)

if temperature_type == "C" or temperature_type == "c":
    print("Det blir " + str(fahrenheit_calculation)+ " grader Fahrenheit.")
elif temperature_type == "F" or temperature_type == "f":
    print("Det blir " + str(celsius_calculation) + " grader Celsius.")


# ****    TO DO  *****
if celsius_calculation < 10:
    print("Sätt på vinterkläder!")

elif celsius_calculation >= 20:
    print("Packa badkläder!")