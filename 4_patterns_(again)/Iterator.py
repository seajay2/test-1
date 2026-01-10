class CustomCollection:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return CustomIterator(self.items)


class CustomIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item
