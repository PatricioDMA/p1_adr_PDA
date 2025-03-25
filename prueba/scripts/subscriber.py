#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import NavSatFix

class DronePositionSubscriber(Node):
    def __init__(self):
        super().__init__('drone_position_subscriber') 
        self.subscription = self.create_subscription(NavSatFix, 'drone_position', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Recibido -> Latitud: {msg.latitude}, Longitud: {msg.longitude}, Altitud: {msg.altitude}')

def main(args=None):
    rclpy.init(args=args)
    node = DronePositionSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
