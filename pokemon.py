class Pokemon:
    def __init__(self,name,level,ptype, max_health, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.ptype = ptype
        self.max_health = max_health
        self.current_health = current_health
        self.is_knocked_out = is_knocked_out
        self.damage = self.level

    def attack(self,enemy):
        if self.ptype == "fire" and enemy.ptype == "water":
            slash = self.damage / 2
        if self.ptype == "fire" and enemy.ptype == "grass":
            slash = self.damage * 2
        if self.ptype == "water" and enemy.ptype == "grass":
            slash = self.damage / 2
        if self.ptype == "water" and enemy.ptype == "fire":
            slash = self.damage * 2
        if self.ptype == "grass" and enemy.ptype == "fire":
            slash = self.damage / 2
        if self.ptype == "grass" and enemy.ptype == "water":
            slash = self.damage * 2

        enemy.current_health -= slash
        print(f"{self.name} has dealt {slash} damage to {enemy.name}! {enemy.name} has {enemy.current_health} HP remaining!\n\n")
    
    def faint(self):
        if self.current_health < 0:
            self.is_knocked_out = True
            print(f"{self.name} has fainted and is unable to battle!\n\n")
    
    def recover(self):
        self.current_health += 30
        print(f"{self.name} has recovered 30 HP! {self.current_health} HP remaining!\n\n")

class Trainer:
    def __init__(self, name, pokemon, potions):
        self.name = name
        self.pokemon = pokemon
        self.potions = potions
        self.active_pokemon = 1

    def use_potion(self,pokemon):
        pokemon.current_health += 50
        print(f"{self.name} used a potion on {pokemon.name}! {pokemon.name} has recovered 50 HP! {pokemon.current_health} HP remaining!\n\n")
    

charmander = Pokemon("Charmander", 10, "fire", 36, 36, False)
blastoise = Pokemon("Blastoise", 30, "water", 110, 110, False)

sam = Trainer("Sam", [blastoise], 3)
terry = Trainer("Terry", [charmander], 3)

def main():
    print("Welcome to the world of Pokemon! Here, 10 year olds are sent off to be killed by adult criminal syndicates and their murderbeasts. It's a great time for everyone!\n\nLook, there's one now! Eat his heart!\n\n")

    def trainer_battle():
        while Pokemon.faint != True:
            print("Whatchu gon' do?")
            print("1. Attack")
            print("2. Use Potion")
            user_input = input("")

            if user_input == "1":
                charmander.attack(blastoise)
                if blastoise.current_health == 0:
                    blastoise.faint()
                    exit()
            if user_input == "2":
                terry.use_potion(charmander)
            
            while charmander.current_health > 0:
                blastoise.attack(charmander)
            else:
                charmander.faint()
                exit()


    trainer_battle()

    print("Great job! You beat that guy and stole his wallet. Aquired 152 whateverPokemon'scurrencyis!")
main()