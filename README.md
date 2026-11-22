# Python Algorithms & Data Structures

A collection of Python implementations of fundamental algorithms and problem-solving techniques, developed as part of my interest in algorithms, data structures, and complexity analysis.

The project focuses on algorithmic thinking, efficient implementations, code quality, and software testing.

## Development approach

The algorithms in this repository were implemented while reading the book Data Structures and Algorithms in Python by Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser and many of the implementations are clearly influenced by the book. The algorithms were initially drafted independently by me, based on my understanding of the underlying problems, algorithmic principles, and data structures in Python.

I subsequently used ChatGPT as a programming assistant to review and improve the implementations. This collaboration focused on:
- **Algorithm optimisation:** Improving time and space efficiency where possible.
- **Code quality:** Improving readability, structure, naming conventions, and documentation.
- **Error handling:** Introducing input validation and appropriate exceptions.
- **Testing:** Developing separate pytest test files covering normal cases, edge cases, and invalid inputs.
- **Complexity analysis:** Documenting the theoretical time and auxiliary space complexity of each implementation.

Importantly, I reviewed and verified the resulting implementations to ensure that I understood the algorithms, their underlying logic, and the design decisions involved. The goal was not simply to obtain working solutions, but to use the review process as an opportunity to deepen my understanding of (data structures in) Python and algorithmic problem-solving.

## Repository structure

The repository is organised by algorithm category and data structure, with implementation files separated from their corresponding tests.

```text
python-data-structures-and-algorithms/
│
├── algorithms/
│   ├── arrays/
│   │   ├── common_elements.py
│   │   ├── find_duplicates.py
│   │   ├── find_most_frequent_element.py
│   │   ├── kth_largest.py
│   │   ├── maximum_subarray.py
│   │   ├── merge_two_sorted_lists.py
│   │   ├── rotate_list.py
│   │   └── two_sum.py
│   │
│   ├── graphs/
│   │   └── dijkstra.py
│   │
│   ├── heaps/
│   │   ├── find_k_most_frequent_elements.py
│   │   └── find_k_most_frequent_strings.py
│   │
│   ├── matrices/
│   │   └── sum_and_transpose.py
│   │
│   ├── number_systems/
│   │   └── base_conversion.py
│   │
│   ├── numbers/
│   │   └── find_primes.py
│   │
│   ├── recursion/
│   │   ├── all_permutations.py
│   │   ├── disk_usage.py
│   │   ├── english_ruler.py
│   │   └── summation_puzzle.py
│   │
│   ├── sequences/
│   │   ├── binary_search.py
│   │   └── moving_average.py
│   │
│   ├── stacks/
│   │   ├── check_balanced_parentheses.py
│   │   └── match_html.py
│   │
│   └── strings/
│       ├── check_palindrome.py
│       ├── find_most_frequent_string.py
│       ├── first_non_repeating_char.py
│       ├── group_anagrams.py
│       ├── longest_substring.py
│       ├── longest_word.py
│       ├── reverse_string.py
│       └── valid_anagram.py
│
├── data_structures/
│   ├── array_stack.py
│   ├── dynamic_array.py
│   └── singly_linked_list.py
│
├── tests/
│   ├── algorithms/
│   │   ├── arrays/
│   │   │   ├── test_common_elements.py
│   │   │   ├── test_find_duplicates.py
│   │   │   ├── test_find_most_frequent_element.py
│   │   │   ├── test_kth_largest.py
│   │   │   ├── test_maximum_subarray.py
│   │   │   ├── test_merge_two_sorted_lists.py
│   │   │   ├── test_rotate_list.py
│   │   │   └── test_two_sum.py
│   │   │
│   │   ├── graphs/
│   │   │   └── test_dijkstra.py
│   │   │
│   │   ├── heaps/
│   │   │   ├── test_find_k_most_frequent_elements.py
│   │   │   └── test_find_k_most_frequent_strings.py
│   │   │
│   │   ├── matrices/
│   │   │   └── test_sum_and_transpose.py
│   │   │
│   │   ├── number_systems/
│   │   │   └── test_base_conversion.py
│   │   │
│   │   ├── numbers/
│   │   │   └── test_find_primes.py
│   │   │
│   │   ├── recursion/
│   │   │   ├── test_all_permutations.py
│   │   │   ├── test_disk_usage.py
│   │   │   ├── test_english_ruler.py
│   │   │   └── test_summation_puzzle.py
│   │   │
│   │   ├── sequences/
│   │   │   ├── test_binary_search.py
│   │   │   └── test_moving_average.py
│   │   │
│   │   ├── stacks/
│   │   │   ├── test_check_balanced_parentheses.py
│   │   │   └── test_match_html.py
│   │   │
│   │   └── strings/
│   │       ├── test_check_palindrome.py
│   │       ├── test_find_most_frequent_string.py
│   │       ├── test_first_non_repeating_char.py
│   │       ├── test_group_anagrams.py
│   │       ├── test_longest_substring.py
│   │       ├── test_longest_word.py
│   │       ├── test_reverse_string.py
│   │       └── test_valid_anagram.py
│   │
│   └── data_structures/
│       ├── test_array_stack.py
│       ├── test_dynamic_array.py
│       └── test_singly_linked_list.py
│
└── README.md
```

