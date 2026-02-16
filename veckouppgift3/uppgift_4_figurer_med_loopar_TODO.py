#4 Figurer med loopar
#Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)