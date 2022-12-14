''' Stack Class for Project 4 of cs2420 '''

class Stack:
    '''ADT stack implemented as linked list'''
    class Node:
        '''Node class for linked list'''

        def __init__(self, value=None):
            '''New list Node'''
            self.value = value
            self.next = None

    def __init__(self) -> None:
        '''new Stack'''
        self._head = None
        self._size = 0
        self._tail = None

    def size(self):
        '''size(): return the number of items on the stack.'''
        return self._size

    def __str__(self):
        '''Convert the Stack to a string and return it'''
        res: str = "["
        node = self._head
        while node:
            res += node.value.__str__()
            res += ","
            node = node.next
        res += "]"
        return res

    def push(self, item):
        '''push an item onto the stack. Size increases by 1.'''
        new_node = self.Node(item)
        if self._head:
            new_node.next = self._head
        self._head = new_node
        self._size += 1

    def pop(self) -> any:
        '''remove the top item from the stack and return it.
            Raise an IndexError if the stack is empty.'''
        if not self._head:
            raise IndexError("stack is empty")
        self._size -= 1
        node = self._head
        self._head = self._head.next
        return node.value

    def clear(self):
        '''empty the stack'''
        self._head = None
        self._size = 0

    def top(self) -> any:
        '''return the item on top of the stack without removing it.
            Raise an IndexError if the stack is empty.'''
        if not self._head:
            raise IndexError("stack is empty")
        node = self._head
        return node.value
