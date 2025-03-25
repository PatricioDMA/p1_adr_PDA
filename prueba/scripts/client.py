#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys  # Importar para leer argumentos de la terminal

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
            self.get_logger().info(f'El cuadrado de {number} es: {future.result().sum}')
        else:
            self.get_logger().error('Error al llamar al servicio.')

def main():
    rclpy.init()

    # Comprobar si el usuario proporcionó un argumento
    if len(sys.argv) < 2:
        print("Uso: ros2 run mi_paquete client.py <número>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])  # Convertir el argumento a un número entero
    except ValueError:
        print("Error: El argumento debe ser un número entero.")
        sys.exit(1)

    node = SquareClient()
    node.send_request(number)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
