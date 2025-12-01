# utils/helpers.py

import json
import pygame
from settings import DEBUG_MODE

def debug(msg: str):
    """Print debug messages only when DEBUG_MODE = True."""
    if DEBUG_MODE:
        print(f"[DEBUG] {msg}")

# -----------------------------
# Image Loading Helper
# -----------------------------
def load_image(path, scale=None):
    """Load an image and optionally scale it."""
    try:
        image = pygame.image.load(path).convert_alpha()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except Exception as e:
        print(f"Error loading image '{path}': {e}")
        return None

# -----------------------------
# Collision Helper
# -----------------------------
def rect_collision(rect1, rect2):
    """Simple rectangle collision detection."""
    return rect1.colliderect(rect2)

# -----------------------------
# Save / Load System
# -----------------------------
def save_game(data, file_path):
    """Save a dict as a JSON file."""
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        debug("Game saved successfully.")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game(file_path):
    """Load and return JSON game data."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        debug("Game loaded successfully.")
        return data
    except FileNotFoundError:
        print("No save file found. Starting new game.")
        return None
    except Exception as e:
        print(f"Error loading save file: {e}")
        return None

# -----------------------------
# Math Helpers
# -----------------------------
def clamp(value, min_val, max_val):
    """Keep a number between min and max."""
    return max(min_val, min(value, max_val))