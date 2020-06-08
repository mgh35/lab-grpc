from generated.summer_pb2 import ToSum
import pytest


@pytest.mark.parametrize(["values", "expected"], [
    ([], 0),
    ([1.0], 1.0),
    ([1.0, 1.0], 2.0),
])
def test_some(grpc_stub, values, expected):
    response = grpc_stub.Sum(ToSum(values=values))
    assert response.sum == pytest.approx(expected)
