from collections import Counter
from time import perf_counter


def even_numbers_sum(numbers: list[int]) -> int:
    """
    Create a function that takes a list of integers as input
    and returns the sum of all even numbers in the list.
    """
    return sum(number for number in numbers if number % 2 == 0)


def count_word_in_sentence(sentence: str) -> dict[str, int]:
    """
    Create a function that takes a string as input
    and returns a dictionary containing the count of each word in the string.
    """
    return dict(
        Counter(
            sentence.lower()
            .replace("?", "")
            .replace("!", "")
            .replace(",", "")
            .replace(".", "")
            .split()
        )
    )


def unique_values_list(numbers: list[int]) -> list[int]:
    """
    Create a function that takes a list of numbers as input
    and returns a list containing only the unique values in the list.
    """
    return list(set(numbers))


def squares(numbers: tuple[int]) -> int:
    """
    Create a function that takes a tuple of numbers as input
    and returns the sum of the squares of each number in the tuple.
    """
    return sum(number**2 for number in numbers)


def timer(function):
    """
    Create a decorator function timer that prints
    the time taken to execute a function.
    The decorator should work for functions that
    take any number of arguments.
    """

    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        stop = perf_counter()
        print(f"The time taken to execute a function = {stop - start}")
        return result

    return wrapper


def list_of_strings_with_capital_letter(words_list: list[str]) -> list[str]:
    """
    Create a function that takes a list of strings
    as input and returns a list of strings containing
    only the strings that start with a capital letter.
    """
    return list(filter(lambda word: len(word) > 0 and word[0].isupper(), words_list))


def list_of_numbers_divisible_by_3(numbers: list[int]) -> list[int]:
    """
    Create a function that takes a list of numbers
    as input and returns a list containing only
    the numbers that are divisible by 3. Use the built-in
    filter() function and a lambda function to achieve this.
    """
    return list(filter(lambda x: x % 3 == 0, numbers))


def fibonacci():
    """
    Create a generator function fibonacci() that yields
    the next number in the Fibonacci sequence each time it is called.
    """
    a, b = 0, 1

    while True:
        yield a
        a, b = a + b, a


def lists_to_tuple_list(numbers: list[int], digits: list[int]) -> list[tuple[int, int]]:
    """
    Create a function that takes two lists of numbers
    as input and returns a list containing the product
    of each pair of numbers from the two lists.
    """
    return [number * digit for number, digit in zip(numbers, digits)]
