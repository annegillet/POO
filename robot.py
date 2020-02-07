class Robot:
    nb_step = 0

    def __init__(self, name):
        self.name = name
        self.direction = "Est"
        self.x = 0
        self.y = 0
    
    def move_on(self):
        if self.direction == "Est":
            self.x += 1
        elif self.direction == "Sud":
            self.y -= 1
        elif self.direction == "Ouest":
            self.x -= 1
        else:
            self.y += 1

    def turn_right(self):
        if self.direction == "Est":
            self.direction = "Sud"
        elif self.direction == "Sud":
            self.direction = "Ouest"
        elif self.direction == "Ouest":
            self.direction = "Nord"
        else:
            self.direction = "Est"
        print(f"Mon robot {self.name} tourne à droite vers {self.direction}.")

    def state(self):
        self.__repr__ = f"Il se situe à {self.x, self.y}, en direction {self.direction}"
        print(self.__repr__)