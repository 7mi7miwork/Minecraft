# inventory.py

class Inventory:
    def __init__(self, max_stack_size=64):
        # items: dict mit item_name -> count
        self.items = {}
        self.max_stack_size = max_stack_size

    def add_item(self, item_name, count=1):
        current = self.items.get(item_name, 0)
        new_count = current + count
        if new_count > self.max_stack_size:
            leftover = new_count - self.max_stack_size
            self.items[item_name] = self.max_stack_size
            return leftover  # zurückbleibende Items, die nicht ins Inventar passen
        else:
            self.items[item_name] = new_count
            return 0

    def remove_item(self, item_name, count=1):
        current = self.items.get(item_name, 0)
        if current >= count:
            self.items[item_name] = current - count
            if self.items[item_name] == 0:
                del self.items[item_name]
            return True
        else:
            return False

    def has_item(self, item_name, count=1):
        return self.items.get(item_name, 0) >= count

    def get_all_items(self):
        return dict(self.items)

    def __repr__(self):
        return f"<Inventory {self.items}>"