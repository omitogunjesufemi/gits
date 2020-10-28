KILOGRAMS = 1
POUNDS = 20
print(format("Kilograms", "<10s"),   format("Pounds", "<7s"), format("|", "<2s"), format("Pounds", "<7s"),   "Kilograms")
while (KILOGRAMS < 200) and (POUNDS < 516):
    pounds = KILOGRAMS * 2.205
    kilograms = POUNDS / 2.205
    print(format(KILOGRAMS, "<11.0f"), format(pounds, "<6.2f"), format("|", "<2s") , format(POUNDS, "<6.0f"),   format(kilograms, "8.2f") )
    KILOGRAMS += 2
    POUNDS += 5