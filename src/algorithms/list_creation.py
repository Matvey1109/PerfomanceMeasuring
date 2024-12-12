import numpy as np


def create_list_comprehension(size):
    """Function using list comprehension"""
    return [i for i in range(size)]


def create_list_for_loop(size):
    """Function using a for loop"""
    result = []
    for i in range(size):
        result.append(i)
    return result


def create_list_numpy_creation(size):
    """Function using numpy"""
    return np.arange(size).tolist()