## Implemented algorithms

The repository currently includes the following problems:

| Category | Algorithm |
|---|---|
| Arrays | Finding common elements in two sequences |
| Arrays | Finding duplicates |
| Arrays | Finding the most frequent element(s) |
| Arrays | Kth largest distinct element |
| Arrays | Maximum sum of a contiguous subarray (Kadane's algorithm) |
| Arrays | Merging two sorted lists |
| Arrays | List rotation |
| Arrays | Two Sum |
| Graphs | Shortest paths using Dijkstra's algorithm |
| Heaps | Finding the k most frequent elements using different approaches |
| Heaps | Finding the k most frequent strings using different approaches |
| Matrices | Row sums and matrix transpose |
| Number Systems | Conversion between arbitrary number systems (bases 2–36) |
| Numbers | Sieve of Eratosthenes |
| Recursion | Generating all unique permutations of a string |
| Recursion | Drawing an English ruler |
| Recursion | Recursive directory disk usage calculation |
| Recursion | Summation puzzle solving (backtracking) |
| Sequences | Binary search on sorted sequences |
| Sequences | Moving average (sliding window) |
| Stacks | Checking balanced parentheses and delimiters |
| Stacks | Matching opening and closing HTML tags |
| Strings | Palindrome checking |
| Strings | Finding the most frequent string |
| Strings | Finding the first non-repeating character |
| Strings | Grouping anagrams |
| Strings | Longest substring without repeated characters |
| Strings | Finding the longest word |
| Strings | String reversal |
| Strings | Valid anagram checking |

Each implementation contains a docstring describing the problem, the chosen algorithmic approach, its theoretical complexity, and relevant Python built-in functions or standard-library alternatives.

## Implemented data structures

The repository currently includes the following data structures:

| Data Structure | Implementation |
|---|---|
| Singly linked list | Insertion, removal, and reversal operations |
| Dynamic array | Append, indexed access and assignment, insertion, and removal |
| Array-based stack | Push, top (retrieve the top element without removing it), pop, and emptiness checking |

## Getting started

### Requirements

- Python 3.10 or later.
- pytest for running the tests.

Clone the repository:

```bash
git clone https://github.com/verbiestrik/python-data-structures-and-algorithms
cd python-data-structures-and-algorithms
```

Install pytest:

```bash
python -m pip install pytest
```

### Running an algorithm

The implementations can be imported into other Python scripts or interactive environments. For example, to find the maximum sum of a contiguous subarray:

```python
from algorithms.arrays.maximum_subarray import maximum_sum_cont_subarr

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = maximum_sum_cont_subarr(numbers)

print(result)  # 6
```

To group anagrams:

```python
from algorithms.strings.group_anagrams import group_anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = group_anagrams(words)

print(result)
```

## Running the tests

Testing is performed using [pytest](https://docs.pytest.org/). Run all the tests from the repository root:

```bash
python -m pytest
```

Run tests for a specific algorithm:

```bash
python -m pytest tests/algorithms/arrays/test_two_sum.py
```

Run all tests within a particular category:

```bash
python -m pytest tests/algorithms/strings/
```

For more detailed output, use:

```bash
python -m pytest -v
```

### Testing philosophy

Each algorithm and data structure has a dedicated test file, separate from its implementation.

The tests cover:
- **Normal cases:** Typical inputs and expected outputs.
- **Edge cases:** Empty sequences, single elements, duplicate values, negative numbers, and other boundary conditions where relevant.
- **Invalid inputs:** Incorrect argument types, invalid parameters, and other unsupported inputs.
- **Input preservation:** Where relevant, checking that functions do not unexpectedly modify their input sequences.

The implementations use explicit validation and raise appropriate exceptions when inputs do not satisfy the expected requirements.

## Design principles

Throughout the project, I aim to follow several principles:
1. **Understandable implementations:** Prioritise fundamental Python constructions and algorithmic understanding over unnecessary reliance on convenient libraries.
2. **Efficiency:** Consider both theoretical time and space complexity when choosing an approach.
3. **Readable code:** Use meaningful variable names, clear function interfaces, and comments where they add value.
4. **Reliable behaviour:** Handle relevant edge cases and invalid inputs explicitly.
5. **Testability:** Keep implementations independent of their test suites and make their behaviour easy to verify.

The project will continue to grow as I work through additional algorithmic problems and explore more advanced data structures and problem-solving techniques.
