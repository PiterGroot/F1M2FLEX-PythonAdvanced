import random

class exampleClass:

    lives = 3
    moveSpeed = 6
    coins = 50
    id = "player1"

    def giveStats(self):
        print(self.coins, self.id, self.lives, self.moveSpeed)

    def points(self):
        print("your coins: ", self.coins)

class exampleClass1(exampleClass):

    jumpHeight = 7
    experience = 16
    itemCost = 135
    def points(self):
        print("you need " + (str(self.itemCost - self.coins)) + " coins to buy your item.")

    def giveStats(self):
        super().giveStats()
        print(self.jumpHeight, self.experience)

    def __init__(self):
        self.lives = 4
        self.moveSpeed = 3

Object = exampleClass()
Object1 = exampleClass1()
Object.points()
Object1.points()
Object1.giveStats()
