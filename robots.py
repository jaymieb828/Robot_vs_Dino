from weapons import Weapon
import random

active_weapon = Weapon("lightsaber", (random.randint(25,50)))



class Robot:
    def __init__(self):
        self.name = "T1000"
        self.health = 200
        self.attack_power = active_weapon.attack_power
        self.weapon = active_weapon.name
    


    def attack(self, dino):
        dino.health = dino.health - self.attack_power
        

  