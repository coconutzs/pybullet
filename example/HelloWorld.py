import pybullet as p
import time
import pybullet_data

phsicsClient = p.connect(p.GUI, options="--width=1920, --height=1080")
p.setAdditionalSearchPath(pybullet_data.getDataPath())
print("\n\n*** Start ***\n\n")

p.setGravity(0, 0, -30)
planeId = p.loadURDF("plane.urdf")
cubePos = [0, 0, 1]
cubeOri = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("r2d2.urdf", cubePos, cubeOri)

for i in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)

cubePos_, cubeOri_ = p.getBasePositionAndOrientation(boxId)
print("Pos: ", cubePos_, "\nOri: ", cubeOri_)

print("\n\n**** End ****\n\n")
p.disconnect()


