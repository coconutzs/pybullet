import pybullet as p
import time
import pybullet_data
joint_info_name = ['jointIndex', 'jointName', 'jointType', 'qIndex', 'uIndex', 'flags', 'jointDamping', 'jointFriction', 'jointLowerLinit', 'jointUpperLimit', 'jointMaxForce', 'jointMaxVelocity', 'linkName', 'jointAxis', 'parentFramePos', 'parentFrameOrn', 'parentIndex']

physicsClient = p.connect(p.GUI, options="--width=1920 --height=1080")

print("\n*** Start ***\n")
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)
planeId = p.loadURDF("plane.urdf")

startPos = [0, 0, 1]
startOri = p.getQuaternionFromEuler([-1, -1, -1])

robot1_id = p.loadURDF("r2d2.urdf", startPos, startOri)

for i in range(500):
    p.stepSimulation()
    time.sleep(1./240.)

robot1_nj = p.getNumJoints(robot1_id)
print("\n### Robot1")
print("ID: \t", robot1_id)
print("Num joints: \t", robot1_nj)

for j in range(robot1_nj):
    print("\nJoint%d" % j)
    robot1_j = p.getJointInfo(robot1_id, j)
    for i in range(len(joint_info_name)):
        print("%-20s" % joint_info_name[i], robot1_j[i])

print("\n*** End ***\n")
p.disconnect()

