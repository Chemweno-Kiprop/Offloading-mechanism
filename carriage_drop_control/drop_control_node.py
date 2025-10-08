import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, Bool

class DropControlNode(Node):
    def __init__(self):
        super().__init__('drop_control_node')
        self.servo_pub = self.create_publisher(Int16, '/servo_command', 10)
        self.object_sub = self.create_subscription(Bool, '/object_detected', self.object_callback, 10)
        self.zone_sub = self.create_subscription(Bool, '/at_drop_zone', self.zone_callback, 10)

        self.object_present = False
        self.at_zone = False

    def object_callback(self, msg):
        self.object_present = msg.data
        self.check_and_drop()

    def zone_callback(self, msg):
        self.at_zone = msg.data
        self.check_and_drop()

    def check_and_drop(self):
        if self.object_present and self.at_zone:
            self.get_logger().info("✅ Object detected and at drop zone — activating servo.")
            msg = Int16()
            msg.data = 0     # servo drop position
            self.servo_pub.publish(msg)
        else:
            msg = Int16()
            msg.data = 90    # neutral or rest position
            self.servo_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DropControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
