import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():
    world_file = os.path.join(
        get_package_share_directory("arm_lab"),
        "worlds",
        "empty_world.sdf"
    )

    gazebo = ExecuteProcess(
        cmd=["gz", "sim", world_file],
        output="screen"
    )

    return LaunchDescription([
        gazebo
    ])
