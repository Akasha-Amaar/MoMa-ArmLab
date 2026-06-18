import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    pkg_path = get_package_share_directory("arm_lab")

    world_file = os.path.join(pkg_path, "worlds", "empty_world.sdf")
    xacro_file = os.path.join(pkg_path, "urdf", "simple_robot.urdf.xacro")

    robot_description = Command(["xacro ", xacro_file])

    gazebo = ExecuteProcess(
        cmd=["gz", "sim", "-v", "4", "-r", world_file],
        output="screen"
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {"robot_description": robot_description}
        ]
    )

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-world", "empty_world",
            "-name", "simple_robot",
            "-topic", "robot_description",
            "-x", "0",
            "-y", "0",
            "-z", "0.5"
        ],
        output="screen"
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot
    ])
