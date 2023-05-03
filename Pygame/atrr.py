import time

class CoinSystem:
    def __init__(self, coins_per_second=1):
        self.coins = 0
        self.last_updated = time.time()
        self.coins_per_second = coins_per_second

    def update(self):
        now = time.time()
        time_passed = now - self.last_updated
        coins_earned = time_passed * self.coins_per_second
        self.coins += coins_earned
        self.last_updated = now

    def earn_coins(self, amount):
        self.coins += amount

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            return True
        else:
            return False

class Player:
    def __init__(self, name, level = 1, health=100, defense=10, attack = 0, health_regen=1, max_health=100):
        self.name = name
        self.health = health
        self.defense = defense
        self.health_regen = health_regen
        self.max_health = max_health
        self.level = level
        self.attack = attack
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_level(self):
        return self.level
    
    def set_level(self, level):
        self.level = level

    def get_health(self):
        return self.health
    
    def set_health(self, health):
        self.health = health
        
    def get_defense(self):
        return self.defense
    
    def set_defense(self, defense):
        self.defense = defense
    
    def get_health_regen(self):
        return self.health_regen
    
    def set_health_regen(self, health_regen):
        self.health_regen = health_regen

    def get_max_health(self):
        return self.max_health
    
    def set_max_health(self, max_health):
        self.max_health = max_health
        
    def take_damage(self, damage):
        actual_damage = damage - self.defense
        if actual_damage < 0:
            actual_damage = 0
        self.health -= actual_damage 
    
    def add_points(self, points):
        self.score += points
    
    def heal(self):
        self.health += self.health_regen
        if self.health > self.max_health:
            self.health = self.max_health
    
    def add_exp(self, exp):
        self.exp += exp

class LevelUp:
    def __init__(self, level, exp, exp_required):
        self.level = level
        self.exp = exp
        self.exp_required = exp_required

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.exp_required:
            self.exp -= self.exp_required
            self.level += 1
            self.exp_required = int(self.level + (self.exp_required * self.level))

    def get_level(self):
        return self.level

    def get_exp(self):
        return self.exp

    def get_exp_required(self):
        return self.exp_required