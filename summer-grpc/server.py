from concurrent import futures
from generated import summer_pb2, summer_pb2_grpc
import grpc
import logging


class SummerServicer(summer_pb2_grpc.SummerServicer):

    def Sum(self, request: summer_pb2.ToSum, context):
        logging.info("SummerServicer.Sum(%s)", request)
        s = sum(request.values)
        return summer_pb2.Summed(sum=s)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    summer_pb2_grpc.add_SummerServicer_to_server(
        SummerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
