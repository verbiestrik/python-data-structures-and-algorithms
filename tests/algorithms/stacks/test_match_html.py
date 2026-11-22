import pytest

from algorithms.parsing.match_html import match_html


def test_empty_string():
    assert match_html("") is True


def test_single_tag():
    assert match_html("<div></div>") is True


def test_nested_tags():
    html = "<html><body><p>Hello</p></body></html>"

    assert match_html(html) is True


def test_multiple_sibling_tags():
    html = "<div></div><p></p><span></span>"

    assert match_html(html) is True


def test_nested_identical_tags():
    html = "<div><div><div></div></div></div>"

    assert match_html(html) is True


def test_text_between_tags():
    html = "<p>Hello world!</p>"

    assert match_html(html) is True


def test_unmatched_opening_tag():
    assert match_html("<div>") is False


def test_unmatched_closing_tag():
    assert match_html("</div>") is False


def test_mismatched_tags():
    assert match_html("<div></p>") is False


def test_incorrect_nesting():
    html = "<div><p></div></p>"

    assert match_html(html) is False


def test_missing_closing_angle_bracket():
    assert match_html("<div></div") is False


def test_missing_opening_tag():
    assert match_html("<div><p></p></div>") is True


def test_empty_tag():
    assert match_html("<></>") is False


def test_multiple_unmatched_opening_tags():
    html = "<div><p><span></span>"

    assert match_html(html) is False


@pytest.mark.parametrize("html_src", [
    None,
    123,
    1.5,
    ["<div></div>"],
    {"html": "<div></div>"},
])
def test_invalid_input_type(html_src):
    with pytest.raises(TypeError):
        match_html(html_src)
