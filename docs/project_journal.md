# MoMa-ArmLab Project Journal

## Project Goal

MoMa-ArmLab is the preparation project for the larger MoMa (Mobile Manipulation) warehouse robotics project.

The purpose of MoMa-ArmLab is to learn:

* ROS 2 Humble
* RViz2
* Gazebo
* MoveIt 2
* Robot Modeling (URDF/Xacro)
* TF Trees
* ros2_control
* Git & GitHub workflows
* Docker
* Manipulator integration

before building the full mobile manipulation warehouse system.

---

# Progress Log

## Step 1 — System Verification

Verified operating system:

Ubuntu 22.04.5 LTS

Verified ROS installation:

ROS 2 Humble

Commands used:

```bash
lsb_release -a
printenv | grep ROS
which ros2
```

Purpose:

Learn how to verify the development environment before starting a robotics project.

---

## Step 2 — ROS Sanity Check

Verified ROS communication layer.

Command:

```bash
ros2 topic list
```

Observed topics:

```text
/parameter_events
/rosout
```

Purpose:

Confirm ROS 2 installation is functional.

---

## Step 3 — Project Creation

Created project directory:

```text
~/MoMa-ArmLab
```

Purpose:

Separate project files from other ROS workspaces and university projects.

---

## Step 4 — Git Initialization

Initialized Git repository:

```bash
git init
```

Renamed branch:

```bash
git branch -m main
```

Purpose:

Create version-controlled project from day one.

---

## Step 5 — Project Structure

Current structure:

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

Purpose:

Separate documentation, ROS workspace, Docker files, and project assets.

---

## Step 6 — GitHub Integration

GitHub repository:

MoMa-ArmLab

GitHub user:

Akasha-Amaar

Connected local repository to GitHub:

```bash
git remote add origin <repository-url>
```

Pushed first commit:

```bash
git push -u origin main
```

Purpose:

Learn local-to-remote development workflow.

---

# Concepts Learned

## Git Workflow

```text
Working Directory
        ↓
git add
        ↓
Staging Area
        ↓
git commit
        ↓
Local Repository
        ↓
git push
        ↓
GitHub Repository
```

---

## Project vs Workspace

Project:

```text
MoMa-ArmLab/
```

ROS Workspace:

```text
MoMa-ArmLab/ros2_ws/
```

ROS Packages:

```text
MoMa-ArmLab/ros2_ws/src/
```

Important:

A project can contain one or more ROS workspaces.

---

# Current Status

Completed:

* Environment verification
* ROS verification
* Git setup
* GitHub setup
* Project structure creation
* ROS workspace creation

Not Started:

* ROS package creation
* Robot simulation
* RViz
* Gazebo
* MoveIt 2
* Interbotix Reactor arm

---

# Planned Roadmap

Phase 1

* ROS package creation
* Workspace build process
* Understanding package.xml
* Understanding setup.py

Phase 2

* Interbotix Reactor simulation
* RViz visualization
* MoveIt setup

Phase 3

* Gazebo simulation

Phase 4

* Robot control with Python

Phase 5

* Pick and place

Phase 6

* Mobile robot integration

Phase 7

* Navigation (Nav2)

Phase 8

* Camera integration

Phase 9

* Dockerization

Phase 10

* Full MoMa warehouse project

---

# Notes

The goal is not only to learn one robot.

The goal is to learn a repeatable engineering process that can be applied to any robotic platform in industry.
