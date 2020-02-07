from robot import Robot

class RobotNG(Robot):

    def __init__(self, name):
        super().__init__(name)
        self.turbo = False

    def boost(self):
        if self.turbo == False:
            self.turbo = True
        else:
            self.turbo = False
        return self.turbo

    def move_on(self, nb_step):

        self.nb_step = nb_step

        if self.turbo == False:
            for i in range(self.nb_step) :
                Robot.move_on(self)
        else:
            for i in range(self.nb_step * 3) :
                Robot.move_on(self)

    def turn_left(self):
        if self.direction == "Est":
            self.direction = "Nord"
        elif self.direction == "Nord":
            self.direction = "Ouest"
        elif self.direction == "Ouest":
            self.direction = "Sud"
        else:
            self.direction = "Est"
        print(f"Mon robot {self.name} tourne à gauche vers {self.direction}.")

    def turn_around(self):
        if self.direction == "Est":
            self.direction = "Ouest"
        elif self.direction == "Nord":
            self.direction = "Sud"
        elif self.direction == "Sud":
            self.direction = "Nord"
        else:
            self.direction = "Est"
        print(f"Mon robot {self.name} fait demi-tour vers {self.direction}.")

    def display(self):
        if self.turbo == True:
            print(f"TURBO ON")
        else:
            print(f"TURBO OFF")