import pytest

from main import BinaryTree

inputsData = [
    ([1, 13, 5, 9, 2], 5, False),
    ([7, 1, 3, 9, 2, 8, 0], 7, False),
    ([0, 6, 43, 39, 32, 78, 70, 8, 77], 19, True),
]


@pytest.mark.parametrize("nlist, expected_size, isNegative", inputsData)
def test_treesize_withparameters(nlist, expected_size, isNegative):
    print("\nThe first Test Start: Test tree size with parameters.\n")
    binarytree = BinaryTree()
    for x in nlist:
        binarytree.insert(x)

    print(binarytree.print_tree())
    treeSize = binarytree.size()

    if isNegative:
        # print(inputsData[2][1])
        # print(treeSize)
        if expected_size == treeSize:
            assert False

        else:
            assert True
            print("\nThe two sizes for binary tree are equal.\n")

    else:
        # assert True
        assert expected_size == treeSize
        print("\nThe two sizes for binary tree are equal.\n")
