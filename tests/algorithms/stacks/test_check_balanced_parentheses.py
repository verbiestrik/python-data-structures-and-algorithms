from algorithms.stacks.check_balanced_parentheses import check_balanced_parentheses


def test_correctly_nested_parentheses():
    assert check_balanced_parentheses("[{({{}})}]") is True


def test_multiple_independent_parentheses():
    assert check_balanced_parentheses("(){}[]") is True


def test_unbalanced_opening_parenthesis():
    assert check_balanced_parentheses("(((") is False


def test_unbalanced_closing_parenthesis():
    assert check_balanced_parentheses(")))") is False


def test_mismatched_parentheses():
    assert check_balanced_parentheses("([)]") is False


def test_empty_sequence():
    assert check_balanced_parentheses("") is True


def test_mathematical_expression():
    assert check_balanced_parentheses("(a + b) * [c - {d / e}]") is True


def test_unbalanced_mathematical_expression():
    assert check_balanced_parentheses("(a + b]") is False


def test_parentheses_with_no_opening():
    assert check_balanced_parentheses("a + b)") is False
