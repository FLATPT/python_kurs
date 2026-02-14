# 2. Denna kod ska räkna ut hur mycket som blir kvar, efter att man betalat en biljett. Pengarna som blir över ska du dela med en vän.
# Men koden är inte testad. Finns det några fel i koden?

# Original code with code review

#x = 100  # biljettpris
#y = 200  # pengar på fickan
#print("Det blir " + (y - x) " kronor över.") # As x and y are of type int the values should be converted to a str. The + sign between (y - x) " kronor över." is missing
#z = y - x / 2  # As x and y were converted to data type str in the previous row, they are now re-converted to in to be able to run the calculation
#print("Varje person får " + z) # As the z result is an int, adding it to the string message the z has to be converted from str to int to get the correct result


#Code correction
ticket_price = 100
money_in_pocket = 200
money_left_after_pay = money_in_pocket - ticket_price
print("Det blir " + str(money_left_after_pay) + " kronor över.")
money_left_per_person = int(money_left_after_pay) / 2
print("Varje person får " + str(money_left_per_person))
