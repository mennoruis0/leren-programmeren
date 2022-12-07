from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 2
blok = 1
loop = 1
while loop == 1:
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == str(""):
        break 
    else:
        for x in range(blok):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(blok):
            robotArm.moveLeft()
        blok = blok + 1
robotArm.wait()