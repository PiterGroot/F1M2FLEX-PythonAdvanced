class Character :
    speed = 10
    sprite = None
    jumpHeight = 6
    def Walk(self):
        print("Character loopt nu", self.speed)


class Mario(Character) :
    lives = 3
    item = None
    def __init__(self):
        self.speed = 30
    def Jump(self):
        print("Mario springt met " + str(self.jumpHeight))

#Instansiate
characterA = Character()
MarioX = Mario()

MarioX.Walk()
characterA.Walk()
MarioX.Jump()

print(characterA.speed)
print(MarioX.speed)
print(MarioX.lives)

dontClose = input()
