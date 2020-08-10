#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from time import sleep

def pasarela():
    pub = rospy.Publisher('navcom', String, queue_size=10)
    rospy.init_node('pasarela', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        dirstr = "left"
        pub.publish(dirstr)
        sleep(5)
        dirstr = "right"
        pub.publish(dirstr)
        sleep(5)
        dirstr = "forward"
        pub.publish(dirstr)
        sleep(5)
        dirstr = "backward"
        pub.publish(dirstr)
        sleep(5)
        dirstr = "stop"
        pub.publish(dirstr)
        sleep(5)

if __name__ == '__main__':
    try:
        pasarela()
    except rospy.ROSInterruptException:
        pass

