class exampleClass:
    _year = 2020
    _month = "december"
    _day = ""

    def __init__(self, day):
        self._day = day

    def giveDate(self):
        print("De datum is:", self._day, self._month, self._year)


exampleClassInstance = exampleClass("maandag 30")

exampleClassInstance.giveDate()

dontClose = input()

#MINIMUM EIS OPDRACHT
#ZIE MAIN.PY VOOR DE EXTRA OPDRACHT 
