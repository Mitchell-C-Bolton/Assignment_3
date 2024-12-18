# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import title_screen # ASCII art and logic for title screen
import menus # Game main menu
import map
import battle
import class_info
import win_loss_screen

# Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
os.system('cls') # Clear the junk off your screen
title_screen.print_title() # Title screen from title_screen.py file    

os.system('cls')
character_class_selection = menus.class_selection() # Class selection menu from main_menu.py file

os.system('cls')
player1 = menus.name(character_class_selection) # Choose your hero name from main_menu.py file

os.system('cls')
map.map(player1.name) # Loads in the map from map.py

os.system('cls')
wizard1 = class_info.EvilWizard('Evil Wizard')
win_loss = battle.battle(player1, wizard1)

os.system('cls')
win_loss_screen.win_loss(win_loss)