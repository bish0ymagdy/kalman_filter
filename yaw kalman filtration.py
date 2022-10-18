import rospy
from std_msgs.msg import String
x_last=20
p_last=10

def yaw_est(data):
    z=data
    r=3
    q=3
    x_pre=x_last
    p_pre=p_last+q
    y=z-x_pre
    k=p_pre/(p_pre+r)
    x_c=x_pre+(k*y)
    p_c=(1-k)*p_pre
    x_last=x_c
    p_last=p_c


def yaw_kalman():
    rospy.init_node('yaw_kalman', anonymous=True)
    rospy.Subscriber("yaw", Float32, yaw_est)
    rospy.spin()
if __name__ == '__main__':
    yaw_kalman()