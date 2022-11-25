from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 2
grijparm = 10
for x in range(9):
    grijparm = grijparm - 1
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "red":
        for x in range(grijparm):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(grijparm):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
robotArm.wait()