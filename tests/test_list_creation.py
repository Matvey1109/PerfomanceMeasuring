import pytest

from src.algorithms.list_creation import (create_list_comprehension,
                                          create_list_for_loop,
                                          create_list_numpy_creation)


@pytest.mark.parametrize("size", [100, 1000, 100000])
@pytest.mark.list_creation
def test_list_comprehension(benchmark, size: int):
    result = benchmark(create_list_comprehension, size)
    assert len(result) == size


@pytest.mark.parametrize("size", [100, 1000, 100000])
@pytest.mark.list_creation
def test_list_for_loop(benchmark, size: int):
    result = benchmark(create_list_for_loop, size)
    assert len(result) == size


@pytest.mark.parametrize("size", [100, 1000, 100000])
@pytest.mark.list_creation
def test_list_numpy_creation(benchmark, size: int):
    result = benchmark(create_list_numpy_creation, size)
    assert len(result) == size
