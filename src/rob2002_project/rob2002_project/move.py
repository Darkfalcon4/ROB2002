import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Moves(Node):
    def __init__(self):
        super().__init__('move')

        # Create a publisher for the cmd_vel topic
        self.movement_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.moving)
        self.i = 0

    def moving(self):
        twist_msg = Twist()

        twist_msg.linear.x = 0.2
        twist_msg.linear.z = 0.2

        self.movement_publisher.publish(twist_msg)

def main(args=None):
    print('Starting move_square.py.')

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