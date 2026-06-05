# AI Handover Document

## Project: MoMa-ArmLab → MoMa

Author: Akasha-Amaar

Purpose:
This document allows any future AI assistant (or future ChatGPT conversation) to immediately understand the project, teaching style, current status, roadmap, and user preferences.

---

# User Goals

The ultimate goal is to become an industry-ready Robotics Engineer.

Primary interests:

* Manipulators
* Cobots
* Mobile Robots
* ROS 2
* Gazebo
* RViz2
* MoveIt 2
* Docker
* Git/GitHub

The user wants to understand not only how to use a robot but also how to approach a completely new robotic platform professionally.

Example:

If given a new robot in industry, the user wants to know:

1. How to verify compatibility.
2. How to inspect documentation.
3. How to clone repositories.
4. How to build workspaces.
5. How to understand package structures.
6. How to launch simulation.
7. How to debug issues.
8. How to integrate into existing projects.

---

# Final Project

Project Name:

MoMa

Meaning:

Mobile Manipulation

Project Description:

A warehouse logistics robot that:

* Navigates autonomously.
* Uses a manipulator to pick objects.
* Uses perception.
* Delivers objects to a drop-off location.

Technologies:

* ROS 2 Humble
* Python
* Gazebo
* RViz2
* MoveIt 2
* Nav2
* SLAM Toolbox
* OpenCV
* Docker
* Git/GitHub

Everything is simulation only.

No hardware.

---

# Current Learning Project

Project Name:

MoMa-ArmLab

Purpose:

Learn manipulation fundamentals before starting MoMa.

Chosen Manipulator:

Interbotix Reactor / X-Series style arm.

Reason:

* Easier than UR5.
* Good ROS2 support.
* Good MoveIt integration.
* Good documentation.

Future migration to UR5 remains possible.

---

# Teaching Methodology

The user explicitly requested:

* Start completely from scratch.
* Explain industry workflow.
* Explain why every step is performed.
* Teach concepts before tools.
* Use very small steps.
* Avoid large jumps.
* Prefer brief answers.
* Avoid unnecessarily long explanations.
* Focus on understanding.

The assistant should act as:

* Robotics mentor
* Senior engineer
* Technical guide

Not as:

* Tutorial dump
* Code generator

The assistant should frequently ask:

"What do you think will happen?"

to encourage engineering thinking and prediction.

---

# Important User Preferences

Environment:

* Ubuntu 22.04
* ROS 2 Humble
* Python
* GitHub username:
  Akasha-Amaar

Version Control:

* Uses GitHub
* Uses Personal Access Tokens (PAT)
* SSH may be learned later

Development Style:

* Learn by building.
* Commit often.
* Push often.
* Understand before moving forward.

---

# Completed Work

Environment verification:

Verified:

* Ubuntu 22.04.5
* ROS 2 Humble
* ROS installation working

Commands used:

```bash
lsb_release -a
printenv | grep ROS
which ros2
ros2 topic list
```

---

GitHub setup:

Created repository:

MoMa-ArmLab

Initialized Git.

Renamed branch:

main

Created first commits.

Connected GitHub remote.

Pushed successfully.

---

Project structure:

```text
MoMa-ArmLab/
├── assets/
├── docker/
├── docs/
├── scripts/
├── ros2_ws/
│   └── src/
└── README.md
```

---

Workspace creation:

Created:

```text
ros2_ws/src
```

Learned:

* Workspace
* Package
* Source code structure

---

First ROS Package

Created:

```bash
ros2 pkg create --build-type ament_python arm_lab
```

Learned:

* package.xml
* setup.py
* setup.cfg
* resource folder
* package hierarchy

---

Workspace Build Process

Learned:

```bash
colcon build
```

Creates:

```text
build/
install/
log/
```

---

Sourcing

Learned:

```bash
source install/setup.bash
```

Purpose:

Make ROS aware of workspace packages.

Learned difference between:

```bash
source /opt/ros/humble/setup.bash
```

and

```bash
source install/setup.bash
```

---

First ROS Node

Created:

```text
arm_lab/hello_node.py
```

Learned:

* Python script
* ROS node
* rclpy
* Node names
* Logging

---

setup.py Entry Points

Learned:

```python
'hello_node = arm_lab.hello_node:main'
```

Purpose:

Expose executable through ROS.

---

ros2 run

Learned:

```bash
ros2 run arm_lab hello_node
```

---

Node Lifetime

Learned:

```python
rclpy.spin(node)
```

Purpose:

Keep node alive and listening for events.

---

ROS Graph Inspection

Learned:

```bash
ros2 node list
```

Observed:

```text
/hello_node
```

---

Current Status

Completed:

* ROS installation verification
* Git setup
* GitHub setup
* Workspace creation
* Package creation
* Build process
* Sourcing
* First ROS node
* First ROS executable
* Node inspection

Current skill level:

Beginning ROS developer with understanding of:

* Workspaces
* Packages
* Nodes
* Build process
* Sourcing
* Git workflow

---

Next Immediate Phase

ROS Communication Fundamentals

Topics

Create:

* Publisher node
* Subscriber node

Learn:

* Topics
* Messages
* Publishers
* Subscribers

Commands to learn:

```bash
ros2 topic list
ros2 topic echo
ros2 topic info
```

---

Future Roadmap

Phase 1
ROS communication

Phase 2
Services

Phase 3
Actions

Phase 4
TF

Phase 5
URDF

Phase 6
Xacro

Phase 7
RViz2

Phase 8
Gazebo

Phase 9
Interbotix simulation

Phase 10
MoveIt 2

Phase 11
Manipulation

Phase 12
Mobile robot integration

Phase 13
Navigation (Nav2)

Phase 14
Perception

Phase 15
Docker

Phase 16
MoMa warehouse project

---

Mission Statement

The objective is not merely to learn one robot.

The objective is to develop a reusable engineering process that allows the user to approach any robotic platform confidently in industry.
