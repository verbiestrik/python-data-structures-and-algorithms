from collections.abc import Iterable

def find_duplicates(numbers: Iterable[int | float]) -> set[int | float]:
    """Return all numbers that occur more than once."""

    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return duplicates
