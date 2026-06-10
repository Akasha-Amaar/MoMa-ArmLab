import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config_file = os.path.join(
        get_package_share_directory("arm_lab"),
        "config",
        "arm_lab_params.yaml"
    )

    parameter_node = Node(
        package="arm_lab",
        executable="parameter_node",
        name="parameter_node",
        parameters=[config_file]
    )

    return LaunchDescription([
        parameter_node
    ])
