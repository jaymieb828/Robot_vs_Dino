
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
        print(f"{dino_1.name} attack power is {dino_1.attack_power}!")
        sleep(.5)
        print(f"{robot_1.name} attack power is {robot_1.attack_power}!")
        sleep(.5)

    def battle_phase(self):
        while dino_1.health and robot_1.health >= 0:
            robot_1.attack(dino_1)
            dino_1.health = dino_1.health - robot_attack
            print(f"{robot_1.name} has attacked {dino_1.name} with a {robot_1.weapon}!")
            sleep(.5)
            print(f"{dino_1.name}'s current health is {dino_1.health}!")
            sleep(.5)
            dino_1.attack(robot_1)
            robot_1.health = robot_1.health - dino_attack
            print(f"{dino_1.name} has attacked {robot_1.name}!")
            sleep(.5)
            print(f"{robot_1.name}'s current health is {robot_1.health}!")
            sleep(.5)

                        
    def display_winner(self):
        if robot_1.health <= dino_1.health:
            print(f"{dino_1.name} has defeated {robot_1.name} and ate him for dinner!")
            sleep(.5)
        elif dino_1.health <= robot_1.health:
            print(f"{robot_1.name} has terminated {dino_1.name}!")
        elif dino_1.health == robot_1.health:
            print("The battle is a draw.")
        
