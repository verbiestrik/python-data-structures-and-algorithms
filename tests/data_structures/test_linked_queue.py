import pytest

from data_structures.queues.linked_queue import LinkedQueue, Empty


def test_new_queue_is_empty():
    queue = LinkedQueue()

    assert len(queue) == 0
    assert queue.is_empty()


def test_enqueue_and_dequeue():
    queue = LinkedQueue()

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
    queue = LinkedQueue()

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.first() == 10
    assert queue.first() == 10
    assert len(queue) == 2

    assert queue.dequeue() == 10
    assert queue.first() == 20


def test_dequeue_from_empty_queue_raises_exception():
    queue = LinkedQueue()

    with pytest.raises(Empty):
        queue.dequeue()


def test_first_on_empty_queue_raises_exception():
    queue = LinkedQueue()

    with pytest.raises(Empty):
        queue.first()


def test_dequeue_last_element_resets_queue():
    queue = LinkedQueue()

    queue.enqueue(10)

    assert queue.dequeue() == 10
    assert queue.is_empty()
    assert len(queue) == 0


def test_enqueue_after_queue_becomes_empty():
    queue = LinkedQueue()

    queue.enqueue(10)
    assert queue.dequeue() == 10

    # The queue must correctly restore both head and tail references.
    queue.enqueue(20)
    queue.enqueue(30)

    assert len(queue) == 2
    assert queue.first() == 20
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30

    assert queue.is_empty()


def test_interleaved_enqueue_and_dequeue_operations():
    queue = LinkedQueue()

    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.dequeue() == 1

    queue.enqueue(3)
    queue.enqueue(4)

    assert queue.dequeue() == 2
    assert queue.dequeue() == 3

    queue.enqueue(5)

    assert queue.dequeue() == 4
    assert queue.dequeue() == 5

    assert queue.is_empty()


def test_queue_accepts_none_as_a_valid_element():
    queue = LinkedQueue()

    queue.enqueue(None)

    assert len(queue) == 1
    assert not queue.is_empty()
    assert queue.first() is None
    assert queue.dequeue() is None
    assert queue.is_empty()


def test_queue_accepts_different_element_types():
    queue = LinkedQueue()

    elements = [10, "hello", None, 3.14, False]

    for element in elements:
        queue.enqueue(element)

    for element in elements:
        assert queue.dequeue() == element

    assert queue.is_empty()


def test_large_number_of_elements():
    queue = LinkedQueue()

    for value in range(1000):
        queue.enqueue(value)

    assert len(queue) == 1000

    for value in range(1000):
        assert queue.dequeue() == value

    assert queue.is_empty()


def test_multiple_queues_are_independent():
    queue_a = LinkedQueue()
    queue_b = LinkedQueue()

    queue_a.enqueue(10)
    queue_b.enqueue(20)

    assert queue_a.first() == 10
    assert queue_b.first() == 20

    queue_a.enqueue(30)

    assert queue_a.dequeue() == 10
    assert queue_a.dequeue() == 30
    assert queue_b.dequeue() == 20

    assert queue_a.is_empty()
    assert queue_b.is_empty()
