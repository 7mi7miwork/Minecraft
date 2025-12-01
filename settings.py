# settings.py

# --- Window Settings ---
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
FPS = 60
TITLE = "2D Multi-World Adventure"

# --- Tile Settings ---
TILE_SIZE = 32

# --- Player Settings ---
PLAYER_SPEED = 3
PLAYER_JUMP_FORCE = 10
PLAYER_GRAVITY = 0.5
PLAYER_MAX_HEALTH = 100

# --- Save System ---
SAVE_FILE = "savegame.json"

# --- Worlds ---
WORLD_ORDER = [
    "grassland",
    "stoneworld",
    "crystalcaves",
    "lavaworld"
]

# --- Paths ---
ASSET_PATH = "assets/"
BLOCK_ASSET_PATH = ASSET_PATH + "blocks/"
ITEM_ASSET_PATH = ASSET_PATH + "items/"
WORLD_SPRITE_PATH = ASSET_PATH + "world_sprites/"

# --- Debug ---
DEBUG_MODE = False
