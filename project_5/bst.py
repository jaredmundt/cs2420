

class BST:
    '''binary search tree'''

    def __init__(self) -> None:
        self._size = 0
        self._height = -1
        self._root = None

    class Node:
        '''node for holding values of bst'''
        def __init__(self, item) -> None:
            self.item = item
            self.left = None
            self.right = None
            self.parent = None

    def size(self):
        '''Return the number of nodes in the tree.'''
        return self._size

    def is_empty(self):
        '''Return	True if there	aren't	any nodes in the	tree,	False	otherwise.'''
        return self._size == 0
    
    def height(self):
        '''Return the height of the tree, defined is the length of the path from the root to its deepest leaf. A tree with zero nodes has a height of - 1.'''
        return self._height

    def add(self, item):
        '''Add item to its proper place in the tree. Return the modified tree.'''
        self._size += 1
        height = 0
        new_node = self.Node(item)
        if not self._root:
            self._root = new_node 
        else:
            node = self._root
            while node:
                height += 1
                if item < node.item:
                    if node.left:
                        node = node.left
                    else:
                        node.left = new_node
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = new_node
                        break

        self._height = max(self._height, height)



    def remove(self, item):
        '''Remove item from the tree if it exists, if not - do nothing. Return the resulting tree.'''
        self._size -= 1
        # if self._root:
        #     if self._root.item == item:

        # parent = None
        # node = self._root
        # while node:
        #     if node.left:
        #         if item == node.left.item:

        #     elif item < node.item:
        #         node = node.left
        #     else:
        #         node = node.right
        #     parent = node
        # return self

    def find(self, item):
        '''Return the matched item. If item is not in the tree, raise a ValueError.'''
        node = self._root
        while node:
            if item == node.item:
                return node.item
            elif item < node.item:
                node = node.left
            else:
                node = node.right
        raise ValueError
       

    def inorder(self):
        '''Return a list with the data items in order of inorder traversal.'''
        lyst: list[self.Node] = []
        if self._root:
            self.inorder_recurive(self._root, lyst)
        return lyst

    def inorder_recurive(self, node: Node, lyst: list[Node]):
        '''Helper for inorder traversal'''
        if node.left:
            self.inorder_recurive(node.left, lyst)
        lyst.append(node.item)
        if node.right:
            self.inorder_recurive(node.right, lyst)
            

    def preorder(self):
        '''Return a list with the data items in order of preorder traversal.'''
        lyst: list[self.Node] = []
        if self._root:
            self.preorder_recurive(self._root, lyst)
        return lyst

    def preorder_recurive(self, node: Node, lyst: list[Node]):
        '''Helper for preorder traversal'''
        lyst.append(node.item)
        if node.left:
            self.preorder_recurive(node.left, lyst)
        if node.right:
            self.preorder_recurive(node.right, lyst)


    def postorder(self):
        '''Return a list with the data items in order of postorder traversal.'''
        lyst: list[self.Node] = []
        if self._root:
            self.postorder_recurive(self._root, lyst)
        return lyst

    def postorder_recurive(self, node: Node, lyst: list[Node]):
        '''Helper for postorder traversal'''
        if node.left:
            self.postorder_recurive(node.left, lyst)
        if node.right:
            self.postorder_recurive(node.right, lyst)
        lyst.append(node.item)

