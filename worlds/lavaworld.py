# worlds/lavaworld.py

from settings import TILE_SIZE
import pygame
from utils.helpers import load_image

BLOCK_TYPES = {
    "magma": "magma.png",
    "obsidian": "obsidian.png",
    "rock": "rock.png",
    "lava_stone": "lava_stone.png",
}

MAP_DATA = [
    [None, None, None, None, None, None, None, None, None, None],
    [None, "magma", None, None, None, None, None, None, None, None],
    ["rock", "rock", "obsidian", "obsidian", "obsidian", None, None, None, None, None],
    ["lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone"],
    ["lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone", "lava_stone"],
]

def load_block_images():
    images = {}
    for block, filename in BLOCK_TYPES.items():
        path = f"assets/blocks/{filename}"
        img = load_image(path, scale=(TILE_SIZE, TILE_SIZE))
        if img:
            images[block] = img
    return images