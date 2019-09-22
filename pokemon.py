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
        enemy.current_health -= self.damage
        print(f"{self.name} has dealt {self.damage} to {enemy.name}!")
    
    def faint(self):
        if self.current_health == 0:
            print(f"{self.name} has fainted and is unable to battle!")