# Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import class_info
import os

# Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_battle(player, wizard): # Battle visuials credit goes to Mitchell Bolton (I made this one personally)
    print(f''' 
                                                   \   /
       @                                            \@/
      /|\                                            |
       |                                            / \\
______/_\___________________________________________|__\_____
.---.__.---.__.---.__.---.__.---.__.---.__.---.__.---.__.---.
.--.__.--.__.--.__.--.__.--.__.--.__.--.__.--.__.--.__.--.__.


   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
   |                 {player.name} the hero!
   |
   |  Health:████████████████████████████████████████
   |  Attack Power: {player.attack_power}
   |
   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
   |                 Evil Wizard
   |  
   |  Health:████████████████████████████████████████
   |  Attack Power: {wizard.attack_power}
   |
    ''')

def battle(player, wizard):# Battle function with user menu for actions
    os.system('cls')
    while wizard.health > 0 and player.health > 0:
        print_battle(player, wizard)
        test = input('test')
        



        
        
# player1 = class_info.Archer('jake')
# wizard1 = class_info.EvilWizard('paull') 
# battle(player1, wizard1)
        
        
        
        
        
        
        
        
        
        
    #     print("\n--- Your Turn ---")
    #     print("1. Attack")
    #     print("2. Use Special Ability")
    #     print("3. Heal")
    #     print("4. View Stats")
        
    #     choice = input("Choose an action: ")

    #     if choice == '1':
    #         player.attack(wizard)
    #     elif choice == '2':
    #         # Call the special ability here
    #         pass  # Implement this
    #     elif choice == '3':
    #         # Call the heal method here
    #         pass  # Implement this
    #     elif choice == '4':
    #         player.display_stats()
    #     else:
    #         print("Invalid choice, try again.")
    #         continue

    #     # Evil Wizard's turn to attack and regenerate
    #     if wizard.health > 0:
    #         wizard.regenerate()
    #         wizard.attack(player)

    #     if player.health <= 0:
    #         print(f"{player.name} has been defeated!")
    #         break

    # if wizard.health <= 0:
    #     print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        
    # if player.health <= 0:
    #     print(f"The player {player.name} has been defeated by {wizard.name}!")