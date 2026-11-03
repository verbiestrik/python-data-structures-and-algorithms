from algorithms.strings.first_non_repeating_char import first_non_repeating_char


def test_multiple_repeated_characters():
    assert first_non_repeating_char("Daddalena") == "l"


def test_all_characters_unique():
    assert first_non_repeating_char("Python") == "p"


def test_no_non_repeating_character():
    assert first_non_repeating_char("aabbcc") is None


def test_case_insensitivity():
    assert first_non_repeating_char("AaBbCcDdE") == "e"


def test_leading_and_trailing_whitespace():
    assert first_non_repeating_char("  aabbc  ") == "c"


def test_empty_string():
    assert first_non_repeating_char("") is None


def test_single_character():
    assert first_non_repeating_char("A") == "a"


def test_whitespace_only():
    assert first_non_repeating_char("   ") is None
