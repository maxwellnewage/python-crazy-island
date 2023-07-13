class Entity():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def draw(self) -> str:
        pass
