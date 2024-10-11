import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ros_lessons'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]), ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), # added for launch files
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gu',
    maintainer_email='gubo@mmmi.sdu.dk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'param_node = ros_lessons.python_parameters_node:main',
            'send_str_clt = ros_lessons.send_str_clt:main',
            'send_str_srv = ros_lessons.string_srv:main',
            'fibonacci_action_server = ros_lessons.fibonacci_action_server:main',
            'fibonacci_action_client = ros_lessons.fibonacci_action_client:main',
        ],
    },
)
