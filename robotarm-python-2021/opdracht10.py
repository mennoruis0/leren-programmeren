from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = 2
grijparm = 10
for x in range(5):
    grijparm = grijparm - 1
    robotArm.grab()
    for x in range(grijparm):
        robotArm.moveRight()
    robotArm.drop()
    grijparm = grijparm - 1
    for x in range(grijparm):
        robotArm.moveLeft()
robotArm.wait()