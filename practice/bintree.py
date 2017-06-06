class BinTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BinTree:
    def __init__(self):
        self._root = None

    def insert(self, data):
        if self._root is None:
            self._root = BinTreeNode(data)
            return
        node = self._root
        while node is not None:
            if data < node.data:
                if node.left is None:
                    node.left = BinTreeNode(data)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BinTreeNode(data)
                    break
                else:
                    node = node.right

    def delete(self, data):
        pass

    def preorder(self):
        return [x for x in self._preorder(self._root)]

    def _preorder(self, node):
        if node is None:
            return
        for x in self._preorder(node.left):
            yield x
        yield node.data
        for x in self._preorder(node.right):
            yield x

    def inorder(self):
        return [x for x in self._inorder(self._root)]

    def _inorder(self, node):
        if node is None:
            return
        yield node.data
        for x in self._inorder(node.left):
            yield x
        for x in self._inorder(node.right):
            yield x

    def postorder(self):
        return [x for x in self._postorder(self._root)]

    def _postorder(self, node):
        if node is None:
            return
        for x in self._postorder(node.left):
            yield x
        for x in self._postorder(node.right):
            yield x
        yield node.data
