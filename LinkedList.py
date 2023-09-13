class Node:
    def __init__ (self, value = 0, next=None):
        self.value = value
        self.next = next
        
class LinkedList(object):
    def __init__(self):
        self.head = None
    # O(n)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # current = self.head
            # while(current.next):
            #      current = current.next
            # current.next = new_node
            
            self.tail.next = new_node
            self.tail = self.tail.next
    # O(n)
    def get(self,idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current
    def insert(self, idx, value):
        new_node = Node(value)
        
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        
        for _ in range(idx-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
    def remove(self, idx):
        new_node = Node(value);
        for _ in range(idx-1):
            current = current.next;
        new_node.next = current.next.next;
        current.next = new_node; 