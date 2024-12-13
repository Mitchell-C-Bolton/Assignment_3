# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import keyboard
import character_art
import class_info

# Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def class_selection():
    
    # ASCII for the class sellection screen
    print('''
        +-------Select your class------+
        |                              |
        |   1) ~~~~ Warrior ~~~~       |
        |   A strong and mele fighter  |
        |                              |
        |   2) ~~~~~ Mage ~~~~~~       |
        |   A master of arcane magic   |
        |                              |
        |   3) ~~~~~ Archer ~~~~       |
        |   A ranged expert            |
        |                              |
        |   4) ~~~~~ Paladin ~~~       |
        |   A holy knight              |
        |                              |
        +------------------------------+
        
        Press the coresponding numebr to select a class.
        ''')
    
    while True: # Select a class logic
        if keyboard.is_pressed('1'):
            return 1
        elif keyboard.is_pressed('2'):
            return 2
        elif keyboard.is_pressed('3'):
            return 3
        elif keyboard.is_pressed('4'):
            return 4
        elif keyboard.read_event().event_type == keyboard.KEY_DOWN: #checks if any key outside of 1-4 was pressed
            print('        please choose a class using 1-4')

def name(class_selection): # Menu for setting your name 
    if class_selection == 1:
        character_art.warior()
        name = input('Name your warrior: ')
        return class_info.Warrior(name)
    elif class_selection == 2:
        character_art.mage()
        name = input('Name your mage: ')
        return class_info.Mage(name)
    elif class_selection == 3:
        character_art.archer()
        name = input('Name your archer: ')
        return class_info.Archer(name)
    elif class_selection == 4:
        character_art.paladin()
        name = input('Name your paladin: ')
        return class_info.Paladin(name)
