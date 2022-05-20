
from dinos import Dino
from robots import Robot

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
        
        # while dino_1.health and robot_1.health >= 0:
        #     robot_1.attack(dino_1)
        #     dino_1.health = dino_1.health - robot_attack
        #     print(f"{robot_1.name} has attacked {dino_1.name} with a {robot_1.weapon}!")
        #     print(f"Your {dino_1.name}'s current health is {dino_1.health}!")
        #     robot_1.health = robot_1.health - dino_attack
        #     dino_1.attack(robot_1)
        #     print(f"{dino_1.name} has attacked {robot_1.name}!")
        #     print(f"{robot_1.name}'s current health is {robot_1.health}!")
        # if dino_1.health <= 0:
        #     print(f"{dino_1.name} is EXTINCT! {robot_1.name} wins!")
        # elif robot_1.health <= 0:
        #     print(f"{robot_1.name} has been terminated!")
            
    
        
    def display_welcome(self):
        print("WELCOME TO ROBOT VS DINOSAUR!")

    def battle_phase(self):
        while dino_1.health and robot_1.health >= 0:
            robot_1.attack(dino_1)
            dino_1.health = dino_1.health - robot_attack
            print(f"{robot_1.name} has attacked {dino_1.name} with a {robot_1.weapon}!")
            print(f"{dino_1.name}'s current health is {dino_1.health}!")
            robot_1.health = robot_1.health - dino_attack
            dino_1.attack(robot_1)
            print(f"{dino_1.name} has attacked {robot_1.name}!")
            print(f"{robot_1.name}'s current health is {robot_1.health}!")
        if dino_1.health <= 0:
            print(f"{dino_1.name} is EXTINCT! {robot_1.name} is unstoppable!")
        elif robot_1.health <= 0:
            print(f"{robot_1.name} has been terminated!")
            
    def display_winner(self):
        if robot_1.health <= dino_1.health:
            print(f"{dino_1.name} rules all!")
        elif dino_1.health <= robot_1.health:
            print(f"{robot_1.name} wins!")
        
