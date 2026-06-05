import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TalkerNode(Node):

    def __init__(self):
        super().__init__("talker_node")

        self.publisher_ = self.create_publisher(
            String,
            "chatter",
            10
        )

        self.timer = self.create_timer(1.0, self.publish_message)

        self.counter = 0

    def publish_message(self):
        msg = String()
        msg.data = f"Hello ROS 2: {self.counter}"

        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")

        self.counter += 1


def main(args=None):
    rclpy.init(args=args)

    node = TalkerNode()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
