# worlds/grassland.py

from settings import TILE_SIZE
import pygame
from utils.helpers import load_image

# Block-Typen der Grasland-Welt
BLOCK_TYPES = {
    "grass": "grass.png",
    "dirt": "dirt.png",
    "wood": "wood.png",
    "stone": "stone.png",
    "plant": "plant.png"
}

# Beispiel Map (2D-Liste), wo jeder Eintrag ein Block-Typ oder None ist
MAP_DATA = [
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, "plant", None, None, None, None, None, None],
    [None, None, "wood", "wood", "wood", None, None, None, None, None],
    ["dirt", "dirt", "dirt", "dirt", "dirt", "dirt", "dirt", "dirt", "dirt", "dirt"],
    ["grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass"],
]

def load_block_images():
    images = {}
    for block, filename in BLOCK_TYPES.items():
        path = f"assets/blocks/{filename}"
        img = load_image(path, scale=(TILE_SIZE, TILE_SIZE))
        if img:
            images[block] = img
    return images