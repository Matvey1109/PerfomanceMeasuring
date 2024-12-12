import numpy as np


def create_list_comprehension(size: int) -> list[int]:
    """Function using list comprehension"""
    return [i for i in range(size)]


def create_list_for_loop(size: int) -> list[int]:
    """Function using a for loop"""
    result: list[int] = []
    for i in range(size):
        result.append(i)
    return result


def create_list_numpy_creation(size: int) -> list[int]:
    """Function using numpy"""
    return np.arange(size).tolist()
