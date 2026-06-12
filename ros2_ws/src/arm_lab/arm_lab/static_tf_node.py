import rclpy
from rclpy.node import Node

from geometry_msgs.msg import TransformStamped
from tf2_ros import StaticTransformBroadcaster


class StaticTFNode(Node):

    def __init__(self):
        super().__init__("static_tf_node")

        self.broadcaster = StaticTransformBroadcaster(self)

        transform = TransformStamped()

        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = "base_link"
        transform.child_frame_id = "camera_link"

        transform.transform.translation.x = 0.0
        transform.transform.translation.y = 0.0
        transform.transform.translation.z = 1.0

        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = 0.0
        transform.transform.rotation.w = 1.0

        self.broadcaster.sendTransform(transform)

        self.get_logger().info("Published static transform: base_link -> camera_link")


def main(args=None):
    rclpy.init(args=args)

    node = StaticTFNode()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
