from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        x = 400, y = 30
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
