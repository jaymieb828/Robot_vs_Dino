
from re import T
import re
from dinos import Dino
from robots import Robot
from time import sleep

robot_1 = Robot()
dino_1 = Dino()
robot_attack = robot_1.attack_power
dino_attack = dino_1.attack_power



class Battlefield:
    def __init__(self):
        self.robot_1= robot_1.name
        self.dino_1 = dino_1.name
    
    def run_game(self) -> None:
        self.display_welcome()
        self.battle_phase()
        self.display_winner()    
        
       
    
        
    def display_welcome(self):
        print("WELCOME TO ROBOT VS DINOSAUR!")
        sleep(.5)
        print(f"In this battle, {dino_1.name} faces {robot_1.name} in a fight to the death!")
        sleep(.5)
        
    def battle_phase(self):
        while dino_1.health and robot_1.health >= 0:
            robot_1.attack(dino_1)
            print(f"{robot_1.name} has attacked {dino_1.name} with a {robot_1.weapon}!")
            sleep(.5)
            print(f"{dino_1.name}'s current health is {dino_1.health}!")
            sleep(.5)
            if dino_1.health <= 0:
                break
            dino_1.attack(robot_1)
            print(f"{dino_1.name} has attacked {robot_1.name}!")
            sleep(.5)
            print(f"{robot_1.name}'s current health is {robot_1.health}!")
            if robot_1.health <= 0:
                break
            sleep(.5)
            # continue
        if dino_1.health or robot_1.health <=0:
            return False

                        
    def display_winner(self):
        if robot_1.health <= dino_1.health:
            print(f"{dino_1.name} has defeated {robot_1.name} and ate him for dinner!")
            sleep(.5)
        elif dino_1.health <= robot_1.health:
            print(f"{robot_1.name} has terminated {dino_1.name}!")
        else:
            print("The battle is a draw.")
        
