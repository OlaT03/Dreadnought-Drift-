# ship.py
class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.is_sunk = False

    def hit(self):
        self.hits += 1
        if self.hits == self.size:
            self.is_sunk = True
