from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

robotArm.speed = 2

for x in range(4):
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

robotArm.wait()