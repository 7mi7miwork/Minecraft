# world.py

import pygame
from settings import TILE_SIZE
from utils.helpers import load_image

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, block_type, image):
        super().__init__()
        self.block_type = block_type
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

class World:
    def __init__(self, map_data, block_images):
        """
        map_data: 2D-Array oder Liste von Listen mit Block-Typen oder None
        block_images: dict block_type -> pygame.Surface
        """
        self.blocks = pygame.sprite.Group()
        self.load_map(map_data, block_images)

    def load_map(self, map_data, block_images):
        self.blocks.empty()
        for row_index, row in enumerate(map_data):
            for col_index, block_type in enumerate(row):
                if block_type:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    image = block_images.get(block_type)
                    if image:
                        block = Block(x, y, block_type, image)
                        self.blocks.add(block)

    def draw(self, surface, camera_offset=(0,0)):
        for block in self.blocks:
            surface.blit(block.image, (block.rect.x - camera_offset[0], block.rect.y - camera_offset[1]))

    def get_collidable_blocks(self):
        # Alle Blöcke, die Kollisionsboxen besitzen
        return self.blocks.sprites()