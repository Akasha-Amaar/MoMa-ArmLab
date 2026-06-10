import rclpy
from rclpy.node import Node


class ParameterNode(Node):

    def __init__(self):
        super().__init__("parameter_node")

        self.declare_parameter("robot_name", "reactor_arm")
        self.declare_parameter("publish_rate", 1.0)

        robot_name = self.get_parameter("robot_name").value
        publish_rate = self.get_parameter("publish_rate").value

        self.get_logger().info(f"Robot name: {robot_name}")
        self.get_logger().info(f"Publish rate: {publish_rate}")


def main(args=None):
    rclpy.init(args=args)

    node = ParameterNode()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()

