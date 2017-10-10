import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan

#Defining a function

i = 0
def turnRight():
	drive(2.5,-2.5)
	i=1
def turnLeft():
	drive(-2.5,2.5)
	i=2
def forWard():
	drive(1.0,1.0)
	i=3
def backWard():
	drive(-1.0,-1.0)
	i=4
def stop():
	drive(0.0,0.0)
	i=5

def handleNewData(data):
	midpoint = len(data.ranges)/2
	right = data.ranges[120]
	left = data.ranges[478]
	center = data.ranges[midpoint]


	if i == 1 or center <= 0.30:
	if right >= 0.10:		
		turnRight()
	if right <= 0.10:
		stop()
	if center > 0.30 and i != 1 and i != 2:
		forWard()

# Intitalize ros
rospy.init_node("maze_wanderer")


# Created publisher (maze_wandere is publishing data to the belowe nodes)
flw_pub = rospy.Publisher("/front_left_wheel_controller/command", Float64, queue_size=0)
frw_pub = rospy.Publisher("/front_right_wheel_controller/command", Float64, queue_size=0)
blw_pub = rospy.Publisher("/back_left_wheel_controller/command", Float64, queue_size=0)
brw_pub = rospy.Publisher("/back_right_wheel_controller/command", Float64, queue_size=0)
#rospy.Publisher(node, data type, queue_size)

# Function that used publisher
def drive(left,right):
	flw_pub.publish(left)
	blw_pub.publish(left)
	frw_pub.publish(right)
	brw_pub.publish(right)

while exit != 'q':
#Created Subscriber (maze_wanderer is subscribed to /scan > maze_wanderer takes data from /scan)
	laser = rospy.Subscriber("/scan", LaserScan, handleNewData)
	exit = raw_input()
#rospy.Subscriber(node, data type, function to run)


