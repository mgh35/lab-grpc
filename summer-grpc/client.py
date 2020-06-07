from generated import summer_pb2, summer_pb2_grpc
import grpc
import sys
import typing


def run(values: typing.List[int]):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = summer_pb2_grpc.SummerStub(channel)

        summed = stub.Sum(summer_pb2.ToSum(values=values))
        print(summed)


if __name__ == "__main__":
    values = [float(_) for _ in sys.argv[1:]]
    run(values)
