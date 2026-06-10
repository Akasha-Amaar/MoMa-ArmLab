from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    talker = Node(
        package="arm_lab",
        executable="talker_node",
        name="talker_node"
    )

    listener = Node(
        package="arm_lab",
        executable="listener_node",
        name="listener_node"
    )

    return LaunchDescription([
        talker,
        listener
    ])
