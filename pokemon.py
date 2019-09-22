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
            print(f"{self.name} has fainted and is unable to battle!\n\n")