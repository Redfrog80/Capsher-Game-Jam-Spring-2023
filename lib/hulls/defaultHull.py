
class hull:
    def __init__(self, 
                 health = 100, 
                 regen = 0.01,
                 damage_resistance = 0,
                 **kwargs) -> None:
        
        self.max_health_real = None
        self.max_health_base = health
        self.max_health_multiplier = 1
        
        self.passive_regen_real = None
        self.passive_regen_base = regen
        self.passive_regen_multiplier = 1
        
        self.damage_resistance_real = None
        self.damage_resistance_base = damage_resistance
        self.damage_resistance_multiplier = 1
        
        self.health = health
        self.update_stats()
    
    def damage(self, amount):
        self.health -= (amount*(1-self.damage_resistance_real)) 
        return self.is_broken()
    
    def is_broken(self):
        return self.health <= 0
    
    def update_stats(self):
        self.max_health_real = self.max_health_base*self.max_health_multiplier
        self.passive_regen_real = self.passive_regen_base*self.passive_regen_multiplier
        self.damage_resistance_real = self.damage_resistance_base*self.damage_resistance_multiplier
    
    def update(self, dt: float):
        if (self.health < self.max_health_real):
            self.health = self.health + self.passive_regen_real*self.max_health_real*dt
        else:
            self.health = self.max_health_real