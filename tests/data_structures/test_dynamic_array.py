import pytest

from data_structures.dynamic_array import DynamicArray


def test_initialisation():
    array = DynamicArray()

    assert len(array) == 0


def test_append_single_element():
    array = DynamicArray()
    array.append(10)

    assert len(array) == 1
    assert array[0] == 10


def test_append_multiple_elements():
    array = DynamicArray()

    for i in range(10):
        array.append(i)

    assert len(array) == 10

    for i in range(10):
        assert array[i] == i


def test_append_triggers_resizing():
    array = DynamicArray()

    # Appending more elements than the initial capacity forces resizing.
    for i in range(100):
        array.append(i)

    assert len(array) == 100

    for i in range(100):
        assert array[i] == i


def test_append_preserves_existing_references():
    array = DynamicArray()
    values = [[1], [2], [3]]

    for value in values:
        array.append(value)

    assert array[0] is values[0]
    assert array[1] is values[1]
    assert array[2] is values[2]


def test_positive_indexing():
    array = DynamicArray()

    array.append("first")
    array.append("second")
    array.append("third")

    assert array[0] == "first"
    assert array[1] == "second"
    assert array[2] == "third"


def test_negative_indexing():
    array = DynamicArray()

    array.append("first")
    array.append("second")
    array.append("third")

    assert array[-1] == "third"
    assert array[-2] == "second"
    assert array[-3] == "first"


def test_assignment():
    array = DynamicArray()

    array.append(10)
    array.append(20)

    array[0] = 100
    array[1] = 200

    assert array[0] == 100
    assert array[1] == 200


def test_assignment_with_negative_index():
    array = DynamicArray()

    array.append(10)
    array.append(20)

    array[-1] = 200

    assert array[1] == 200


def test_index_out_of_range():
    array = DynamicArray()
    array.append(10)

    with pytest.raises(IndexError):
        _ = array[1]

    with pytest.raises(IndexError):
        _ = array[-2]


def test_indexing_empty_array():
    array = DynamicArray()

    with pytest.raises(IndexError):
        _ = array[0]

    with pytest.raises(IndexError):
        _ = array[-1]


def test_assignment_out_of_range():
    array = DynamicArray()
    array.append(10)

    with pytest.raises(IndexError):
        array[1] = 20


@pytest.mark.parametrize("invalid_index", [1.5, "0", None])
def test_invalid_index_type(invalid_index):
    array = DynamicArray()
    array.append(10)

    with pytest.raises(TypeError):
        _ = array[invalid_index]
