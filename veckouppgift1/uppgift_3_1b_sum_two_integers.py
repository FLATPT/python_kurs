# 3.1b- Fråga användaren efter ett annat heltal. Skriv ut summan av talen, alltså tal1 + tal2.
#  Testa genom att hitta på två tal och räkna ut summan i huvudet. Kontrollera om programmet räknar rätt.

tal1 = input("Please, input an integer number for tal1: ")
tal2 = input("Please, input an integer number for tal2: ")
tal1_int = int(tal1)
tal2_int = int(tal2)
tal_sum = tal1_int + tal2_int
print("The sum of tal1 + tal2 = " + str(tal_sum))

