from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 2

for b in range(1, 5):  
    print(b)
    for x in range(b):
        robotArm.grab()
        for x in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()

robotArm.wait()


