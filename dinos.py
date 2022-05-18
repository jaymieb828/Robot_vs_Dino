
from robots import Robot

import random

current_robot = Robot("", 200, random.randint(20,50))


class Dino:
    def __init__(self, name, attack_power, health):
        self.name = ""
        self.attack_power= ()
        self.health = 200
    

    def attack(self, robot):
        robot = current_robot
        if self.attack_power >= 25:
            robot.health = ((robot.health) - (self.attack_power))
            print(f"{self.name} has attacked {current_robot} with {self.attack_power}% power!")
            print(f"{current_robot} health is at {robot.health}!")
        elif robot.health <= 0:
            print(f"Game over! {self.name} wins!")
        else:
            print("Dude! You didnt even scratch that thing!")
        
    



