import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

# Define the service implementation
class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.ArithmeticResponse(result=result)
    
    # add the Multiply method
    def Multiply(self, request, context):
        result = request.num1 * request.num2
        return calculator_pb2.ArithmeticResponse(result=result)
    
    # add subtract method
    def Subtract(self, request, context):
        result = request.num1 - request.num2
        return calculator_pb2.ArithmeticResponse(result=result)

# Set up the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
