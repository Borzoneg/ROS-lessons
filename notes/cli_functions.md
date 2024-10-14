# Terminal useful functions

### to run ros node
    ros2 run <ROS_PACKAGE> <ROS_NODE>
### to launch ros launch file
    ros2 launch <ROS_PACKAGE> <ROS_NODE>
### to change a parameter from terminal: 
    ros2 param set /minimal_param_node my_parameter <NEW_VALUE>
### to see that an interface is been initiated correctly
    ros2 interface show action_tutorials_interfaces/action/Fibonacci
### to send a goal
    ros2 action send_goal fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"
