from .defaultWeapon import weapon

class bolter(weapon):
    def __init__(self, projectile_texture_name, projectile_tag, image_dict, sound_dict, **kwargs) -> None:
        super().__init__(image_dict = image_dict, sound_dict = sound_dict, **kwargs)
        self.set_projectile_weapon()
        
        self.damage_base = self.damage_base or 20
        self.firerate_base = self.firerate_base or .2
        self.range_base = self.range_base or 400
        
        self.projectile_velocity_base = kwargs.get("projectile_velocity") or 600
        self.projectile_count = kwargs.get("projectile_count") or 3
        self.projectile_firing_angle = kwargs.get("projectile_firing_angle") or 25
        self.projectile_size = kwargs.get("projectile_size") or (55,55)
        self.projectile_texture_name = projectile_texture_name or "bullet1"
        self.projectile_tag = projectile_tag
        
        self.update_projectile_stats()

    def fire(self, dt,**kwargs ):
        return self.fire_projectile(dt,**kwargs)