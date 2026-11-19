"""
English Ruler
=============

Problem
-------
Draw an English ruler with a specified number of inches and maximum tick
length.

Each inch is marked with a major tick, whose length is equal to the specified
maximum tick length. The major ticks are labelled with their corresponding
inch numbers.

Between consecutive major ticks, progressively shorter ticks are drawn
according to a recursive pattern.

For example, with 2 inches and a maximum tick length of 3:

    ***0
    *
    **
    *
    ***1
    *
    **
    *
    ***2

Approach
--------
Use recursion to generate the intermediate tick marks.

The draw_interval() function follows a recursive pattern:

1. Recursively draw an interval with one shorter tick length.
2. Draw the central tick.
3. Recursively draw another interval with one shorter tick length.

This produces a symmetric sequence of tick lengths.

The draw_ruler() function first draws the initial major tick and then
repeatedly draws an intermediate interval followed by another major tick.

Complexity
----------
Let n be the number of inches and L be the maximum tick length.

Each interval produces 2^(L-1) - 1 intermediate ticks.

Time complexity:
    O(n * L * 2^L), including the time required to print the tick characters.

Space complexity:
    O(L) auxiliary space for the recursive call stack.

The algorithm prints the ruler directly and does not store the generated
output in memory.

Python alternatives
-------------------
- range(): Iterates over the inches without requiring an explicit counter.
- String multiplication (*): Constructs each tick using a concise built-in
  operation.
- print(): Displays each tick directly.
- An iterative implementation using a stack could replace recursion, but
  recursion expresses the symmetric structure of the ruler more naturally.

Input validation
----------------
- number_of_inches must be a non-negative integer.
- max_tick_length must be a positive integer.
- Boolean values are explicitly rejected, even though bool is a subclass
  of int in Python.
"""


def draw_line(tick_length: int, label: str = "") -> None:
    """Print a tick mark, optionally followed by a label."""

    if isinstance(tick_length, bool) or not isinstance(tick_length, int):
        raise TypeError("Tick length must be an integer.")

    if tick_length < 0:
        raise ValueError("Tick length must be non-negative.")

    if not isinstance(label, str):
        raise TypeError("Label must be a string.")

    print("*" * tick_length + label)


def _draw_interval(center_length: int) -> None:
    """Recursively print the tick marks of an interval."""

    if center_length > 0:

        _draw_interval(center_length - 1)

        draw_line(center_length)

        _draw_interval(center_length - 1)


def draw_interval(center_length: int) -> None:
    """Print an interval of ticks with the specified central tick length."""

    if isinstance(center_length, bool) or not isinstance(center_length, int):
        raise TypeError("Center length must be an integer.")

    if center_length < 0:
        raise ValueError("Center length must be non-negative.")

    _draw_interval(center_length)


def draw_ruler(number_of_inches: int, max_tick_length: int) -> None:
    """Print an English ruler with the specified dimensions."""

    if isinstance(number_of_inches, bool) or not isinstance(number_of_inches, int):
        raise TypeError("Number of inches must be an integer.")

    if number_of_inches < 0:
        raise ValueError("Number of inches must be non-negative.")

    if isinstance(max_tick_length, bool) or not isinstance(max_tick_length, int):
        raise TypeError("Maximum tick length must be an integer.")

    if max_tick_length <= 0:
        raise ValueError("Maximum tick length must be positive.")

    # Draw the initial major tick.
    draw_line(max_tick_length, "0")

    # Draw the intermediate ticks and subsequent major ticks.
    for inch in range(1, number_of_inches + 1):

        draw_interval(max_tick_length - 1)

        draw_line(max_tick_length, str(inch))
