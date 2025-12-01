# portal.py

import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, image, required_items):
        """
        x, y: Position in Pixeln
        image: pygame.Surface für das Portal
        required_items: dict item_name -> Anzahl, die zum Aktivieren nötig sind
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.required_items = required_items
        self.activated = False

    def try_activate(self, player_inventory):
        """
        Versucht das Portal zu aktivieren:
        - Prüft, ob alle erforderlichen Items im Inventar sind
        - Falls ja, aktiviert Portal (True zurück)
        - Sonst False
        """
        for item, count in self.required_items.items():
            if not player_inventory.has_item(item, count):
                return False
        # Entferne die Items aus Inventar
        for item, count in self.required_items.items():
            player_inventory.remove_item(item, count)
        self.activated = True
        return True