# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import msvcrt
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
    
    while True:
        selection = msvcrt.getch() # gets a keyboard input and converts it into a byte string for class selection logic
        if selection == b'1': # class selection logic 
            return 1
        elif selection == b'2':
            return 2
        elif selection == b'3':
            return 3
        elif selection == b'4':
            return 4
        else:
            print(f'{selection.decode()} is not a valid selection.') #.decode turns a byts into utf-8

def name(char_name): # Menu for setting your name 
    if char_name == 1:
        character_art.warior()
        name = input('Name your warrior: ')
        return class_info.Warrior(name)
    elif char_name == 2:
        character_art.mage()
        name = input('Name your mage: ')
        return class_info.Mage(name)
    elif char_name == 3:
        character_art.archer()
        name = input('Name your archer: ')
        return class_info.Archer(name)
    elif char_name == 4:
        character_art.paladin()
        name = input('Name your paladin: ')
        return class_info.Paladin(name)
