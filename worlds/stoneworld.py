# worlds/stoneworld.py

from settings import TILE_SIZE
import pygame
from utils.helpers import load_image

BLOCK_TYPES = {
    "stone": "stone.png",
    "iron": "iron_ore.png",
    "coal": "coal_ore.png",
    "rock": "rock.png",
}

MAP_DATA = [
    [None, None, None, None, None, None, None, None, None, None],
    [None, "coal", None, None, None, None, None, None, None, None],
    ["rock", "rock", "iron", "iron", "iron", None, None, None, None, None],
    ["stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone"],
    ["stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone"],
]

def load_block_images():
    images = {}
    for block, filename in BLOCK_TYPES.items():
        path = f"assets/blocks/{filename}"
        img = load_image(path, scale=(TILE_SIZE, TILE_SIZE))
        if img:
            images[block] = img
    return images