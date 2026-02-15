print("Uppgift 1a \nSkriv färdigt kodexemplet.")
answer = 0
for i in range(1,11):   # urprungs kod var "for i in ????????????:"
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

print("\nSVAR: La till range(1,11) i for-loopen, så att i tar värdena 1,2,3,4,5,6,7,8,9 och 10. Varje gång loopen körs så läggs i till variabeln answer. När loopen är klar så skrivs svaret ut.")
print("\n***********************************************************************************")


print("\nUppgift 1b")
print("Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)")

data= "1, 2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ,100"
token_list = data.split(",")  # split() delar upp strängen data i mindre delar, så kallade tokens, baserat på det tecken som anges inom parentesen. I det här fallet är det ett kommatecken, så varje gång ett kommatecken hittas i strängen data, delas den upp i en token. Resultatet är en lista av tokens som kan användas för vidare bearbetning.
sum_so_far= 0
for token in token_list:
    token_number= int(token.strip())  # varje token är en sträng, så jag konverterar den till ett heltal
    sum_so_far= sum_so_far + token_number  # varje token är en sträng, så jag konverterar den till ett heltal innan jag lägger till den i sum_so_far
print("Summan av alla talen är: " + str(sum_so_far))

print("\n***********************************************************************************")

print("\nUppgift 1c")
print("Skriv om 1b så att den använder en while-loop.")

token = 1
sum_so_far=0

while token <= 100:
    sum_so_far += token  #
    token += 1
print("Summan av alla talen är: " + str(sum_so_far))

print("\n***********************************************************************************")


print("\nUppgift 2")
print("Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]")  # resultatet ska bli 1

lista = [1, -2, 3, -2, 4, -3]
sum_so_far = 0
for i in lista:   # i står för varje element i listan, så i kommer att ta värdena 1, -2, 3, -2, 4 och -3 under loopen
    sum_so_far += i
print("Summan av alla elementen i listan är: " + str(sum_so_far))


print("\n***********************************************************************************")


print("\nUppgift 3")
print("Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.")
print("\n3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan med funktionen print.")

film_lista = ["The color purple", "Schindler's list", "The Piano", "Gone with the wind"]
print(film_lista)


print("\n3b Lägg till 'Fellowship of the ring' sist i listan.")
film_lista = ["The color purple", "Schindler's list", "The Piano", "Gone with the wind"]
film_lista.append ("Fellowship of the ring")
print(film_lista)


print("\n3c Lägg till 'The two towers' på första platsen i listan. (index noll)")
film_lista.insert(0,"The two towers")
print(film_lista)


print("\n3d Ta reda på vilken position (index) 'Fellowship of the ring' har nu.")
#film_lista.index('Fellowship of the ring')
print("Filmen 'Fellowship of the ring' har index "+ str(int(film_lista.index('Fellowship of the ring'))) + " i listan.")


print("\n3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?")
print(film_lista)
film_lista.remove("The Piano")
print(film_lista)
print("JA, filmen 'Fellowship of the ring' har nu index 4 i listan, eftersom den har flyttats på när 'The Piano' togs bort.")


print("\n3f Ta reda på hur lång listan är. (len)")
print("Listan har " + str(len(film_lista)) + " element.")


print("\n3g Vänd listan baklänges.")
print("Listan i ordning är: " + str(film_lista))
film_lista.reverse()
print("Listan i omvänd ordning är: " + str(film_lista))


print("\n3h Sortera listan stigande i bokstavsordning.")
print(film_lista)
film_lista.sort()
print("Listan i bokstavsordning är: " + str(film_lista))