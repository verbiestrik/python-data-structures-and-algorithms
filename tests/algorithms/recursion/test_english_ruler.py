import pytest

from algorithms.recursion.english_ruler import (
    draw_line,
    draw_interval,
    draw_ruler
)


def test_standard_ruler(capsys):

    draw_ruler(2, 3)

    expected = (
        "***0\n"
        "*\n"
        "**\n"
        "*\n"
        "***1\n"
        "*\n"
        "**\n"
        "*\n"
        "***2\n"
    )

    assert capsys.readouterr().out == expected


def test_single_interval(capsys):

    draw_ruler(1, 2)

    expected = (
        "**0\n"
        "*\n"
        "**1\n"
    )

    assert capsys.readouterr().out == expected


def test_zero_inches(capsys):

    draw_ruler(0, 3)

    assert capsys.readouterr().out == "***0\n"


def test_minimum_tick_length(capsys):

    draw_ruler(2, 1)

    expected = (
        "*0\n"
        "*1\n"
        "*2\n"
    )

    assert capsys.readouterr().out == expected


def test_draw_interval(capsys):

    draw_interval(2)

    expected = (
        "*\n"
        "**\n"
        "*\n"
    )

    assert capsys.readouterr().out == expected


def test_zero_length_interval(capsys):

    draw_interval(0)

    assert capsys.readouterr().out == ""


def test_draw_line(capsys):

    draw_line(4, "10")

    assert capsys.readouterr().out == "****10\n"


@pytest.mark.parametrize(
    "number_of_inches, max_tick_length, exception",
    [
        (-1, 3, ValueError),
        (2, 0, ValueError),
        (2, -1, ValueError),
        (1.5, 3, TypeError),
        (2, 2.5, TypeError),
        ("2", 3, TypeError),
        (2, "3", TypeError),
        (True, 3, TypeError),
        (2, False, TypeError)
    ]
)
def test_invalid_ruler_arguments(
    number_of_inches,
    max_tick_length,
    exception
):

    with pytest.raises(exception):
        draw_ruler(number_of_inches, max_tick_length)


@pytest.mark.parametrize(
    "center_length, exception",
    [
        (-1, ValueError),
        (1.5, TypeError),
        ("2", TypeError),
        (True, TypeError)
    ]
)
def test_invalid_interval_arguments(center_length, exception):

    with pytest.raises(exception):
        draw_interval(center_length)


@pytest.mark.parametrize(
    "tick_length, label, exception",
    [
        (-1, "", ValueError),
        (1.5, "", TypeError),
        ("2", "", TypeError),
        (True, "", TypeError),
        (2, 123, TypeError)
    ]
)
def test_invalid_line_arguments(tick_length, label, exception):

    with pytest.raises(exception):
        draw_line(tick_length, label)
