#!/usr/bin/env python3
# license removed for brevity
import rospy
from assignment0.msg import TwoInt
from random import seed
from random import randint

def generator():
    pub = rospy.Publisher('numbers', TwoInt, queue_size=10)
    rospy.init_node('generator', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        
        
        msg = TwoInt()
        msg.num1 = randint(0,100)
        msg.num2 = randint(0,100)
    
        #rospy.loginfo("The numbers are: %s", msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        generator()
    except rospy.ROSInterruptException:
        pass
