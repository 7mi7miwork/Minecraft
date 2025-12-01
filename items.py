# items.py

import pygame

class Item:
    def __init__(self, name, image, description=""):
        """
        name: String, eindeutiger Item-Name
        image: pygame.Surface, Icon des Items
        description: kurze Beschreibung
        """
        self.name = name
        self.image = image
        self.description = description

    def __repr__(self):
        return f"<Item: {self.name}>"