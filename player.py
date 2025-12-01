# player.py

import pygame
from settings import TILE_SIZE, PLAYER_SPEED, PLAYER_JUMP_FORCE, PLAYER_GRAVITY, PLAYER_MAX_HEALTH
from utils.helpers import clamp

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, images=None):
        super().__init__()
        self.images = images or {}
        self.image = self.images.get('idle', pygame.Surface((TILE_SIZE, TILE_SIZE)))
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Bewegung
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        
        # Status
        self.health = PLAYER_MAX_HEALTH
        self.speed = PLAYER_SPEED
        
        # Inventar: dict mit item_name -> Anzahl
        self.inventory = {}
        
    def move(self, keys, platforms):
        # Links/Rechts
        self.vel_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
        
        # Springen
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = -PLAYER_JUMP_FORCE
            self.on_ground = False
        
        # Anwenden von Gravitation
        self.vel_y += PLAYER_GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        
        # Horizontal bewegen und Kollision
        self.rect.x += self.vel_x
        self.collide(self.vel_x, 0, platforms)
        
        # Vertikal bewegen und Kollision
        self.rect.y += self.vel_y
        self.on_ground = False
        self.collide(0, self.vel_y, platforms)
        
    def collide(self, vel_x, vel_y, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if vel_x > 0:  # Rechts
                    self.rect.right = platform.rect.left
                if vel_x < 0:  # Links
                    self.rect.left = platform.rect.right
                if vel_y > 0:  # Fallend
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                if vel_y < 0:  # Springend
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
    
    def add_item(self, item_name, count=1):
        self.inventory[item_name] = self.inventory.get(item_name, 0) + count
    
    def remove_item(self, item_name, count=1):
        if self.inventory.get(item_name, 0) >= count:
            self.inventory[item_name] -= count
            if self.inventory[item_name] <= 0:
                del self.inventory[item_name]
            return True
        return False
    
    def has_items(self, items_required):
        """Check if player has all items with counts in dict items_required"""
        for item, count in items_required.items():
            if self.inventory.get(item, 0) < count:
                return False
        return True
    
    def __str__(self):
        return f"Player at {self.rect.topleft} with inventory {self.inventory}"