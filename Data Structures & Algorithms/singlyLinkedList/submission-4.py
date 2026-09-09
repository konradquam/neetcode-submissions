class Node:
        def __init__(self, val, next_node=None, prev_node=None):
            self.val = val
            self.next_node = next_node
            self.prev_node = prev_node
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        node = self.head
        if not node:
            return -1
        i = 0
        while i < index:
            if node.next_node is None:
                return -1
            node = node.next_node
            i += 1
        return node.val

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            if self.tail:
                self.head.next_node = self.tail
                self.tail.prev_node = self.head
            else:
                self.tail = self.head
            self.size += 1
            return
        new_node = Node(val, self.head, None)
        self.head.prev_node = new_node
        self.head = new_node
        self.size += 1
        return
        

    def insertTail(self, val: int) -> None:
        if self.tail is None:
            self.tail = Node(val)
            if self.head:
                self.tail.prev_node = self.head
                self.head.next_node = self.tail
            else:
                self.head = self.tail
            self.size += 1
            return
        new_node = Node(val, None, self.tail)
        self.tail.next_node = new_node
        self.tail = new_node
        self.size += 1
        return

    def remove(self, index: int) -> bool:
        node = self.head
        if not node:
            return False
        if index == 0:
            self.head = self.head.next_node
            self.size -= 1
            return True
        if index == self.size -1:
            self.tail = self.tail.prev_node
            self.size -= 1
            return True
        i = 0
        while i < index:
            if not node.next_node:
                return False
            node = node.next_node
            i += 1
        prev_node = node.prev_node
        next_node = node.next_node

        if prev_node:
            prev_node.next_node = next_node
        if next_node:
            next_node.prev_node = prev_node
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        node = self.head
        while node:
            values.append(node.val)
            node = node.next_node
        return values
        
