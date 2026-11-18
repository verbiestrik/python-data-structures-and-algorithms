"""
Dijkstra's Shortest Path Algorithm
===================================

Problem
-------
Find the shortest distances and paths from a given source vertex to every
other vertex in a weighted graph.

The graph is represented as an adjacency dictionary, where each vertex maps
to a dictionary containing its neighbours and the corresponding edge weights.

The algorithm assumes non-negative edge weights, which guarantees that no 
reachable negative-weight cycles exist.

Example:
    graph = {
        "A": {"B": 3, "C": 5},
        "B": {"A": 3, "C": 2},
        "C": {"A": 5, "B": 2}
    }

Approach
--------
Dijkstra's algorithm uses a min-heap to process vertices in ascending order
of their currently known shortest distance from the source.

1. Initialise the distance to the source as zero and all other distances
   as infinity.
2. Insert the source into a min-heap.
3. Repeatedly extract the vertex with the smallest tentaive distance
   to the source.
4. If travelling through the current vertex produces a shorter distance 
   to a neighbour, update that neighbour's distance and predecessor, 
   and add it to the heap (so-called edge relaxation).
5. Ignore outdated heap entries. Since heapq does not support efficient
   decrease-key operations, improved distances are inserted as new entries.
6. Reconstruct the shortest paths using the predecessor dictionary.

A counter is included in heap entries to ensure that vertices themselves
never need to be compared. This allows arbitrary hashable vertex types,
including strings, integers and tuples.

The algorithm supports directed and undirected graphs, but requires all
edge weights to be non-negative.

Complexity
----------
Let V be the number of vertices and E the number of edges (counting
adjacency entries).

Shortest-distance computation:
    Time:  O((V + E) log V)
    Space: O(V + E) auxiliary space, including the heap.

Path reconstruction:
    Time:  O(V²) in the worst case.
    Space: O(V²) in the worst case for the returned paths.

The quadratic path-reconstruction cost arises because the complete path
to every reachable vertex is explicitly stored.

Python alternatives
-------------------
- heapq: Provides an efficient min-heap implementation. Using min() to
  repeatedly find the smallest distance would be simpler but less efficient.
- dict: Provides efficient distance and predecessor lookups.
- collections.deque with BFS: A better alternative for unweighted graphs.
- queue.PriorityQueue: Another priority queue implementation.

Returns
-------
distances : dict
    Shortest distance from the source to every vertex. Unreachable vertices
    have a distance of infinity.

paths : dict
    Shortest path from the source to every reachable vertex, represented
    as a list of vertices in source-to-destination order. Unreachable
    vertices are omitted. The source has a path consisting of itself.
"""

from collections.abc import Mapping
from heapq import heappop, heappush
from itertools import count
from math import inf, isfinite
from numbers import Real
from typing import Hashable


def find_shortest_path(
    src_vertex: Hashable,
    graph: Mapping[Hashable, Mapping[Hashable, Real]]
) -> tuple[dict[Hashable, Real], dict[Hashable, list[Hashable]]]:

    if not isinstance(graph, Mapping):
        raise TypeError("Graph must be a mapping.")

    if src_vertex not in graph:
        raise ValueError("Source vertex is not present in the graph.")

    # Validate the graph before running the algorithm.
    for vertex, neighbours in graph.items():

        if not isinstance(neighbours, Mapping):
            raise TypeError(
                f"Neighbours of vertex {vertex!r} must be a mapping."
            )

        for neighbour, weight in neighbours.items():

            if neighbour not in graph:
                raise ValueError(
                    f"Neighbour {neighbour!r} is not present in the graph."
                )

            if isinstance(weight, bool) or not isinstance(weight, Real):
                raise TypeError("Edge weights must be real numbers.")

            # Dijkstra's algorithm does not support negative edge weights.
            if weight < 0:
                raise ValueError("Edge weights must be non-negative.")

            # Reject NaN and infinite floating-point weights.
            # Very large integers are finite, even if math.isfinite()
            # cannot convert them to a float.
            try:
                if not isfinite(weight):
                    raise ValueError("Edge weights must be finite.")
            except OverflowError:
                pass

    # Initialise distances.
    distances = {vertex: inf for vertex in graph}
    distances[src_vertex] = 0

    # Store the predecessor of each vertex in its shortest path.
    predecessors = {}

    # A counter prevents comparisons between vertices when distances tie.
    sequence = count()

    # Each heap entry contains (distance, sequence number, vertex).
    dist_heap = [(0, next(sequence), src_vertex)]

    while dist_heap:

        current_distance, _, current_vertex = heappop(dist_heap)

        # Ignore outdated entries resulting from previously improved
        # distances.
        if current_distance != distances[current_vertex]:
            continue

        for neighbour, weight in graph[current_vertex].items():

            new_distance = current_distance + weight

            # Relax the edge if a shorter path has been found.
            if new_distance < distances[neighbour]:

                distances[neighbour] = new_distance
                predecessors[neighbour] = current_vertex

                heappush(
                    dist_heap,
                    (new_distance, next(sequence), neighbour)
                )

    # Reconstruct paths using the predecessor dictionary.
    paths = {src_vertex: [src_vertex]}

    for vertex in graph:

        # Skip the source and unreachable vertices.
        if vertex == src_vertex or distances[vertex] == inf:
            continue

        path = []
        current_vertex = vertex

        # Follow predecessors until reaching the source.
        while current_vertex != src_vertex:
            path.append(current_vertex)
            current_vertex = predecessors[current_vertex]

        path.append(src_vertex)

        # Reverse to obtain source-to-destination order.
        paths[vertex] = path[::-1]

    return distances, paths
