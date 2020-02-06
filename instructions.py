from robot import Robot
from robotNG import RobotNG

first_robot = Robot("Anne")
first_robot.state()

first_robot.move_on()
first_robot.turn_right()
first_robot.state()

first_robot.move_on()
first_robot.turn_right()
first_robot.state()

#first_robot.move_on()
first_robot.turn_right()
first_robot.state()

first_robot.move_on()
#first_robot.turn_right()
first_robot.state()

newgen_robot = RobotNG('Nini')
print(f"Mon new generation robot s'appelle {newgen_robot.name}")
newgen_robot.move_on(3)
newgen_robot.turn_left()
newgen_robot.state()

newgen_robot.turn_around()
newgen_robot.state()

