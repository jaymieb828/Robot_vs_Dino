from weapons import Weapon

active_weapon = Weapon("Lightsaber")

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.attack_power = active_weapon.attack_power


    def attack(self, dino):
        print(dino.health)
        pass
        

    # def attack(self, dinosaur):
    #     dinosaur = current_dino
    #     if current_weapon.attack_power >= 25:
    #         current_dino.health = ((current_dino.health) - (current_weapon.attack_power))
    #         print(f"{self.name} has attacked {dinosaur} with {self.active_weapon}!")
    #         print(f"{current_dino} healt is at {current_dino.health}!")
    #     else:
    #         print("Dude! You didnt even scratch that thing!")
        