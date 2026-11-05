# Python Algorithms & Data Structures

A collection of Python implementations of fundamental algorithms and problem-solving techniques, developed as part of my interest in algorithms, data structures, and complexity analysis.

The project focuses on algorithmic thinking, efficient implementations, code quality, and software testing.

## Development approach

The algorithms in this repository were initially drafted independently by me, based on my understanding of the underlying problems, algorithmic principles, and data structures in Python. I subsequently used ChatGPT as a programming assistant to review and improve the implementations. This collaboration focused on:

- **Algorithm optimisation:** Improving time and space efficiency where possible.
- **Code quality:** Improving readability, structure, naming conventions, and documentation.
- **Error handling:** Introducing input validation and appropriate exceptions.
- **Testing:** Developing separate pytest test files covering normal cases, edge cases, and invalid inputs.
- **Complexity analysis:** Documenting the theoretical time and auxiliary space complexity of each implementation.

Importantly, I reviewed and verified the resulting implementations to ensure that I understood the algorithms, their underlying logic, and the design decisions involved. The goal was not simply to obtain working solutions, but to use the review process as an opportunity to deepen my understanding of (data structures in) Python and algorithmic problem-solving.

## Repository structure

The repository is organised by algorithm category, with implementation files separated from their corresponding tests.

```text
python-algorithms/
│
├── algorithms/
│   ├── arrays/
│   │   ├── common_elements.py
│   │   ├── maximum_subarray.py
│   │   ├── rotate_list.py
│   │   └── two_sum.py
│   │
│   ├── matrices/
│   │   └── sum_and_transpose.py
│   │
│   ├── numbers/
│   │   └── find_primes.py
│   │
│   ├── sequences/
│   │   ├── kth_largest.py
│   │   └── moving_average.py
│   │
│   └── strings/
│       ├── check_palindrome.py
│       ├── group_anagrams.py
│       ├── longest_substring.py
│       ├── longest_word.py
│       ├── reverse_string.py
│       └── valid_anagram.py
│
├── tests/
│   └── algorithms/
│       ├── arrays/
│       ├── matrices/
│       ├── numbers/
│       ├── sequences/
│       └── strings/
│
└── README.md
```

## Implemented algorithms

The repository currently includes the following problems:

| Category | Algorithm |
|---|---|
| Arrays | Common elements in two sequences |
| Arrays | Maximum sum of a contiguous subarray (Kadane's algorithm) |
| Arrays | List rotation |
| Arrays | Two Sum |
| Matrices | Row sums and matrix transpose |
| Numbers | Sieve of Eratosthenes |
| Sequences | Kth largest distinct element |
| Sequences | Moving average (sliding window) |
| Strings | Palindrome checking |
| Strings | Grouping anagrams |
| Strings | Longest substring without repeated characters |
| Strings | Finding the longest word |
| Strings | String reversal |
| Strings | Valid anagram checking |

Each implementation contains a docstring describing the problem, the chosen algorithmic approach, its theoretical complexity, and relevant Python alternatives.

## Getting started

### Requirements

- Python 3.10 or later.
- pytest for running the tests.

Clone the repository:

```bash
git clone [url](https://github.com/verbiestrik/python-data-structures-and-algorithms)
cd python-algorithms
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

Each algorithm has a dedicated test file, separate from its implementation.

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
