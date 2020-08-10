#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial
arduino=serial.Serial('/dev/ttyUSB0',9600)  # Serial configuration for communication with Arduino

def callback(data):                         
    cadvel="%s"+"\n",data.data
    arduino.write(data.data)
    rospy.loginfo(rospy.get_caller_id() + " Motors Velocity  L,R= %s ", data.data)


def motors():

    rospy.init_node('motors', anonymous=True)

    rospy.Subscriber("velocity", String, callback)

    rospy.spin()

    arduino.close()

if __name__ == '__main__':
    motors()
