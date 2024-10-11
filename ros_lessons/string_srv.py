from custom_interfaces.srv import String
import rclpy
from rclpy.node import Node
import time
import std_msgs.msg
import random

class ServicesPlaceholder(Node):
    """Use this class if you want to test clients and you have not implemented the services yet, inherits from 
       rclpy.node.Node
    """
    def __init__(self):
        super().__init__('services_place_holder')        
        self.create_service(String, 'generic_send_str', self.string_callback)
        
    def string_callback(self, request, response):
        self.get_logger().info(f"Request with data: {request.data}")
        response.ans = "success"   
        self.get_logger().info("Responding SUCCESS\n")
        return response

def main(args=None):
    rclpy.init(args=args)
    send_pose_server = ServicesPlaceholder()
    rclpy.spin(send_pose_server)
    rclpy.shutdown()


if __name__ == '__main__':
    main()