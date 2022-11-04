from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

robotArm.speed = 2

for x in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.wait()