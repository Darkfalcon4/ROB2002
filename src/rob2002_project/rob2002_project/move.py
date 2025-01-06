import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np
class Moves(Node):
    def __init__(self):
        super().__init__('move')

        # Create a publisher for the cmd_vel topic
        self.publisher_= self.create_publisher(Twist, 'cmd_vel', 10)
        # self.odom_publisher = self.create_publisher(,'cmd_vel',10)

        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.moving)
        self.i = 0

    def moving(self):
        twist_msg = Twist()
        while True:
            msg = Twist()
            msg.angular.z = -0.1
            self.publisher_.publish(msg)
    # def odomError(self, N):
    #     MBE , STD , MAE , RMSE = 0 
    #     ei = []  
    #     for x in range (N) : 
    #      ei.append(x)
    #     self.odom_publisher.publish(ei)
        
        

def main(args=None):

    rclpy.init(args=args)

    movement = Moves()

    rclpy.spin(movement)
   

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    movement.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()