#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class SquareService(Node):
    def __init__(self):
        super().__init__('square_service')
        self.srv = self.create_service(AddTwoInts, 'calculate_square', self.calculate_square)
        self.get_logger().info('Servicio listo para calcular el cuadrado de un número.')

    def calculate_square(self, request, response):
        response.sum = request.a ** 2  # Calcula el cuadrado
        self.get_logger().info(f'Recibido: {request.a}, Enviando: {response.sum}')
        return response

def main():
    rclpy.init()
    node = SquareService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
