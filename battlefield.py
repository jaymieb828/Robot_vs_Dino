
from dinos import Dino
from robots import Robot

robot_1 = Robot()
dino_1 = Dino()
robot_attack = robot_1.attack_power

class Battlefield:
    def __init__(self):
        self.robot_1= robot_1.name
        self.dino_1 = dino_1.name
    
    def run_game(self):
        while dino_1.health and robot_1.health >= 0:
            robot_1.attack(dino_1)
            dino_1.health = dino_1.health - robot_attack
            print(f"{robot_1.name} has attacked {dino_1.name} with a {robot_1.attack_power}!")
            print(f"Your {dino_1.name}'s current health is {dino_1.health}!")
            robot_1.health = robot_1.health - dino_1.attack_power
            dino_1.attack(robot_1)
            print(f"{dino_1.name} has attacked {robot_1.name}!")
            print(f"{robot_1.name}'s current health is {robot_1.health}!")
        if dino_1.health <= 0:
            print(f"{dino_1.name} is EXTINCT! {robot_1.name} wins!")
        elif robot_1.health <= 0:
            print(f"{robot_1.name} has been terminated! {dino_1.name} wins!")
            
    
        
        

        
    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
