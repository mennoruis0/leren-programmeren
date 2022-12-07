from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

robotArm.speed = 2

for x in range(7):
    robotArm.moveRight()
for x in range(7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.wait()