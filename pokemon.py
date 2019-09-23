class Pokemon:
    def __init__(self,name,level,ptype, max_health, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.ptype = ptype
        self.max_health = max_health
        self.current_health = current_health
        self.is_knocked_out = is_knocked_out
        self.damage = self.attack

    def attack(self,enemy):
        if self.ptype == "fire" and enemy.ptype == "water":
            self.damage /= 2
        if self.ptype == "fire" and enemy.ptype == "grass":
            self.damage *= 2
        if self.ptype == "water" and enemy.ptype == "grass":
            self.damage /= 2
        if self.ptype == "water" and enemy.ptype == "fire":
            self.damage *= 2
        if self.ptype == "grass" and enemy.ptype == "fire":
            self.damage /= 2
        if self.ptype == "grass" and enemy.ptype == "water":
            self.damage *2

        enemy.current_health -= self.damage
        print(f"{self.name} has dealt {self.damage} to {enemy.name}!\n\n")
    
    def faint(self):
        if self.current_health == 0:
            self.is_knocked_out = True
            print(f"{self.name} has fainted and is unable to battle!\n\n")
    
    def recover(self):
        self.current_health += 30
        print(f"{self.name} has recovered 30 health! {self.current_health} health remaining!")

class Trainer:
    def __init__(self, name, pokemon, potions):
        self.name = name
        self.pokemon = pokemon
        self.potions = potions
        self.active_pokemon = 1

    def use_potion(self,pokemon):
        pokemon.current_health += 50
        print(f"{self.name} used a potion on {pokemon.name}! {pokemon.name} has recovered 50 health! {pokemon.current_health} remaining!")
    

charmander = Pokemon("Charmander", 10, "fire", 36, 36, False)
blastoise = Pokemon("Blastoise", 30, "water", 110, 110, False)

sam = Trainer("Sam", [blastoise], 3)
terry = Trainer("Terry", [charmander], 3)