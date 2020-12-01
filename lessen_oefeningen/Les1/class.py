class Hallo :
    _welkom = "Hallo"
    _haha = "HAHAHAHAHAH"

    def Test(self):
        print("Welkom bericht is: ", self._welkom)

    def __init__(self, lives):
        self.lives = lives



instantieHallo = Hallo(300)
print(instantieHallo._haha)
instantieHallo.Test()
instantieHallo._welkom = "NIET MEER HALLO"
instantieHallo.Test()
print(instantieHallo.lives)

dontClose = input()
