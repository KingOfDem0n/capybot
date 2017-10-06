import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan

def handleNewData(data):
	midpoint = len(data.ranges)/2
	right = data.ranges[120]
	left = data.ranges[478]
	
	print(data.ranges[120])
	#print(data.ranges[358])
	#if data.ranges[midpoint] > 0.25:
		#drive(1.0,1.0)
	#elif data.ranges[midpoint] <= 0.25:
		#drive(0.0,0.0)
	

# Intitalize ros
rospy.init_node("maze_wanderer")

#Created Subscriber
laser = rospy.Subscriber("/scan", LaserScan, handleNewData)

# Created publisher
flw_pub = rospy.Publisher("/front_left_wheel_controller/command", Float64, queue_size=0)
frw_pub = rospy.Publisher("/front_right_wheel_controller/command", Float64, queue_size=0)
blw_pub = rospy.Publisher("/back_left_wheel_controller/command", Float64, queue_size=0)
brw_pub = rospy.Publisher("/back_right_wheel_controller/command", Float64, queue_size=0)

# Function that used publisher
def drive(left,right):
	flw_pub.publish(left)
	blw_pub.publish(left)
	frw_pub.publish(right)
	brw_pub.publish(right)


rospy.spin()
	

