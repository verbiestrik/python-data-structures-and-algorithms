import pytest

from data_structures.stacks.linked_stack import LinkedStack, Empty


def test_new_stack_is_empty():
    stack = LinkedStack()

    assert len(stack) == 0
    assert stack.is_empty()


def test_push_and_pop():
    stack = LinkedStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert len(stack) == 3
    assert not stack.is_empty()

    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10

    assert len(stack) == 0
    assert stack.is_empty()


def test_top_returns_top_element_without_removing_it():
    stack = LinkedStack()

    stack.push(10)
    stack.push(20)

    assert stack.top() == 20
    assert stack.top() == 20
    assert len(stack) == 2

    assert stack.pop() == 20
    assert stack.top() == 10


def test_pop_from_empty_stack_raises_exception():
    stack = LinkedStack()

    with pytest.raises(Empty):
        stack.pop()


def test_top_on_empty_stack_raises_exception():
    stack = LinkedStack()

    with pytest.raises(Empty):
        stack.top()


def test_stack_can_be_reused_after_becoming_empty():
    stack = LinkedStack()

    stack.push(10)
    assert stack.pop() == 10
    assert stack.is_empty()

    stack.push(20)
    stack.push(30)

    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.is_empty()


def test_interleaved_push_and_pop_operations():
    stack = LinkedStack()

    stack.push(1)
    stack.push(2)

    assert stack.pop() == 2

    stack.push(3)
    stack.push(4)

    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 1

    assert stack.is_empty()


def test_stack_accepts_none_as_a_valid_element():
    stack = LinkedStack()

    stack.push(None)

    assert len(stack) == 1
    assert not stack.is_empty()
    assert stack.top() is None
    assert stack.pop() is None
    assert stack.is_empty()


def test_stack_accepts_different_element_types():
    stack = LinkedStack()

    elements = [10, "hello", None, 3.14, False]

    for element in elements:
        stack.push(element)

    for element in reversed(elements):
        assert stack.pop() == element

    assert stack.is_empty()


def test_large_number_of_elements():
    stack = LinkedStack()

    for value in range(1000):
        stack.push(value)

    assert len(stack) == 1000

    for value in reversed(range(1000)):
        assert stack.pop() == value

    assert stack.is_empty()


def test_pop_returns_removed_element():
    stack = LinkedStack()

    stack.push("first")
    stack.push("second")

    removed_element = stack.pop()

    assert removed_element == "second"
    assert stack.top() == "first"
    assert len(stack) == 1


def test_multiple_stacks_are_independent():
    stack_a = LinkedStack()
    stack_b = LinkedStack()

    stack_a.push(10)
    stack_b.push(20)

    assert stack_a.top() == 10
    assert stack_b.top() == 20

    stack_a.push(30)

    assert stack_a.top() == 30
    assert stack_b.top() == 20

    assert stack_a.pop() == 30
    assert stack_b.pop() == 20
