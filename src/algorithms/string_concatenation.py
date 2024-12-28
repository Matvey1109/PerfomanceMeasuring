def concatenate_with_plus_equals(number_of_strings: int, size_of_string: int) -> str:
    """Function using concatenation with plus equals"""
    result: str = ""
    for _ in range(number_of_strings):
        string_to_add: str = "a" * size_of_string
        result += string_to_add
    return result


def concatenate_with_join(number_of_strings: int, size_of_string: int) -> str:
    """Function using concatenation with join"""
    strings_to_join: list[str] = [
        "a" * size_of_string for _ in range(number_of_strings)
    ]
    return "".join(strings_to_join)
