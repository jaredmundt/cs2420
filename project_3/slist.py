
class SList:
    class SListNode:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self._head = None
        self._size = 0
        self._iter_node = None


    def insert(self, value):
        '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
        new_node = self.SListNode(value)
        dummy = self.SListNode()
        dummy.next = self._head
        node = dummy
        while True:
            if not node.next or node.next.value > value:
                new_node.next = node.next
                node.next = new_node
                self._size += 1
                break

            node = node.next

        self._head = dummy.next


    def find(self, value):
        '''Search for a value in the list, return it if found, None otherwise'''
        node = self._head
        while node:
            if node.value > value:
                return None
            if node.value == value:
                return node.value
            node = node.next
        return None


    def remove(self, value) -> bool:
        '''Remove the first occurance of value.'''
        node = self._head
        prev = None
        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self._head = node.next
                self._size -= 1
                return True
            prev = node
            node = node.next
        return False

    def remove_all(self, value):
        '''Remove all instances of value'''
        cont = True
        while cont:
            cont = self.remove(value)

    def __str__(self):
        '''Convert the list to a string and return it'''
        res: str = "["
        node = self._head
        while node:
            res += node.value.__str__()
            res += ","
            node = node.next
        res += "]"
        return res


    def __iter__(self):
        '''Return an iterator for the list'''
        self._iter_node = self._head
        return self

        
    def __next__(self):
        if not self._iter_node:
            raise StopIteration
        value = self._iter_node.value
        self._iter_node = self._iter_node.next
        return value


    def __getitem__(self, index):
        '''Return the item at the given index, or throw an exception if invalid index'''
        node = self._head
        for _ in range(index):
            if not node:
                raise Exception("index out of bounds")
            node = node.next

        if not node:
            raise Exception("index out of bounds")
        return node.value


    def __len__(self):
        return self._size
