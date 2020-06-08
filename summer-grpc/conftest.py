import pytest


@pytest.fixture(scope='module')
def grpc_add_to_server():
    from generated.summer_pb2_grpc import add_SummerServicer_to_server
    return add_SummerServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from server import SummerServicer
    return SummerServicer()


@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    from generated.summer_pb2_grpc import SummerStub
    return SummerStub
