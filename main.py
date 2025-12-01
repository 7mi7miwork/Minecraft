# main.py

import pygame
import sys
from settings import *
from player import Player
from world import World
from utils.helpers import load_image
from inventory import Inventory
from crafting import Crafting

# Welt-Module importieren
import worlds.grassland as grassland
import worlds.stoneworld as stoneworld
import worlds.crystalcaves as crystalcaves
import worlds.lavaworld as lavaworld

def load_world_by_name(name):
    if name == "grassland":
        images = grassland.load_block_images()
        map_data = grassland.MAP_DATA
    elif name == "stoneworld":
        images = stoneworld.load_block_images()
        map_data = stoneworld.MAP_DATA
    elif name == "crystalcaves":
        images = crystalcaves.load_block_images()
        map_data = crystalcaves.MAP_DATA
    elif name == "lavaworld":
        images = lavaworld.load_block_images()
        map_data = lavaworld.MAP_DATA
    else:
        raise ValueError(f"Unknown world: {name}")
    return World(map_data, images)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Spieler starten bei (0,0)
    player = Player(50, 50)

    # Startwelt laden
    current_world_index = 0
    current_world_name = WORLD_ORDER[current_world_index]
    world = load_world_by_name(current_world_name)

    # Inventar & Crafting
    inventory = Inventory()
    crafting = Crafting()

    # Beispiel Rezept: Portal (Portalaktivator + Eisen)
    crafting.add_recipe(
        "world_portal",
        {"portal_activator": 1, "iron": 3},
        ("world_portal", 1)
    )

    # Kamera-Offset (für Scrollen)
    camera_x = 0
    camera_y = 0

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # Sekunden seit letztem Frame
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Spieler bewegen mit Kollision
        collidable_blocks = world.get_collidable_blocks()
        player.move(keys, collidable_blocks)

        # Kamera folgt Spieler
        camera_x = player.rect.centerx - WINDOW_WIDTH // 2
        camera_y = player.rect.centery - WINDOW_HEIGHT // 2

        # Einfaches Zeichnen
        screen.fill((50, 50, 80))  # Hintergrundfarbe
        world.draw(screen, (camera_x, camera_y))
        screen.blit(player.image, (player.rect.x - camera_x, player.rect.y - camera_y))

        # HUD: Inventar anzeigen (Item-Namen & Anzahl)
        font = pygame.font.SysFont(None, 24)
        x_hud = 10
        y_hud = 10
        for item_name, count in inventory.get_all_items().items():
            text = font.render(f"{item_name}: {count}", True, (255, 255, 255))
            screen.blit(text, (x_hud, y_hud))
            y_hud += 25

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()