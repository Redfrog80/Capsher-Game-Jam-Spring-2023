
class weapon:
    """The weapon base class is a template to build special weapon types. This is not a functional class!
    """
    def __init__(self) -> None:
        self.damage_real = None
        self.damage_base = None
        self.damage_multiplier = None
        
        self.firerate_real = None
        self.firerate_base = None
        self.firerate_multiplier = None
        
        self.range_real = None
        self.range_base = None
        self.range_multiplier = None
        
        self.is_projectile_weapon = False
        self.is_beam_weapon = False
        
    
    def set_projectile_weapon(self):
        self.projectile_velocity = None
        self.projectile_velocity_multiplier = None
        self.projectile_life = None
        self.projectile_texture = None
        self.projectile_shape = None
        
        self.is_projectile_weapon = True
        self.is_beam_weapon = False
    
    # Need to get a collider set up for this weapon variant!
    def set_beam_weapon(self):
        self.beam_range = None
        self.beam_width = None
        self.beam_texture = None
        self.beam_life = None
        self.beam_damaging_life = None
        
        self.is_projectile_weapon = False
        self.is_beam_weapon = True
    