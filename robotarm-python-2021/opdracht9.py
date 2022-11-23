from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
# robotArm.speed = 2
for x in range(10):
    if x == 1 :
        robotArm.moveRight()
    if x  == 3 :   
        robotArm.moveRight()
    if x ==  6 :
        robotArm.moveRight() 
    if x ==  10 :
        robotArm.wait()
    robotArm.grab()
    for x in range(5):
        robotArm.moveRight()
    robotArm.drop() 
    for x in range(5):
        robotArm.moveLeft()
robotArm.wait()











