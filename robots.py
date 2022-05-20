from weapons import Weapon
import random

active_weapon = Weapon("lightsaber", (random.randint(5,50)))



class Robot:
    def __init__(self):
        self.name = "T1000"
        self.health = 200
        self.attack_power = active_weapon.attack_power
        self.weapon = active_weapon.name
    


    def attack(self, dino):
        dino.health = dino.health - self.attack_power
        

    # def attack(self, dinosaur):
    #     dinosaur = current_dino
    #     if current_weapon.attack_power >= 25:
    #         current_dino.health = ((current_dino.health) - (current_weapon.attack_power))
    #         print(f"{self.name} has attacked {dinosaur} with {self.active_weapon}!")
    #         print(f"{current_dino} healt is at {current_dino.health}!")
    #     else:
    #         print("Dude! You didnt even scratch that thing!")
        