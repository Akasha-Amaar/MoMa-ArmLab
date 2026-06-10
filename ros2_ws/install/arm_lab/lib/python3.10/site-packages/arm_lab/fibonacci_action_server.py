import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from example_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__("fibonacci_action_server")

        self.action_server = ActionServer(
            self,
            Fibonacci,
            "fibonacci",
            self.execute_callback
        )

        self.get_logger().info("Fibonacci Action Server is ready.")

    def execute_callback(self, goal_handle):
        self.get_logger().info("Goal received.")

        feedback_msg = Fibonacci.Feedback()
        feedback_msg.sequence = [0, 1]

        for i in range(2, goal_handle.request.order):
            next_number = feedback_msg.sequence[i - 1] + feedback_msg.sequence[i - 2]
            feedback_msg.sequence.append(next_number)

            self.get_logger().info(f"Feedback: {feedback_msg.sequence}")
            goal_handle.publish_feedback(feedback_msg)

            time.sleep(1)

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = feedback_msg.sequence

        self.get_logger().info("Goal completed.")
        return result


def main(args=None):
    rclpy.init(args=args)

    node = FibonacciActionServer()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
