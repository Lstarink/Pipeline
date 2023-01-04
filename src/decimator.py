class Decimator:
    def __init__(self, order):
        assert(type(order) == int)
        self.order = order
        self.count = 0

    def UseSample(self):
        self.count += 1
        if self.count == self.order:
            self.count = 0
            return True
        else:
            return False
