import pytest

from algorithms.graphs.dijkstra import find_shortest_path


def test_standard_graph():

    graph = {
        "A": {"B": 3, "C": 3},
        "B": {"A": 3, "D": 3.5, "E": 2.8},
        "C": {"A": 3, "E": 2.8, "F": 3.5},
        "D": {"B": 3.5, "E": 3.1, "G": 10},
        "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
        "F": {"G": 2.5, "C": 3.5},
        "G": {"F": 2.5, "E": 7, "D": 10}
    }

    distances, paths = find_shortest_path("B", graph)

    expected_distances = {
        "A": 3,
        "B": 0,
        "C": 5.6,
        "D": 3.5,
        "E": 2.8,
        "F": 9.1,
        "G": 9.8
    }

    expected_paths = {
        "A": ["B", "A"],
        "B": ["B"],
        "C": ["B", "E", "C"],
        "D": ["B", "D"],
        "E": ["B", "E"],
        "F": ["B", "E", "C", "F"],
        "G": ["B", "E", "G"]
    }

    assert distances == pytest.approx(expected_distances)
    assert paths == expected_paths


def test_single_vertex_graph():

    graph = {"A": {}}

    distances, paths = find_shortest_path("A", graph)

    assert distances == {"A": 0}
    assert paths == {"A": ["A"]}


def test_disconnected_graph():

    graph = {
        "A": {"B": 2},
        "B": {"A": 2},
        "C": {"D": 3},
        "D": {"C": 3}
    }

    distances, paths = find_shortest_path("A", graph)

    assert distances["A"] == 0
    assert distances["B"] == 2
    assert distances["C"] == float("inf")
    assert distances["D"] == float("inf")

    assert paths == {
        "A": ["A"],
        "B": ["A", "B"]
    }


def test_directed_graph():

    graph = {
        "A": {"B": 2},
        "B": {"C": 3},
        "C": {}
    }

    distances, paths = find_shortest_path("A", graph)

    assert distances == {
        "A": 0,
        "B": 2,
        "C": 5
    }

    assert paths == {
        "A": ["A"],
        "B": ["A", "B"],
        "C": ["A", "B", "C"]
    }


def test_zero_weight_edges():

    graph = {
        "A": {"B": 0},
        "B": {"C": 0},
        "C": {"D": 2},
        "D": {}
    }

    distances, paths = find_shortest_path("A", graph)

    assert distances == {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 2
    }

    assert paths == {
        "A": ["A"],
        "B": ["A", "B"],
        "C": ["A", "B", "C"],
        "D": ["A", "B", "C", "D"]
    }


def test_cycle():

    graph = {
        "A": {"B": 1},
        "B": {"C": 2},
        "C": {"A": 1, "D": 3},
        "D": {}
    }

    distances, paths = find_shortest_path("A", graph)

    assert distances == {
        "A": 0,
        "B": 1,
        "C": 3,
        "D": 6
    }

    assert paths["D"] == ["A", "B", "C", "D"]


def test_mixed_vertex_types_with_equal_distances():

    # Vertices do not need to be mutually comparable.
    graph = {
        "A": {1: 2, ("B",): 2},
        1: {},
        ("B",): {}
    }

    distances, paths = find_shortest_path("A", graph)

    assert distances[1] == 2
    assert distances[("B",)] == 2

    assert paths[1] == ["A", 1]
    assert paths[("B",)] == ["A", ("B",)]


def test_source_vertex_not_in_graph():

    graph = {
        "A": {"B": 1},
        "B": {}
    }

    with pytest.raises(ValueError):
        find_shortest_path("C", graph)


def test_invalid_graph_type():

    with pytest.raises(TypeError):
        find_shortest_path("A", ["A", "B"])


def test_invalid_neighbours_type():

    graph = {
        "A": ["B"],
        "B": {}
    }

    with pytest.raises(TypeError):
        find_shortest_path("A", graph)


def test_neighbour_not_in_graph():

    graph = {
        "A": {"B": 1}
    }

    with pytest.raises(ValueError):
        find_shortest_path("A", graph)


@pytest.mark.parametrize(
    "weight, exception",
    [
        (-1, ValueError),
        (-0.5, ValueError),
        (float("nan"), ValueError),
        (float("inf"), ValueError),
        (float("-inf"), ValueError),
        ("2", TypeError),
        (True, TypeError),
        (None, TypeError)
    ]
)
def test_invalid_edge_weights(weight, exception):

    graph = {
        "A": {"B": weight},
        "B": {}
    }

    with pytest.raises(exception):
        find_shortest_path("A", graph)
