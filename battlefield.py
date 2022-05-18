
from dinos import Dino
from robots import Robot

myrobot = Robot()
mydino = Dino()

class Battlefield:
    def __init__(self):
        robot_attack = myrobot
        dino_attack = mydino

    def run_game(self):
        print (f" {myrobot.name} vs {mydino.name}!")
    
    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
