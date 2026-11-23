import pytest

from data_structures.list_implementations.dynamic_array import DynamicArray


def test_initialisation():
    array = DynamicArray()

    assert len(array) == 0


def test_append_single_element():
    array = DynamicArray()
    array.append(10)

    assert len(array) == 1
    assert array[0] == 10


def test_append_multiple_elements_and_resize():
    array = DynamicArray()

    for i in range(100):
        array.append(i)

    assert len(array) == 100
    assert [array[i] for i in range(len(array))] == list(range(100))


def test_append_preserves_object_references():
    array = DynamicArray()
    values = [[1], [2], [3]]

    for value in values:
        array.append(value)

    assert array[0] is values[0]
    assert array[1] is values[1]
    assert array[2] is values[2]


def test_positive_and_negative_indexing():
    array = DynamicArray()

    for value in ("first", "second", "third"):
        array.append(value)

    assert array[0] == "first"
    assert array[2] == "third"
    assert array[-1] == "third"
    assert array[-2] == "second"
    assert array[-3] == "first"


def test_assignment():
    array = DynamicArray()
    array.append(10)
    array.append(20)

    array[0] = 100
    array[-1] = 200

    assert array[0] == 100
    assert array[1] == 200


@pytest.mark.parametrize("invalid_index", [1.5, "0", None])
def test_invalid_index_type(invalid_index):
    array = DynamicArray()
    array.append(10)

    with pytest.raises(TypeError):
        _ = array[invalid_index]

    with pytest.raises(TypeError):
        array.insert(invalid_index, 20)


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


# --------------------------------------------------
# Insert tests
# --------------------------------------------------

def test_insert_at_beginning_middle_and_end():
    array = DynamicArray()
    array.append(1)
    array.append(3)

    array.insert(0, 0)
    array.insert(2, 2)
    array.insert(len(array), 4)

    assert [array[i] for i in range(len(array))] == [0, 1, 2, 3, 4]


def test_insert_into_empty_array():
    array = DynamicArray()
    array.insert(0, "value")

    assert len(array) == 1
    assert array[0] == "value"


def test_insert_triggers_resize_and_preserves_elements():
    array = DynamicArray()

    for value in range(4):
        array.append(value)

    array.insert(2, "new")

    assert [array[i] for i in range(len(array))] == [0, 1, "new", 2, 3]


def test_insert_with_negative_indices():
    array = DynamicArray()

    for value in (1, 2, 3):
        array.append(value)

    array.insert(-1, "before last")
    array.insert(-100, "at beginning")

    assert [array[i] for i in range(len(array))] == [
        "at beginning", 1, 2, "before last", 3
    ]


def test_insert_indices_beyond_bounds_are_clamped():
    array = DynamicArray()

    array.insert(100, "end")
    array.insert(-100, "beginning")

    assert [array[i] for i in range(len(array))] == [
        "beginning", "end"
    ]


# --------------------------------------------------
# Remove tests
# --------------------------------------------------

def test_remove_first_occurrence_only():
    array = DynamicArray()

    for value in (1, 2, 2, 3):
        array.append(value)

    array.remove(2)

    assert [array[i] for i in range(len(array))] == [1, 2, 3]
    assert len(array) == 3


def test_remove_from_beginning_middle_and_end():
    array = DynamicArray()

    for value in (1, 2, 3, 4):
        array.append(value)

    array.remove(1)
    array.remove(3)
    array.remove(4)

    assert len(array) == 1
    assert array[0] == 2


def test_remove_last_element():
    array = DynamicArray()
    array.append("only element")

    array.remove("only element")

    assert len(array) == 0

    with pytest.raises(IndexError):
        _ = array[0]


def test_remove_missing_value_raises_value_error():
    array = DynamicArray()
    array.append(1)

    with pytest.raises(ValueError):
        array.remove(2)


def test_remove_from_empty_array_raises_value_error():
    array = DynamicArray()

    with pytest.raises(ValueError):
        array.remove("missing")


def test_remove_uses_equality_not_identity():
    array = DynamicArray()
    stored_value = [1, 2]

    array.append(stored_value)
    array.remove([1, 2])

    assert len(array) == 0
