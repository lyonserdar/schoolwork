#!/usr/bin/env python

"""
Project: 4 - Binary Search Tree
Author: Ali Serdar Aydogdu
Course: CS 2420-601
Date Created: 05/12/2021
Date Last Modified: 06/09/2021
"""


class BST:
    """Binary Search Tree(BST)"""

    class Node:
        """BST Node"""

        def __init__(self, item=None):
            """Initialize the BST Node"""
            self.item = item
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        """Initialize the BST with root pointing at None"""
        self.root = None

    def is_empty(self):
        """Checks if the BST is empty"""
        return self.root is None

    def size(self):
        """Returns the size of the BST"""
        if self.root:
            return self.__size(self.root, 0)

        return 0

    def __size(self, current, size):
        """Size recursive helper function"""
        if current:
            size += (
                1 + self.__size(current.left, size) + self.__size(current.right, size)
            )

        return size

    def height(self):
        """Returns the height of the BST"""
        if self.root:
            return self.__height(self.root, 0)

        return 0

    def __height(self, current, height):
        """Height recursive helper function"""
        if current:
            left_height = self.__height(current.left, height + 1)
            right_height = self.__height(current.right, height + 1)
            return max(left_height, right_height)

        return height

    def add(self, item):
        """Adds a new item to the list"""
        if self.root:
            self.__add(item, self.root)
        else:
            self.root = self.Node(item)

    def __add(self, item, current):
        """Add recursive helper function"""
        if item < current.item:
            if current.left:
                self.__add(item, current.left)
            else:
                current.left = self.Node(item)
                current.left.parent = current
        elif item > current.item:
            if current.right:
                self.__add(item, current.right)
            else:
                current.right = self.Node(item)
                current.right.parent = current
        else:
            current.item += item

    def remove(self, item):
        """Removes an item from the list"""
        if self.root:
            self.__remove(self.__find(item, self.root))

    def __remove(self, current):
        """Remove recursive helper function"""
        if not current.left and not current.right:
            if current.parent.left is current:
                current.parent.left = None
            elif current.parent.right is current:
                current.parent.right = None
        elif bool(current.left) != bool(current.right):
            child = None
            if current.left:
                child = current.left
            elif current.right:
                child = current.right

            if current.parent.left is current:
                current.parent.left = child
            elif current.parent.right is current:
                current.parent.right = child

            child.parent = current.parent
        elif current.left and current.right:
            min_right_node = self.__min(current.right)
            current.item = min_right_node.item
            self.__remove(min_right_node)

    def find(self, item):
        """Finds the item and returns it, otherwise raises a ValueError"""
        if self.root:
            result = self.__find(item, self.root)
            if result:
                return result.item
        raise ValueError("Item not found in the list")

    def __find(self, item, current):
        """Find recursive helper function"""
        if not current:
            return None
        elif item < current.item:
            return self.__find(item, current.left)
        elif item > current.item:
            return self.__find(item, current.right)
        else:
            return current

    def inorder(self):
        """Inorder traversal of the BST"""
        bst_list = []
        if self.root:
            self.__inorder(self.root, bst_list)

        return bst_list

    def __inorder(self, current, bst_list):
        """Inorder recursive helper function"""
        if current:
            self.__inorder(current.left, bst_list)
            bst_list.append(current.item)
            self.__inorder(current.right, bst_list)

    def preorder(self):
        """Preorder traversal of the BST"""
        bst_list = []
        if self.root:
            self.__preorder(self.root, bst_list)

        return bst_list

    def __preorder(self, current, bst_list):
        """Preorder recursive helper function"""
        if current:
            bst_list.append(current.item)
            self.__preorder(current.left, bst_list)
            self.__preorder(current.right, bst_list)

    def postorder(self):
        """Postorder traversal of the BST"""
        bst_list = []
        if self.root:
            self.__postorder(self.root, bst_list)

        return bst_list

    def __postorder(self, current, bst_list):
        """Postorder recursive helper function"""
        if current:
            self.__postorder(current.left, bst_list)
            self.__postorder(current.right, bst_list)
            bst_list.append(current.item)

    def rebalance(self):
        """Rebalances the BST"""
        if self.root:
            bst_list = list(self.__inorder_gen(self.root))
            root_index = len(bst_list) // 2
            self.root = bst_list[root_index]
            self.__rebalance(
                self.root, bst_list[:root_index], bst_list[root_index + 1 :]
            )
            # print(len(bst_list) // 2)

    def __rebalance(self, current, left_list, right_list):
        """Rebalance recursive helper function"""
        if current:
            if len(left_list):
                current_index = len(left_list) // 2
                if current_index > 1:
                    current.left = left_list[current_index]
                    current.left.parent = current
                    self.__rebalance(
                        current.left,
                        left_list[:current_index],
                        left_list[current_index + 1 :],
                    )
            if len(right_list):
                current_index = len(right_list) // 2
                if current_index > 1:
                    current.right = right_list[current_index]
                    current.right.parent = current
                    self.__rebalance(
                        current.right,
                        right_list[:current_index],
                        right_list[current_index + 1 :],
                    )

    def __inorder_gen(self, current):
        """Inorder generator helper function"""
        if not current:
            return
        if current.left:
            for x in self.__inorder_gen(current.left):
                yield x
        yield current
        if current.right:
            for x in self.__inorder_gen(current.right):
                yield x

    def min(self):
        """Returns the min value of the BST"""
        if self.root:
            result = self.__min(self.root)
            if result:
                return result.item
        else:
            raise ValueError("BST is empty.")

    def __min(self, current):
        """Min recursive helper function"""
        if current.left:
            return self.__min(current.left)
        else:
            return current

    def max(self):
        """Returns the max value of the BST"""
        if self.root:
            result = self.__max(self.root)
            if result:
                return result.item
        else:
            raise ValueError("BST is empty.")

    def __max(self, current):
        """Max recursive helper function"""
        if current.right:
            return self.__max(current.right)
        else:
            return current

    def __setitem__(self, item):
        self.add(item)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return bool(self.__find(item, self.root))

    def __iter__(self):
        return self.__inorder_gen(self.root)
