# 1 Skriv en funktion som tar en sträng som parameter. När den anropas ska den skriva ut strängen och "är en fena på programmering". Exempel:
# my_function("David") → "David är en riktig hacker"
def ange_namn(namn):
    print(f"{namn} är en fena på programmering")

# 2a Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. Exempel:
# eko("hej") → skriver ut "hejhej"
def eko(string):
    print(2 * string)

# 2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas. Exempel:
# eko("hej", 3) → skriver ut "hejhejhej"
def eko_count(string, count):
    print(string * count)

#3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.
# end = 5
# y = 1
# for x in range(1, 100):
#     y *= 2
#     # avsluta loopen med en if-sats här
# print(y)

def loop(end):            # Parameter "end" avgör när loopen ska avslutas
    y = 1
    for x in range(1, 100):
        y *= 2
        print(f"Varv {x}: y = {y}")  # visar resultatet varje varv
        if x == end:  # om x når värdet av "end", dvs x=5 och end =5, avsluta loopen
            break
    print(y)


#4 Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.
#last([1, 2, 3]) → 3