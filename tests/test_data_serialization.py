import pytest

from src.algorithms.data_serialization import (
    serialize_deserialize_with_json, serialize_deserialize_with_msgpack,
    serialize_deserialize_with_pickle)


@pytest.mark.parametrize("memory_size_kb", [1, 1024, 10240])  # 1KB, 1MB, 10MB in KB
@pytest.mark.data_serialization
def test_serialize_deserialize_with_pickle(benchmark, memory_size_kb: int):
    result = benchmark(serialize_deserialize_with_pickle, memory_size_kb)
    assert result is not None


@pytest.mark.parametrize("memory_size_kb", [1, 1024, 10240])  # 1KB, 1MB, 10MB in KB
@pytest.mark.data_serialization
def test_serialize_deserialize_with_json(benchmark, memory_size_kb: int):
    result = benchmark(serialize_deserialize_with_json, memory_size_kb)
    assert result is not None


@pytest.mark.parametrize("memory_size_kb", [1, 1024, 10240])  # 1KB, 1MB, 10MB in KB
@pytest.mark.data_serialization
def test_serialize_deserialize_with_msgpack(benchmark, memory_size_kb: int):
    result = benchmark(serialize_deserialize_with_msgpack, memory_size_kb)
    assert result is not None
