"""
Recursive Disk Usage
====================

Problem
-------
Calculate the cumulative size, in bytes, of a file or directory and all its
descendants.

For a directory, the result includes its own immediate size and the reported
sizes of all files and subdirectories contained within it.

Symbolic links are ignored to avoid double-counting files and accidentally
traversing directory cycles.

Approach
--------
Use recursion to traverse the directory hierarchy.

1. Obtain the immediate size of the current path using os.path.getsize().
2. If the path is a directory, iterate over its entries using os.scandir().
3. Recursively calculate the size of each non-symbolic-link entry.
4. Add the results to the cumulative total.
5. Return the total size.

Complexity
----------
Let N be the number of filesystem entries visited and D the maximum
directory nesting depth.

Time:  O(N), assuming filesystem metadata operations take O(1) time.

Space: O(D) auxiliary space for the recursive call stack and active
       directory iterators.

Python alternatives
-------------------
- os.path.getsize(): Returns the size of a file or directory in bytes.
- os.scandir(): Efficiently iterates over directory entries without
  creating a complete list of filenames.
- os.listdir(): An alternative for obtaining directory contents, but
  creates a list containing all entry names.
- os.walk(): An iterative alternative for recursively traversing directory
  hierarchies.

Note
----
The returned value represents the sum of the sizes reported by
os.path.getsize(), not necessarily the actual physical disk space occupied.
For example, directory metadata, filesystem allocation, compression and
sparse files can affect the actual storage consumption.
"""

import os


def disk_usage(path: str | os.PathLike[str]) -> int:

    # Ignore symbolic links to avoid following directory cycles.
    if os.path.islink(path):
        return 0

    total = os.path.getsize(path)

    if os.path.isdir(path):

        with os.scandir(path) as entries:

            for entry in entries:
                total += disk_usage(entry.path)

    return total
