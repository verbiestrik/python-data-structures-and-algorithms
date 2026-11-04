"""
Problem: Singly Linked List and Reversal

Implement a singly linked list with the following operations:
- Initialize an empty linked list.
- Add and remove the first node.
- Add and remove the last node.
- Add and remove a node before a given node.
- Add and remove a node after a given node.
- Reverse the entire linked list.

Approach:
Each node contains:
- _value: The stored element.
- _next: A reference to the next node.
- _owner_token: A unique identity marker identifying the
  linked list to which the node belongs.

The Node class is nested inside SinglyLinkedList.

The linked list maintains:
- _head: Reference to the first node.
- _tail: Reference to the last node.
- _list_token: A unique identity marker created during
  initialization. All nodes belonging to this list share
  this marker.

Node membership is validated by comparing _owner_token
with _list_token using the identity operator (is).

When a node is removed, its _owner_token is set to None,
preventing its subsequent use in linked-list operations.

Operations:
- add_first(value): Insert a node with certain value at the beginning.
- remove_first(): Remove and return the first value.
- add_last(value): Insert a node with certain value at the end.
- remove_last(): Remove and return the last value.
- add_before(node, value): Insert a node with certain value before a given node.
- remove_before(node): Remove and return node with certain value before a given node.
- add_after(node, value): Insert a node with a certain value after a given node.
- remove_after(node): Remove and return node with certain value following a given node.

Complexity Analysis:

Let n be the number of nodes.

| Operation       | Time Complexity |
|-----------------|-----------------|
| Initialization  | O(1)            |
| add_first       | O(1)            |
| remove_first    | O(1)            |
| add_last        | O(1)            |
| remove_last     | O(n)            |
| add_before      | O(n)            |
| remove_before   | O(n)            |
| add_after       | O(1)            |
| remove_after    | O(1)            |
| reverse         | O(n)            |

All operations require O(1) auxiliary space.
The linked list itself requires O(n) space.

Python Alternative:
Python's built-in list provides reverse(), which reverses
a list in place. However, Python does not provide a built-in
singly linked list with these operations.
"""


class SinglyLinkedList:

    class _Node:
        def __init__(self, value, owner_token):
            self._value = value
            self._next = None
            self._owner_token = owner_token

    def __init__(self):
        self._head = None
        self._tail = None

        # Unique identity marker for this linked list.
        self._list_token = object()

    def __iter__(self):
        current = self._head

        while current is not None:
            yield current._value
            current = current._next

    def _validate_node(self, node):
        """Check whether a node belongs to this linked list."""

        if (not isinstance(node, self._Node)
                or node._owner_token is not self._list_token):
            raise ValueError("Node does not belong to this linked list.")

    def add_first(self, value):
        new_node = self._Node(value, self._list_token)
        new_node._next = self._head
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

        return new_node

    def remove_first(self):
        if self._head is None:
            raise IndexError("Cannot remove from an empty linked list.")

        removed = self._head
        self._head = removed._next

        if self._head is None:
            self._tail = None

        removed._next = None
        removed._owner_token = None

        return removed._value

    def add_last(self, value):
        new_node = self._Node(value, self._list_token)

        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node

        return new_node

    def remove_last(self):
        if self._head is None:
            raise IndexError("Cannot remove from an empty linked list.")

        previous = None
        current = self._head

        while current._next is not None:
            previous = current
            current = current._next

        if previous is None:
            self._head = None
            self._tail = None
        else:
            previous._next = None
            self._tail = previous

        current._next = None
        current._owner_token = None

        return current._value

    def add_before(self, node, value):
        self._validate_node(node)

        new_node = self._Node(value, self._list_token)

        if node is self._head:
            return self.add_first(value)

        previous = self._head

        while previous._next is not node:
            previous = previous._next

        new_node._next = node
        previous._next = new_node

        return new_node

    def remove_before(self, node):
        self._validate_node(node)

        if node is self._head:
            raise ValueError("There is no node before the given node.")

        before_previous = None
        previous = self._head

        while previous._next is not node:
            before_previous = previous
            previous = previous._next

        if before_previous is None:
            self._head = node
        else:
            before_previous._next = node

        previous._next = None
        previous._owner_token = None

        return previous._value

    def add_after(self, node, value):
        self._validate_node(node)

        new_node = self._Node(value, self._list_token)
        new_node._next = node._next
        node._next = new_node

        if self._tail is node:
            self._tail = new_node

        return new_node

    def remove_after(self, node):
        self._validate_node(node)

        removed = node._next

        if removed is None:
            raise ValueError("There is no node after the given node.")

        node._next = removed._next

        if self._tail is removed:
            self._tail = node

        removed._next = None
        removed._owner_token = None

        return removed._value


def reverse_linked_list(linked_list):
    """Reverse a singly linked list in place."""

    previous = None
    current = linked_list._head
    old_head = linked_list._head

    while current is not None:
        next_node = current._next
        current._next = previous
        previous = current
        current = next_node

    linked_list._head = previous
    linked_list._tail = old_head
