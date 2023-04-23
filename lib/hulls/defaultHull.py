
class hull:
    def __init__(self, maxhealth, passive_regen) -> None:
        self.health = maxhealth
        self.max_health = maxhealth
        self.passive_regen = passive_regen
        self.damage_resistance = 0
    
    def damage(self, amount):
        self.health -= (amount*(1-self.damage_resistance)) 
        return True if (self.health < 0) else False
    
    def update(self, dt, **kwargs):
        if (self.health != self.max_health):
            self.health = self.max_health if (self.health > self.max_health) else self.health + self.passive_regen*dt