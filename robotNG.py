from robot import Robot

class RobotNG(Robot):

    def move_on(self, nb_step):
        self.nb_step += nb_step

    def turn_left(self):
        self.x -=1

    def turn_around(self):
        self.x -=2