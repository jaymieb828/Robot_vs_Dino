import random

class Dino:
    def __init__(self, name):
        self.name = name
        self.attack_power = (random.randint(0,15))
        self.health = 200


    def attack(self, robot):
        robot.health = robot.health - self.attack_power 
        print (robot.health)
    

    

    # def attack(self, robot):
        
    



