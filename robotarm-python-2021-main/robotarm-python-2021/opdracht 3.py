from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# robotArm.speed = 2

robotArm.moveRight()

for x in range(4):
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

robotArm.wait()