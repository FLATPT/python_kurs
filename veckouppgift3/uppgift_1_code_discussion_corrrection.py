#1 Diskutera i grupp
#Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den.

#1 Vad skrivs ut?
print("Uppgift 1.1")
print("Vad skrivs ut?")
limit = 15
index = 5
while index <= limit:
    print(index)
    index = index + 2
print("SVAR: Siffrorna 5,7,9,11,13,15 skrivs ut")
print("\n***********************************************************************************")

#2 Vad skrivs ut?
print("\nUppgift 1.2")
print("Vad skrivs ut?")
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
    i= i + 1
print("SVAR: 0,1,2,3,4,,6,7,8,9")
print("\n***********************************************************************************")

#3 Vad blir summan? Skriv ner din bästa gissning innan du kör koden.
print("\nUppgift 1.3")
print("Vad blir summan?")
counter = 0 # räknar antal gånger loopen körs
for i in range(6): # range(6) = 0,1,2,3,4,5, loopen körs 6 gånger
    counter += 1 # varje gång loopen körs, 1 läggs till variabeln counter
print(counter)
print("SVAR: 6")
print("\n***********************************************************************************")

#4 Vad skrivs ut?
# För att förstå koden kan du sätta ut brytpunkter och köra med debugging.
# Det kan också underlätta att skriva samtidigt med papper och penna.
print("\nUppgift 1.4")
print("Vad skrivs ut?")

# x = 0
# y = 1
# while y < 10:
#     if y % 2 == 0: # Om y är jämnt, det vill säga delbart med 2 utan rest, så körs koden i if-satsen
#         x -= y        # Tips:sätt en brytpunkt här
#     else:             # Om y är udda, det vill säga inte delbart med 2 utan rest, så körs koden i else-satsen
#         x += y * y    # Tips:sätt en brytpunkt här

print("SVAR: y=1 och kommer alltid att vara udda, så x kommer att öka med y*y varje gång. Programmet kommer inte att sluta köras då y är alltid 1.")
print("\n***********************************************************************************")



#5 Vad skrivs ut?
#Kan du göra om koden så att den skriver ut "time" i stället?
print("\nUppgift 1.5")
message ="its_time_to_get_coding"
print(message[3:7])

print("SVAR: _tim")
print("\n***********************************************************************************")


#6 Vad skrivs ut?
#Kan du flytta linjen ett steg åt höger?
print("\nUppgift 1.6")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
print("\nSVAR: #.......,.#......,..#.....,...#....,....#...,.....#..")
print("\n***********************************************************************************")
