import pytest

from algorithms.data_structures.array_stack import ArrayStack, Empty


def test_initialisation():
    stack = ArrayStack()

    assert len(stack) == 0
    assert stack.is_empty()


def test_push_single_element():
    stack = ArrayStack()
    stack.push(10)

    assert len(stack) == 1
    assert not stack.is_empty()
    assert stack.top() == 10


def test_push_multiple_elements():
    stack = ArrayStack()

    for value in (1, 2, 3, 4):
        stack.push(value)

    assert len(stack) == 4
    assert stack.top() == 4


def test_top_does_not_remove_element():
    stack = ArrayStack()
    stack.push(10)

    assert stack.top() == 10
    assert len(stack) == 1
    assert not stack.is_empty()


def test_pop_returns_last_element():
    stack = ArrayStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_stack_follows_lifo_order():
    stack = ArrayStack()

    for value in ("first", "second", "third"):
        stack.push(value)

    assert stack.pop() == "third"
    assert stack.pop() == "second"
    assert stack.pop() == "first"
    assert stack.is_empty()


def test_length_after_push_and_pop():
    stack = ArrayStack()

    stack.push(1)
    stack.push(2)

    assert len(stack) == 2

    stack.pop()

    assert len(stack) == 1

    stack.pop()

    assert len(stack) == 0
    assert stack.is_empty()


def test_push_none():
    stack = ArrayStack()
    stack.push(None)

    assert len(stack) == 1
    assert stack.top() is None
    assert stack.pop() is None
    assert stack.is_empty()


def test_push_different_types():
    stack = ArrayStack()

    stack.push(10)
    stack.push("hello")
    stack.push([1, 2, 3])

    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 10


def test_stack_can_be_reused_after_becoming_empty():
    stack = ArrayStack()

    stack.push(1)
    stack.pop()

    assert stack.is_empty()

    stack.push(2)

    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.is_empty()


def test_top_on_empty_stack_raises_empty():
    stack = ArrayStack()

    with pytest.raises(Empty, match="No top element; stack is empty!"):
        stack.top()


def test_pop_on_empty_stack_raises_empty():
    stack = ArrayStack()

    with pytest.raises(Empty, match="No top element; stack is empty!"):
        stack.pop()


def test_pop_until_empty_then_raises_empty():
    stack = ArrayStack()

    stack.push(1)
    stack.push(2)

    assert stack.pop() == 2
    assert stack.pop() == 1

    with pytest.raises(Empty):
        stack.pop()
