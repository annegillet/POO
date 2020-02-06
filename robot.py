class Robot:
    nb_step = 0

    def __init__(self, name):
        self.name = name
        self.direction = "Est"
        self.x = 0
        self.y = 0

    def position(self, x, y):
        self.x = x
        self.y = y
    
    def move_on(self):
        self.y += 1

    def turn_right(self):
        self.x += 1
        if self.direction == "Est":
            self.direction = "Sud"
        elif self.direction == "Sud":
            self.direction = "Ouest"
        elif self.direction == "Ouest":
            self.direction = "Nord"
        else:
            self.direction = "Est"

    def state(self):
        self.__repr__ = f" Position : {self.x, self.y}, direction : {self.direction}"
        print(self.__repr__)