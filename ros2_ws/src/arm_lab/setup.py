from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'arm_lab'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',
    	glob('launch/*.launch.py')),
    	('share/' + package_name + '/config',
    	glob('config/*.yaml')),
    	],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akasha',
    maintainer_email='akashaamaar786@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [ 'hello_node = arm_lab.hello_node:main',
        'talker_node = arm_lab.talker_node:main',
        'listener_node = arm_lab.listener_node:main',
	'add_two_ints_server = arm_lab.add_two_ints_server:main',
	'fibonacci_action_server = arm_lab.fibonacci_action_server:main',
	'parameter_node = arm_lab.parameter_node:main',
        ],
    },
)
