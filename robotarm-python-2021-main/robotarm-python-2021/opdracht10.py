from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = 2
grijparm = 10
for x in range(1, 5):
    grijparm = grijparm - 1
    robotArm.grab()
    for x in range(10 - x):
        robotArm.moveRight()
    robotArm.drop()
    grijparm = grijparm - 1
    for grijparm in range(grijparm):
        robotArm.moveLeft()
robotArm.wait()