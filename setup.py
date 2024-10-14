import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ros_lessons'

data_files=[
            ('share/ament_index/resource_index/packages', ['resource/' + package_name]), ('share/' + package_name, ['package.xml']),
            (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), # added for launch files
            (os.path.join('share', package_name, 'config'), glob('config/*')), # added for config files
        ]
for robot_name in os.listdir('robots'): # to extract all the robots and placed them nicely in the install folder
    data_files.append((os.path.join('share', package_name, robot_name, 'meshes/collision'), glob(('robots/' + robot_name + '/meshes/collision/*'))))
    data_files.append((os.path.join('share', package_name, robot_name, 'meshes/visual'),    glob(('robots/' + robot_name + '/meshes/visual/*'  ))))
    data_files.append((os.path.join('share', package_name, robot_name, 'urdf'),             glob(('robots/' + robot_name + '/urdf/*'  ))))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
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
