import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):

    def __init__(self):
        super().__init__("add_two_ints_server")

        self.server = self.create_service(
            AddTwoInts,
            "add_two_ints",
            self.add_callback
        )

        self.get_logger().info("Add Two Ints Server is ready.")

    def add_callback(self, request, response):
        response.sum = request.a + request.b

        self.get_logger().info(
            f"Received: {request.a} + {request.b} = {response.sum}"
        )

        return response


def main(args=None):
    rclpy.init(args=args)

    node = AddTwoIntsServer()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
