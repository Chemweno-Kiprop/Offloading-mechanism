import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from cv_bridge import CvBridge
import cv2
import numpy as np

class VisionNode(Node):
    def __init__(self):
        super().__init__('vision_node')
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        self.object_pub = self.create_publisher(Bool, '/object_detected', 10)
        self.zone_pub = self.create_publisher(Bool, '/at_drop_zone', 10)
        self.get_logger().info("Vision node started.")

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        # Example: detect red object
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        red_area = cv2.countNonZero(mask)

        # Example thresholds — tune these
        object_detected = red_area > 500
        at_drop_zone = red_area < 200 and self.get_clock().now().nanoseconds % 2e9 < 1e9  # placeholder logic

        self.object_pub.publish(Bool(data=object_detected))
        self.zone_pub.publish(Bool(data=at_drop_zone))

def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
