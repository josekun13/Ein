#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from time import sleep

def reader():
    file1 = open("Demo.txt","r") 
    pub = rospy.Publisher('velocity', String, queue_size=10)
    rospy.init_node('reader', anonymous=True) 
    ctxt=file1.readlines()
    file1.close()
    rospy.loginfo("Active")
    for lin in ctxt:
        x=lin.split("|")
        X=int(x[1])
        info_str = x[0]+" \n"
        pub.publish(info_str)
        sleep(X)
    rospy.loginfo("Inctive")

if __name__ == '__main__':
    try:
        reader()
    except rospy.ROSInterruptException:
        pass
