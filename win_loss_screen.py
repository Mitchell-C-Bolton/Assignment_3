# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import sys
import msvcrt

# Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def win_loss(win_loss):
    if win_loss == False:
        print('''
   _____ _                     _                  _       _       __            _           _                     _ 
  |_   _| |__   ___  __      _(_)______ _ _ __ __| |   __| | ___ / _| ___  __ _| |_ ___  __| |  _   _  ___  _   _| |
    | | | '_ \ / _ \ \ \ /\ / / |_  / _` | '__/ _` |  / _` |/ _ \ |_ / _ \/ _` | __/ _ \/ _` | | | | |/ _ \| | | | |
    | | | | | |  __/  \ V  V /| |/ / (_| | | | (_| | | (_| |  __/  _|  __/ (_| | ||  __/ (_| | | |_| | (_) | |_| |_|
    |_| |_| |_|\___|   \_/\_/ |_/___\__,_|_|  \__,_|  \__,_|\___|_|  \___|\__,_|\__\___|\__,_|  \__, |\___/ \__,_(_)
                                                                                               |___/              
    
    Thank you for playing :)
    
    ''')# Credit for text generation goes to: http://patorjk.com/software/taag
    else:
        print('''
                           _       __            _           _   _   _                     _                  _ _ 
   _   _  ___  _   _    __| | ___ / _| ___  __ _| |_ ___  __| | | |_| |__   ___  __      _(_)______ _ _ __ __| | |
  | | | |/ _ \| | | |  / _` |/ _ \ |_ / _ \/ _` | __/ _ \/ _` | | __| '_ \ / _ \ \ \ /\ / / |_  / _` | '__/ _` | |
  | |_| | (_) | |_| | | (_| |  __/  _|  __/ (_| | ||  __/ (_| | | |_| | | |  __/  \ V  V /| |/ / (_| | | | (_| |_|
   \__, |\___/ \__,_|  \__,_|\___|_|  \___|\__,_|\__\___|\__,_|  \__|_| |_|\___|   \_/\_/ |_/___\__,_|_|  \__,_(_)
   |___/  
   
   Thank you for playing :)
                                                                                                     
    ''')# Credit for text generation goes to: http://patorjk.com/software/taag
    
    sys.exit() # Exits the script