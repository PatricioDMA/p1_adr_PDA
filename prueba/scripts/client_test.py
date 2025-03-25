#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class SquareClient(Node):
    def __init__(self):
        super().__init__('square_client')
        self.client = self.create_client(AddTwoInts, 'calculate_square')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando el servicio...')

    def send_request(self, number):
        request = AddTwoInts.Request()
        request.a = number

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f'Respuesta recibida: {future.result().sum}')
        else:
            self.get_logger().error('Error al llamar al servicio.')

def main():
    rclpy.init()
    node = SquareClient()
    number = 5  # Número de prueba
    node.send_request(number)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
