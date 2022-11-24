from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 2

# for x in range(8):
#     robotArm.moveRight() 
for x in range(9):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur != "white":         
        robotArm.drop()
        robotArm.moveRight()
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveRight()

robotArm.wait()