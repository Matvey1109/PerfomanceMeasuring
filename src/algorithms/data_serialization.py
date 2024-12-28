import json
import os
import pickle

import msgpack


def serialize_deserialize_with_pickle(memory_size_kb: int) -> bool:
    """Serialize and deserialize data using pickle"""
    data: bytes = os.urandom(memory_size_kb * 1024)  # Convert KB to bytes
    serialized_data: bytes = pickle.dumps(data)
    deserialized_data: bytes = pickle.loads(serialized_data)

    return data == deserialized_data


def serialize_deserialize_with_json(memory_size_kb: int) -> bool:
    """Serialize and deserialize data using JSON"""
    data: bytes = os.urandom(memory_size_kb * 1024)  # Convert KB to bytes
    serialized_data: bytes = json.dumps(data.decode("latin1")).encode("utf-8")
    deserialized_data: bytes = bytes(json.loads(serialized_data).encode("latin1"))

    return data == deserialized_data


def serialize_deserialize_with_msgpack(memory_size_kb: int) -> bool:
    """Serialize and deserialize data using msgpack"""
    data: bytes = os.urandom(memory_size_kb * 1024)  # Convert KB to bytes
    serialized_data: bytes = msgpack.packb(data)  # type: ignore
    deserialized_data: bytes = msgpack.unpackb(serialized_data)

    return data == deserialized_data
