class BST:
    """Binary Search Tree(BST)"""

    class Node:
        """
        BST Node
        """

        def __init__(self, item=None):
            self.item = item
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def size(self):
        if self.root:
            return self.__size(self.root, 0)
        else:
            return 0

    def __size(self, current, size):
        if current:
            size += (
                1 + self.__size(current.left, size) + self.__size(current.right, size)
            )

        return size

    def height(self):
        if self.root:
            return self.__height(self.root, 0)
        else:
            return 0

    def __height(self, current, height):
        if current:
            left_height = self.__height(current.left, height + 1)
            right_height = self.__height(current.right, height + 1)
            return max(left_height, right_height)
        else:
            return height

    def add(self, item):
        if self.root:
            self.__add(item, self.root)
        else:
            self.root = self.Node(item)

    def __add(self, item, current):
        if item < current.item:
            if current.left:
                self.__add(item, current.left)
            else:
                current.left = self.Node(item)
        elif item > current.item:
            if current.right:
                self.__add(item, current.right)
            else:
                current.right = self.Node(item)
        else:
            self.current.item += item

    def remove(self, item):
        pass

    def find(self, item):
        if self.root:
            result = self.__find(item, self.root)
            if result:
                return result.item
        raise ValueError("Item not in the list")

    def __find(self, item, current):
        if not current:
            return None

        if item < current.item:
            return self.__find(item, current.left)
        elif item < current.item:
            return self.__find(item, current.right)
        else:
            return current

    def inorder(self):
        bst_list = []
        if self.root:
            self.__inorder(self.root, bst_list)

        return bst_list

    def __inorder(self, current, bst_list):
        if current:
            self.__inorder(current.left, bst_list)
            bst_list.append(current.item)
            self.__inorder(current.right, bst_list)

    def preorder(self):
        pass

    def postorder(self):
        pass

    def rebalance(self):
        pass

    def __setitem__(self, item):
        self.add(item)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return bool(self.__find(item, self.root))
