
import random
from weapons import Weapon
from dinos import Dino

current_weapon = Weapon("Lightsaber", random.randint(10,100))
current_dino = Dino("T-Rex", random.randint(10-50), 200)

class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = ""
        self.health = 200
        self.active_weapon = current_weapon

    def attack(self, dinosaur):
        dinosaur = current_dino
        if current_weapon.attack_power >= 25:
            current_dino.health = ((current_dino.health) - (current_weapon.attack_power))
            print(f"{self.name} has attacked {dinosaur} with {self.active_weapon}!")
            print(f"{current_dino} healt is at {current_dino.health}!")
        else:
            print("Dude! You didnt even scratch that thing!")
        