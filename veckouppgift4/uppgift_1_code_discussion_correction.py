# #1 Läsa och förstå kod - diskutera i grupp
# Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?

print("Uppgift 1a")
# 1a
def foo(t):
    print("test")
foo("hej")

print("SVAR: test. När functionen anropas")
print("\n***********************************************************************************")

print("Uppgift 1b")
def fun1(x, y):
    return x * y

print(3, 5)

print("SVAR: 3 5. Funktionen fun1 anropas inte. Det är endast det som står i print(3, 5) som skrivs ut")
print("\n***********************************************************************************")

print("Uppgift 1c")

def fun1(x, y):
    return x * y

print(fun1(3, 5))

print("SVAR: 15. Funktionen fun1 anropas i print(fun1(3, 5)) med parameter x=3 och y=5")
print("\n***********************************************************************************")


print("Uppgift 1d")

def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))  # a = fun2(fun2(2) + fun2(3))  -> a = fun2((5*2) + (5*3))   -> a = fun2(25)   -> a = fun2(5*25)  -> a =125
print(a)  # 125

print("SVAR: 125.")
print("\n***********************************************************************************")


print("Uppgift 1e")

a = 5
def fun3(a):  # fun3(5)
    a += 1    # 5 += 1 -> 6

a += 2        # 5 += 2 -> 7, pga av indentering är functionen fun3 resultat utanför den här raden och ränas inte iden. Så variable a är fortfarande a = 5 och 5 += 2 = 7
print(a)      # 7

print("SVAR: 7.")
print("\n***********************************************************************************")


print("Uppgift 1f")

def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)     # Eftersom x i detta fall är funktionen foo, blir samma sak som att anropa foo(3).

a = goo(foo, 3); # Inuti goo, kommer foo att anropas med 3 som argument, vilket innebär att foo(3) beräknas. foo returnerar 2*3*3 =18. Värdet 18 som returneras från goo(foo, 3) tilldelas variabeln a.
print(a)            # a = 18

print("SVAR: 18 ")
print("\n***********************************************************************************")


print("Uppgift 1g")
# Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False                # Om is_number int eller float så returneras True, annars False.

print(is_number(5.5))
print(is_number(42))
# int(is_number("hej"))

print("SVAR: True, True")
print("\n***********************************************************************************")


print("Uppgift 1h\n")

def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:   # Om item längd > 4 och < än 8 bokstäver, skall den läggs till i listan found.
            found.append(item)
    return found
average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"]))  # La till den här raden för att se resultatet av funktionen average_words. Det som skrivs ut är det som returneras i funktionen, alltså listan found.



print("\nSVAR: ['how's', 'going', 'coding']")
print("\n***********************************************************************************")

print("Uppgift 1i\n")
# 1i En uppgift i tre delar:
print("\n**** Del 1 ****")
print("Lista ut vad som är funktionens syfte, baserad på namn och sammanhang")
print("\nSVAR: Funktionen find_min ska hitta det minsta talet i en lista. Den tar en lista av numbers som argument och returnerar det lägsta talet i listan.")

print("\n**** Del 2 ****")
print("\nLista ut vad som ska vara det förväntade resultatet för de tre testlistorna.")
print("\nSVAR: Resultatet för find_min([10, 3, -4, -11]) bör vara -11. eftersom den är den lägsta talet i listan." +
      "\nResultatet för find_min([]) blir nog None då det inte finns något tal i listan." +
      "\nResultatet för find_min([100]) bör vara 100 eftersom det är det enda talet i listan.")

print("\n**** Del 3 ****")
print("\nRätta felen, så funktionen gör det den ska.")

def find_min(numbers):
    if not numbers:       # Hanterar om listan är tom. Om listan är tom, kan vi returnera None eller ett lämpligt meddelande.
        print(f"The smallest item is: None. The list is empty.")
        return None
    #counter = 0             # original kod
    counter = numbers[0]     # Korrigering för att hitta det minsta talet i listan, måste vi börja med att sätta counter till det första elementet i listan. Annars kommer counter alltid att vara 0, och om alla tal i listan är positiva så kommer counter aldrig att uppdateras.
    for item in numbers:
        if item < counter:
            counter = item

    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

print("\n***********************************************************************************")

