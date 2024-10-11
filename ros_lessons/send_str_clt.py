from custom_interfaces.srv import String
import rclpy
from rclpy.node import Node
import sys

class SendStrClient(Node):
    """
    A client to send request to a ros service, the class inherit from rclpy.node.Node
    """
    def __init__(self, name: str=None):
        """Constructor

        Args:
            name (str, optional):   The name of the service that the client will connect to, it also serve to generate 
                                    the  name of the client node
        """
        super().__init__(name + "_client")
        if name is None:
            name = 'generic_send_str'
        self.cli = self.create_client(String, name)
        self.future = None

        while not self.cli.wait_for_service(timeout_sec=5):
            self.get_logger().info('service {} not available, waiting again...'.format(self.cli.srv_name))
            
    def send_request(self, data: String=""):
        """Send a string to the connected service

        Args:
            data (String, optional): The string that will be sent. Defaults to "".

        Returns:
            custom_interfaces.srv.String: Response from the service
        """
        self.req = String.Request()
        self.req.data = data
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main():
    rclpy.init()
    clt = SendStrClient("generic_send_str")
    response = clt.send_request("Hello World!")
    clt.get_logger().info("Response: " + str(response.ans))

if __name__ == '__main__':
    rclpy.init()
    if len(sys.argv) != 3:
        print("Usage: ros2 run <package> <exe> service_name string_data")
        quit()
    clt = SendStrClient(sys.argv[1])
    clt.send_request(sys.argv[2])
