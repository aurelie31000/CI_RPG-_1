# src/main/python/character.py
class Character:
    def __init__(self, health=10):
        self.health = health

    def is_dead(self):
        return self.health <= 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, target):
        if not self.is_dead():
            target.take_damage(1)