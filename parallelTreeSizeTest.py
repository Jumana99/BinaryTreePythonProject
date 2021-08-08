import time

import pytest

from main import BinaryTree


@pytest.mark.parametrize("nlist, expected_size", [([1, 13, 5, 9, 2], 5)])
def test_treesize_withparameters(nlist, expected_size):
    print("\nThe first test Start: Test tree size with parameters.")
    binarytree = BinaryTree()

    for x in nlist:
        binarytree.insert(x)

    print(binarytree.print_tree())
    treeSize = binarytree.size()

    assert expected_size == treeSize
    print("\nThe two sizes for binary tree are equal.\n")

    time.sleep(5)
    print("\nThe first test End: Test tree size with parameters.\n")


@pytest.mark.parametrize("nlist, expected_size", [([0, 3, 15, 7, 4, 12, 10], 7)])
def test_treesize_withparameters_2(nlist, expected_size):
    print("\nThe second test Start: Test tree size with parameters.")
    binarytree = BinaryTree()

    for x in nlist:
        binarytree.insert(x)

    print(binarytree.print_tree())
    treeSize = binarytree.size()

    assert expected_size == treeSize
    print("\nThe two sizes for binary tree are equal.\n")
    time.sleep(5)
    print("\nThe second test End: Test tree size with parameters.\n")
