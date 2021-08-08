# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        if self.value > node.value:
            if self.left is None:
                self.left = node

            else:
                self.left.insert(node)

        elif self.value < node.value:
            if self.right is None:
                self.right = node

            else:
                self.right.insert(node)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value, end=' ')
        if self.right is not None:
            self.right.inorder()

    def search(self, nvalue):

        if self.value == nvalue:
            return True

        elif nvalue < self.value and self.left:
            return self.left.search(nvalue)

        elif nvalue > self.value and self.right:
            return self.right.search(nvalue)

        return False

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value, end=' ')

        if self.right:
            self.right.print_tree()

    def size(self):
        if self.left and self.right:
            return 1 + self.left.size() + self.right.size()
        elif self.left:
            return 1 + self.left.size()
        elif self.right:
            return 1 + self.right.size()
        else:
            return 1


class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root is not None:
            self.root.inorder()

    def insert(self, key):
        new_node = BinaryTreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

    def search(self, key):

        if self.root:
            return self.root.search(key)
        else:
            return False

    def print_tree(self):
        if self.root:
            self.root.print_tree()

    def size(self):
        if self.root:
            # print(self.root.size(), end=' ')
            return self.root.size()

        else:
            return 0


"""
if __name__ == '__main__':
    binarytree = BinaryTree()

nlist = [1, 13, 5, 9, 2]
for x in nlist:
    binarytree.insert(x)

print("The binary tree: ", end='')
binarytree.print_tree()

print('\nSorted list: ', end='')
binarytree.inorder()

print("\nThe size of binary tree is: ", end='')
binarytree.size()

inputKey = int(input("\n\nEnter the value you want to add it: "))
binarytree.insert(inputKey)

print("\nThe binary tree after adding a new node: ", end='')
binarytree.print_tree()

print('\nSorted list after adding a new node: ', end='')
binarytree.inorder()
# print()
print("\n\nThe size of binary tree after adding new element is: ", end='')
binarytree.size()

searchKey = int(input("\n\nEnter the value you want to search: "))

if binarytree.search(searchKey) is True:
    print("The value is exist in the tree.")

else:
    print("The value is not exist in he tree.")

alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]

for x in alist:
    binarytree.insert(x)

print('Sorted list: ', end='')
binarytree.inorder()

searchKey = int(input("\nEnter the value you want to search: "))

if binarytree.search(searchKey) is True:
    print("The value is exist in the tree.")

else:
    print("The value is not exist in he tree.")
# print(binarytree.search(searchKey))
"""
