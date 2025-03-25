#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import NavSatFix

class DronePositionPublisher(Node):
    def __init__(self):
        super().__init__('drone_position_publisher') 
        self.publisher = (self.create_publisher(NavSatFix, 'drone_position', 10))
        self.timer = (self.create_timer(1.0, self.publish_position)) 

    def publish_position(self):
        msg = NavSatFix()
        msg.latitude = 37.7749   # Latitud simulada
        msg.longitude = -122.4194  # Longitud simulada
        msg.altitude = 50.0  # Altitud en metros
        self.publisher.publish(msg) 
        self.get_logger().info(f'Publicando posición: Lat: {msg.latitude}, Lon: {msg.longitude}, Alt: {msg.altitude}')

def main(args=None):
    rclpy.init(args=args)
    node = DronePositionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
