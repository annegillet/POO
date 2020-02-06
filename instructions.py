from robot import Robot

first_robot = Robot("Anne")
print(f"Mon premier robot s'appelle {first_robot.name} et se situe en {first_robot.x, first_robot.y}, direction {first_robot.direction}")

first_robot.move_on()
first_robot.turn_right()
print(f"Mon premier robot s'appelle {first_robot.name} et se situe en {first_robot.x, first_robot.y}, direction {first_robot.direction}")

first_robot.move_on()
first_robot.turn_right()
print(f"Mon premier robot s'appelle {first_robot.name} et se situe en {first_robot.x, first_robot.y}, direction {first_robot.direction}")

#first_robot.move_on()
first_robot.turn_right()
print(f"Mon premier robot s'appelle {first_robot.name} et se situe en {first_robot.x, first_robot.y}, direction {first_robot.direction}")

first_robot.move_on()
#first_robot.turn_right()
print(f"Mon premier robot s'appelle {first_robot.name} et se situe en {first_robot.x, first_robot.y}, direction {first_robot.direction}")

first_robot.state()
