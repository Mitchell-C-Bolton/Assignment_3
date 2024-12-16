# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import msvcrt
import os
import time

# Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def map(name):
    active = True
    map = [ # Game map
     '██████████████████████████████████',
     '█       █   █     █        █     █',
     '█       █   ████  █    █████  ጰ  █',
     '█           █     █              █',
     '█   █████████  ████        ███████',
     '█           █     █              █',
     '█           ████  ███████████    █',
     '█████   █   █               █    █',
     '█       █   ███████      █  █    █',
     '█       █         █      █  █    █',
     '█   𓀠   █                █       █',
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

    def move(row_dif, column_dif):
        row, column = current_position()
        if map[row+row_dif][column+column_dif] == ' ':
            temp_convert = list(map[row+row_dif])
            temp_convert[column+column_dif] = '𓀠'
            map[row+row_dif] = ''.join(temp_convert) 
            make_zero(row, column)
        elif map[row+row_dif][column+column_dif] == '█':
            pass
        elif map[row+row_dif][column+column_dif] == 'ጰ':
            time.sleep(0.15)
            return False
        
    print_map(name)
    
    while active != False:
        direction = msvcrt.getch()
        if direction == b'w': 
            active = move(-1, 0)
            os.system('cls')
            print_map(name)
            continue
        elif direction == b'a':
            active = move(0, -1)
            os.system('cls')
            print_map(name)
            continue
        elif direction == b's':
            active = move(1, 0)
            os.system('cls')
            print_map(name)
            continue
        elif direction == b'd':
            active = move(0, 1)
            os.system('cls')
            print_map(name)
            continue

