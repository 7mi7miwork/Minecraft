# crafting.py

class Crafting:
    def __init__(self, recipes=None):
        """
        recipes: dict mit Rezeptnamen -> dict mit:
            'ingredients': dict item_name -> Anzahl
            'result': tuple (item_name, Anzahl)
        Beispiel:
            {
                "portal": {
                    "ingredients": {"portal_activator": 1, "iron": 3},
                    "result": ("world_portal", 1)
                }
            }
        """
        self.recipes = recipes or {}

    def add_recipe(self, name, ingredients, result):
        self.recipes[name] = {
            "ingredients": ingredients,
            "result": result
        }

    def can_craft(self, inventory, recipe_name):
        """Prüft, ob Crafting möglich ist mit gegebenem Inventory"""
        if recipe_name not in self.recipes:
            return False
        ingredients = self.recipes[recipe_name]["ingredients"]
        for item, count in ingredients.items():
            if not inventory.has_item(item, count):
                return False
        return True

    def craft(self, inventory, recipe_name):
        """
        Versucht ein Item zu craften:
        - Prüft Zutaten
        - Entfernt Zutaten aus Inventory
        - Fügt Ergebnis hinzu
        - Gibt True/False zurück
        """
        if not self.can_craft(inventory, recipe_name):
            return False
        ingredients = self.recipes[recipe_name]["ingredients"]
        for item, count in ingredients.items():
            inventory.remove_item(item, count)
        result_item, result_count = self.recipes[recipe_name]["result"]
        inventory.add_item(result_item, result_count)
        return True