import pytest

from tasks import (
    count_word_in_sentence,
    even_numbers_sum,
    list_of_numbers_divisible_by_3,
    list_of_strings_with_capital_letter,
    lists_to_tuple_list,
    squares,
    unique_values_list,
)


@pytest.mark.parametrize(
    "got, expected",
    [
        ([], 0),
        ([1, 2, 3, 4, 5, 6], 12),
        ([2, 4, 6], 12),
        ([1, 3, 5], 0),
    ],
)
def test_even_numbers_sum(got, expected):
    assert even_numbers_sum(got) == expected


@pytest.mark.parametrize(
    "got, expected",
    [
        (
            "Ala ma kota a kot ma Ale",
            {
                "ala": 1,
                "ma": 2,
                "kota": 1,
                "a": 1,
                "kot": 1,
                "ale": 1,
            },
        ),
        ("", {}),
        ("  ", {}),
        ("test test! test, test?", {"test": 4}),
    ],
)
def test_count_word_in_sentence(got, expected):
    assert count_word_in_sentence(got) == expected


@pytest.mark.parametrize(
    "got, expected",
    [
        ([1, 3, 3, 4, 5, 1, 3, 2], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1], [1]),
        ([], []),
    ],
)
def test_unique_values_list(got, expected):
    assert unique_values_list(got) == expected


@pytest.mark.parametrize(
    "got, expected",
    [
        ((1, 2, 3, 4), 30),
        ((), 0),
    ],
)
def test_squares(got, expected):
    assert squares(got) == expected


@pytest.mark.parametrize(
    "got, expected",
    [
        (
            ["Alpha", "beta", "gamma", "ale", "Alicja", "Mama"],
            ["Alpha", "Alicja", "Mama"],
        ),
        (["alpha", "beta", "gamma", "ale", "alicja", "mama"], []),
        ([], []),
        (["alPha", "bEta", "gamma", "alE", "alicja", "mama"], []),
        (["", ""], []),
    ],
)
def test_list_of_strings_with_capital_letter(got, expected):
    assert list_of_strings_with_capital_letter(got) == expected


@pytest.mark.parametrize(
    "got, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 6, 9]),
        ([2, 4, 6, 8], [6]),
        ([], []),
    ],
)
def test_list_of_numbers_divisible_by_3(got, expected):
    assert list_of_numbers_divisible_by_3(got) == expected


@pytest.mark.parametrize(
    "got, expected",
    [
        (([2, 3, 4], [6, 7, 8]), [12, 21, 32]),
        (([], []), []),
        (([1, 2], []), []),
    ],
)
def test_lists_to_tuple_list(got, expected):
    assert lists_to_tuple_list(*got) == expected
