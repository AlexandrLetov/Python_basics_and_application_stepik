class MoneyBox:
    def __init__(self, capacity):
        self.v = 0
        self.capacity = capacity

    def can_add(self, v):
        if v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if MoneyBox.can_add(self, v):
            self.v += v
            self.capacity -= v
            return True
        else:
            return False
