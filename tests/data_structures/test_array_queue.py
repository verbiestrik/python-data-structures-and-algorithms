import pytest

from data_structures.queues.array_queue import ArrayQueue, Empty


def test_new_queue_is_empty():
    queue = ArrayQueue()

    assert len(queue) == 0
    assert queue.is_empty()


def test_enqueue_and_dequeue():
    queue = ArrayQueue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert len(queue) == 3
    assert not queue.is_empty()

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30

    assert len(queue) == 0
    assert queue.is_empty()


def test_first_returns_front_element_without_removing_it():
    queue = ArrayQueue()

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.first() == 10
    assert queue.first() == 10
    assert len(queue) == 2

    assert queue.dequeue() == 10
    assert queue.first() == 20


def test_dequeue_from_empty_queue_raises_exception():
    queue = ArrayQueue()

    with pytest.raises(Empty):
        queue.dequeue()


def test_first_on_empty_queue_raises_exception():
    queue = ArrayQueue()

    with pytest.raises(Empty):
        queue.first()


def test_wraparound_reuses_freed_positions():
    queue = ArrayQueue(initial_capacity=3)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

    # These elements should occupy positions freed at the beginning
    # of the underlying circular array.
    queue.enqueue(4)
    queue.enqueue(5)

    assert len(queue) == 3

    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5

    assert queue.is_empty()


def test_resize_preserves_fifo_order_when_array_is_wrapped():
    queue = ArrayQueue(initial_capacity=4)

    for value in range(1, 5):
        queue.enqueue(value)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

    queue.enqueue(5)
    queue.enqueue(6)

    # The underlying array is now full, with elements stored across
    # both sides of the circular boundary.
    assert len(queue) == 4

    # Enqueuing another element triggers a resize.
    queue.enqueue(7)

    assert len(queue) == 5
    assert queue.first() == 3

    assert [
        queue.dequeue(),
        queue.dequeue(),
        queue.dequeue(),
        queue.dequeue(),
        queue.dequeue(),
    ] == [3, 4, 5, 6, 7]

    assert queue.is_empty()


def test_multiple_resizes_preserve_fifo_order():
    queue = ArrayQueue(initial_capacity=2)

    for value in range(100):
        queue.enqueue(value)

    assert len(queue) == 100

    for value in range(100):
        assert queue.dequeue() == value

    assert queue.is_empty()


def test_queue_accepts_none_as_a_valid_element():
    queue = ArrayQueue()

    queue.enqueue(None)

    assert len(queue) == 1
    assert not queue.is_empty()
    assert queue.first() is None
    assert queue.dequeue() is None
    assert queue.is_empty()


def test_queue_accepts_different_element_types():
    queue = ArrayQueue()

    elements = [10, "hello", None, 3.14, False]

    for element in elements:
        queue.enqueue(element)

    for element in elements:
        assert queue.dequeue() == element

    assert queue.is_empty()


@pytest.mark.parametrize("capacity", [1, 2, 8, 16])
def test_valid_initial_capacity(capacity):
    queue = ArrayQueue(initial_capacity=capacity)

    assert queue.is_empty()
    assert len(queue) == 0


@pytest.mark.parametrize("capacity", [0, -1, -10])
def test_non_positive_initial_capacity_raises_value_error(capacity):
    with pytest.raises(ValueError):
        ArrayQueue(initial_capacity=capacity)


@pytest.mark.parametrize("capacity", [1.5, "8", None, True])
def test_invalid_initial_capacity_type_raises_type_error(capacity):
    with pytest.raises(TypeError):
        ArrayQueue(initial_capacity=capacity)
