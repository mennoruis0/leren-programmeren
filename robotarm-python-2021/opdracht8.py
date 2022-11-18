from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
for x in range(7):
    robotArm.moveRight()
    robotArm.grab()
    for x in range(8):
        robotArm.moveRight() 
    robotArm.drop()
    for x in range(9):
        robotArm.moveLeft()
robotArm.wait()


