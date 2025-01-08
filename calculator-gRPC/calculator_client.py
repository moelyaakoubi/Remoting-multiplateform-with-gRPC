import sys

import grpc
import calculator_pb2
import calculator_pb2_grpc

def run(x,y):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        
        # Create an ADD request with two numbers
        request = calculator_pb2.ArithmeticRequest(num1=x, num2=y)

        # Call the Add method
        response = stub.Add(request)

        print(f'Result of {x} + {y} is {response.result}')

        #create a Multiply request with two numbers
        request = calculator_pb2.ArithmeticRequest(num1=x, num2=y)

        # Call the Multiply method
        response= stub.Multiply(request)
        
        print(f'Result of {x} * {y} is {response.result}')

        #create a Subtract request with two numbers
        request = calculator_pb2.ArithmeticRequest(num1=x, num2=y)

        # Call the Subtract method
        response= stub.Subtract(request)

        print(f'Result of {x} - {y} is {response.result}')


if __name__ == '__main__':
    #run()
    run(int(sys.argv[1]), int(sys.argv[2]))