#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from time import sleep

state="in" #State Variable

def callback(data):
    pub = rospy.Publisher('velocity', String, queue_size=10)
    cadvel=data.data #string evaluation
    if "left"==cadvel:
        state="l"
    elif "right"==cadvel:
        state="r"
    elif "forward"==cadvel:
        state="f"
    elif "backward"==cadvel:
        state="b"
    elif "stop"==cadvel:
        state="s"
    else: 
        state="in"
    rospy.loginfo(rospy.get_caller_id() + " State  = %s ", state) #state uodate
    if state=="in":
        rospy.loginfo("Inctive State")
    elif state=="l":
        rospy.loginfo("Left Turn")
        dirstr = "-300,300\n"
        pub.publish(dirstr)
        sleep(3)
        dirstr = "0,0\n"
        pub.publish(dirstr)
    elif state=="r":
        rospy.loginfo("Right Turn")
        dirstr = "300,-300\n"
        pub.publish(dirstr)
        sleep(3)
        dirstr = "0,0\n"
        pub.publish(dirstr)
    elif state=="f":
        rospy.loginfo("Forward")
        dirstr = "300,300\n"
        pub.publish(dirstr)
    elif state=="b":
        rospy.loginfo("Backward")
        dirstr = "-300,-300\n"
        pub.publish(dirstr)
    elif state=="s":
        rospy.loginfo("Stop")
        dirstr = "0,0\n"
        pub.publish(dirstr)
    else:
        rospy.loginfo("State Error")

    
    
def easynav():
    rospy.init_node('easynav', anonymous=True)
    rospy.Subscriber("navcom", String, callback)
    rospy.spin()
    
if __name__ == '__main__':
    easynav()
        
        
    
        
