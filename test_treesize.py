from main import BinaryTree


def test_treesize():
    expected_size = 5
    binarytree = BinaryTree()

    nlist = [1, 13, 5, 9, 2]
    for x in nlist:
        binarytree.insert(x)

    print("\nThe binary tree: ", end='')
    binarytree.print_tree()

    treeSize = binarytree.size()
    assert treeSize == expected_size
    print("\n\nThe two sizes for binary tree are equal.")
