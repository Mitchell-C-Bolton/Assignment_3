# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import keyboard
import os
import time

# Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def map(name):
    active = True
    map = [ # Game map
     '██████████████████████████████████',
     '█        █                 █   ጰ █',
     '█        █        █              █',
     '█                 █        ███████',
     '█   █████████     █              █',
     '█           █     █              █',
     '█           █     ████████       █',
     '█████   █   █                    █',
     '█       █   ███████      █       █',
     '█       █         █      █       █',
     '█ 𓀠     █   █            █       █',
     '██████████████████████████████████'
    ]

       
    def print_map(name): # prints the map along with controlls/key
        for item in map:
            print(item)
            
        print(f'''
+~~~~~~~~~~~ Controlls ~~~~~~~~~~+
    
    Use ASWD keys to navigate.   
                                     
+~~~~~~~~~~~~~ Key ~~~~~~~~~~~~~~+
    
       █ = Wall                     
       𓀠 = {name} the hero.                   
       ጰ = Evil Wizard              
                                    
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    ''')

    def make_zero(row, column): # Make the cell set to 0 (after move)
        temp_convert = list(map[row]) # Convert to list for modificaitons 
        temp_convert[column] = ' '
        map[row] = ''.join(temp_convert) # Convert back to str for print

    def current_position(): # Find the player
        for row_i, row in enumerate(map):
            for column_i, location in enumerate(row):
                if map[row_i][column_i] == '𓀠':
                    return(row_i, column_i)

    def up(): # Move up
        row, column = current_position()
        if map[row-1][column] == ' ':
            temp_convert = list(map[row-1])
            temp_convert[column] = '𓀠'
            map[row-1] = ''.join(temp_convert) 
            make_zero(row, column)
        elif map[row-1][column] == '█':
            pass
        elif map[row-1][column] == 'ጰ':
            return False

    def right(): # Move right
        row, column = current_position()
        if map[row][column+1] == ' ':
            temp_convert = list(map[row]) 
            temp_convert[column+1] = '𓀠'
            map[row] = ''.join(temp_convert)
            make_zero(row, column)
        elif map[row][column+1] == '█':
            pass
        elif map[row][column+1] == 'ጰ':
            return False
        
    def down(): # Move down
        row, column = current_position()
        if map[row+1][column] == ' ':
            temp_convert = list(map[row+1])
            temp_convert[column] = '𓀠'
            map[row+1] = ''.join(temp_convert)
            make_zero(row, column)
        elif map[row+1][column] == '█':
            pass
        elif map[row+1][column] == 'ጰ':
            return False

    def left(): # Move left
        row, column = current_position()
        if map[row][column-1] == ' ':
            temp_convert = list(map[row])
            temp_convert[column-1] = '𓀠'
            map[row] = ''.join(temp_convert)
            make_zero(row, column)
        elif map[row][column-1] == '█':
            pass
        elif map[row][column-1] == 'ጰ':
            return False
            
    print_map(name)
    
    while active != False:
        if keyboard.is_pressed('w'): 
            os.system('cls')
            active = up()
            print_map(name)
            time.sleep(0.2) # Makes it so keys aren't being rapidly spammed at an ungodly fast rate
            continue
        elif keyboard.is_pressed('a'):
            os.system('cls')
            active = left()
            print_map(name)
            time.sleep(0.2)
            continue
        elif keyboard.is_pressed('s'):
            os.system('cls')
            active = down()
            print_map(name)
            time.sleep(0.2)
            continue
        elif keyboard.is_pressed('d'):
            os.system('cls')
            active = right()
            print_map(name)
            time.sleep(0.2)
            continue