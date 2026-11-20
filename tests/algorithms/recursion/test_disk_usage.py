import os
import pytest

from algorithms.recursion.disk_usage import disk_usage


def test_single_file(tmp_path):

    file_path = tmp_path / "file.txt"
    file_path.write_text("Hello, world!", encoding="utf-8")

    assert disk_usage(file_path) == 13


def test_empty_directory(tmp_path):

    directory = tmp_path / "empty"
    directory.mkdir()

    assert disk_usage(directory) == os.path.getsize(directory)


def test_nested_directory(tmp_path):

    root = tmp_path / "root"
    root.mkdir()

    file_1 = root / "file1.txt"
    file_1.write_text("Hello", encoding="utf-8")

    subdirectory = root / "subdirectory"
    subdirectory.mkdir()

    file_2 = subdirectory / "file2.txt"
    file_2.write_text("World!", encoding="utf-8")

    nested_directory = subdirectory / "nested"
    nested_directory.mkdir()

    file_3 = nested_directory / "file3.txt"
    file_3.write_text("Python", encoding="utf-8")

    expected = sum(
        os.path.getsize(path)
        for path in [
            root,
            file_1,
            subdirectory,
            file_2,
            nested_directory,
            file_3
        ]
    )

    assert disk_usage(root) == expected


def test_directory_with_multiple_files(tmp_path):

    directory = tmp_path / "files"
    directory.mkdir()

    file_1 = directory / "a.txt"
    file_1.write_text("abc", encoding="utf-8")

    file_2 = directory / "b.txt"
    file_2.write_text("defgh", encoding="utf-8")

    expected = (
        os.path.getsize(directory)
        + os.path.getsize(file_1)
        + os.path.getsize(file_2)
    )

    assert disk_usage(directory) == expected


def test_directory_containing_empty_subdirectory(tmp_path):

    root = tmp_path / "root"
    root.mkdir()

    empty_directory = root / "empty"
    empty_directory.mkdir()

    expected = (
        os.path.getsize(root)
        + os.path.getsize(empty_directory)
    )

    assert disk_usage(root) == expected


def test_nonexistent_path(tmp_path):

    path = tmp_path / "nonexistent"

    with pytest.raises(FileNotFoundError):
        disk_usage(path)


def test_invalid_path_type():

    with pytest.raises(TypeError):
        disk_usage(None)


def test_symbolic_link_is_ignored(tmp_path):

    root = tmp_path / "root"
    root.mkdir()

    target = tmp_path / "target.txt"
    target.write_text("Hello", encoding="utf-8")

    link = root / "link.txt"

    try:
        link.symlink_to(target)
    except (OSError, NotImplementedError):
        pytest.skip("Symbolic link creation is not supported.")

    assert disk_usage(root) == os.path.getsize(root)
