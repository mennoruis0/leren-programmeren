from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

robotArm.speed = 2

robotArm.moveRight()

for x in range (3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

robotArm.wait()