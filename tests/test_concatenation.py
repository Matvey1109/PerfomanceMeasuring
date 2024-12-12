import pytest

from src.algorithms.string_concatenation import (concatenate_with_join,
                                                 concatenate_with_plus_equals)


@pytest.mark.parametrize(
    "number_of_strings, size_of_string", [(10, 10), (100, 20), (1000, 5)]
)
@pytest.mark.string_concatenation
def test_concatenate_with_plus_equals(benchmark, number_of_strings, size_of_string):
    result = benchmark(concatenate_with_plus_equals, number_of_strings, size_of_string)
    assert len(result) == number_of_strings * size_of_string


@pytest.mark.parametrize(
    "number_of_strings, size_of_string", [(10, 10), (100, 20), (1000, 5)]
)
@pytest.mark.string_concatenation
def test_concatenate_with_join(benchmark, number_of_strings, size_of_string):
    result = benchmark(concatenate_with_join, number_of_strings, size_of_string)
    assert len(result) == number_of_strings * size_of_string
