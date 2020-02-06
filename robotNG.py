from robot import Robot

class RobotNG(Robot):

    def move_on(self, nb_step):
        self.y += nb_step
        print(f"Mon robot {self.name} avance de {self.y} pas et {self.state}.")

    def turn_left(self):
        self.x -= 1
        if self.direction == "Est":
            self.direction = "Nord"
        elif self.direction == "Nord":
            self.direction = "Ouest"
        elif self.direction == "Ouest":
            self.direction = "Sud"
        else:
            self.direction = "Est"
        print(f"Mon robot {self.name} tourne à gauche et {self.state}.")

    def turn_around(self):
        self.x -=2
        if self.direction == "Est":
            self.direction = "Ouest"
        elif self.direction == "Nord":
            self.direction = "Sud"
        elif self.direction == "Sud":
            self.direction = "Nord"
        else:
            self.direction = "Est"
        print(f"Mon robot {self.name} fait demi-tour et {self.state}.")