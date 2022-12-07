from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')

robotArm.moveRight
robotArm.grab
for x in range(4):
    robotArm.moveRight
robotArm.drop
robotArm.moveLeft

robotArm.wait()
