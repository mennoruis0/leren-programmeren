from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

robotArm.speed = 2

robotArm.grab()
for x in range(4):
    robotArm.moveRight()
robotArm.drop()
for x in range(4):
    robotArm.moveLeft()
robotArm.grab()
for x in range(3):
    robotArm.moveRight()
robotArm.drop()
for x in range(3):
    robotArm.moveLeft()
robotArm.grab()
for x in range(2):
    robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for x in range(2):
    robotArm.moveRight()
robotArm.grab()
for x in range(2):
    robotArm.moveLeft()
robotArm.drop()
for x in range(3):
    robotArm.moveRight()
robotArm.grab()
for x in range(3):
    robotArm.moveLeft()
robotArm.drop()
robotArm.wait()