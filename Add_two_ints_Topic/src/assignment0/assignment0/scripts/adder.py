#!/usr/bin/env python3
import rospy
from assignment0.msg import TwoInt
from std_msgs.msg import Int16

def callback(data):
    #rospy.loginfo(" The numbers are: %s" , (data.num1, data.num2))
    pub2 = rospy.Publisher('sum', Int16, queue_size=10)
    total = data.num1 + data.num2
    msg2 = Int16()
    msg2.data = total
    #rospy.loginfo("The sum is: %s" , (total))
    pub2.publish(total)

def adder():
    rospy.init_node('adder', anonymous=True)
    rospy.Subscriber("numbers", TwoInt, callback)

    
    rospy.spin()

if __name__ == '__main__':
    adder()
