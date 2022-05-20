import random

class Dino:
    def __init__(self):
        self.name = "T-Rex"
        self.attack_power = (random.randint(0,50))
        self.health = 200


    def attack(self, robot):
        robot.health = robot.health - self.attack_power
        
    

    


        
    



