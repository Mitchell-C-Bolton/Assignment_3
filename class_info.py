# Base class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        return f'{self.name} attacks! Dealing {self.attack_power} dammage!'            
            
    def regenerate(self, heal_ammount):
        self.health += heal_ammount
        if self.health > self.max_health:
            self.health = self.max_health
        return f'{self.name} heals {heal_ammount} hitpoints.'

# Player Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Warrior(Character):
    special_name = 'Enrage'
    
    def __init__(self, name):
        super().__init__(name, health=500, attack_power=25)
    
    def special(self, name): # Enrage: multiplies attack power (this effect stacks multiplicativly)
        self.attack_power = int(self.attack_power*1.3)
        return f'{self.name} goes berserk! Increasing their attack power to {self.attack_power}'

class Mage(Character):
    special_name = 'Desperation'
    
    def __init__(self, name):
        super().__init__(name, health=350, attack_power=35) 

    def special(self, opponent): # Desperation: deals damage based on missing health times 3
        opponent.health -= (self.max_health - self.health)/5
        return f'{self.name} sharpens the blood from their wounds! Dealing {self.attack_power*3} dammage!'
    
class Archer(Character):
    special_name = 'Flurry of Arrows'
    
    def __init__(self, name):
        super().__init__(name, health=425, attack_power=30)
        
    def special(self, opponent): # Flurry of Arrows
        opponent.health -= self.attack_power*2
        return f'{self.name} flings a volley of arrows into the air! Dealing {self.attack_power} damage!'

class Paladin(Character):
    special_name = 'Holy Light'
    
    def __init__(self, name):
        super().__init__(name, health=700, attack_power=25)

    def special(self, opponent): # Holy Light
        self.health += 20
        if self.health > self.max_health:
            self.health = self.max_health
        opponent.health -= 20
        return f'{self.name} calls on the gods! Dealing {self.attack_power} damage and healing 7!'
        

# Evil Wizard ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=400, attack_power=23)
        
    def special(self, opponent):
        opponent.health -= self.attack_power
        self.attack_power += 3
        self.health += 3
        if self.health > self.max_health:
            self.health = self.max_health
        return f'{self.name} deals {self.attack_power-3} dammage!\n   |  {self.name} heals for 3!\n   |  {self.name} increasses their attack power to {self.attack_power}!'