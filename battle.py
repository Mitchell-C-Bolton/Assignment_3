# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import class_info
import os
import math
import random

# Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_battle(player, wizard, player_health_bar, wizard_health_bar, wizard_log, player_log):
    print(f''' 
                                                      
       @                                            \@
      /|\                                            |\\
       |                                            / \\
______/_\___________________________________________\__\_____
.---.__.---.__.---.__.---.__.---.__.---.__.---.__.---.__.---.
.--.__.--.__.--.__.--.__.--.__.--.__.--.__.--.__.--.__.--.__.


   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
   |                 {player.name} the hero!
   |
   |  Health:{player_health_bar}
   |  Attack Power: {player.attack_power}
   |  
   |  1) Attack
   |  2) Heal
   |  3) {player.special_name}
   |
   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
   |                 Evil Wizard
   |  
   |  Health:{wizard_health_bar}
   |  Attack Power: {wizard.attack_power}
   |
   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
   |                 Combat Log
   |
   |  {wizard_log}
   |  {player_log}
   |
    ''') # Battle ASCII credit goes to Mitchell Bolton (I made this one personally)

def health_bar(max_health, health):
    max_health_blocks = math.ceil((40 / max_health) * health)
    health_bar = ''
    for i in range(max_health_blocks):
        health_bar+= '█'
    return health_bar

def battle(player, wizard):# Battle function with user menu for actions
    player_health_bar = health_bar(player.max_health, player.health)
    wizard_health_bar = health_bar(wizard.max_health, wizard.health)
    wizard_log = 'The wizard waits in anticipation.'
    player_log = ''
    print_battle(player, wizard, player_health_bar, wizard_health_bar, wizard_log, player_log)
    while wizard.health > 0 and player.health > 0:
        
        # Player attack phase
        player_attack = input('Action: ')
        if player_attack == '1':
            player_log = player.attack(wizard)
        elif player_attack == '2':
            player_log = player.regenerate(10)
        elif player_attack == '3':
            player_log = player.special(wizard)
        else:
            os.system('cls')
            print_battle(player, wizard, player_health_bar, wizard_health_bar, wizard_log, player_log)
            print(f'{player_attack} is Not a valid option.')
            print(f'Chose an action from your list of actions (1-3)')
            continue
        
        # Evil wizard attack phase
        wizard_attack = random.randint(1,3)
        if wizard_attack == 1:
            wizard_log = wizard.attack(player)
        elif wizard_attack == 2:
            wizard_log = wizard.regenerate(7)
        elif wizard_attack == 3:
            wizard_log = wizard.special(player)
        
        player_health_bar = health_bar(player.max_health, player.health)
        wizard_health_bar = health_bar(wizard.max_health, wizard.health)
        os.system('cls')
        print_battle(player, wizard, player_health_bar, wizard_health_bar, wizard_log, player_log)
        
    
    if player.health > 0:
        return True
    else:
        return False