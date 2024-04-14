"""
code with queue using stacks 
"""

class Node:
    """
    node class
    """
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class Stack:
    """
    stack class
    """
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        """
        pushes to the stack
        """
        new_node = Node(data, self.head)
        self.head = new_node

    def pop(self):
        """
        pops first el
        """
        deleted = self.head
        self.head = self.head.next
        return deleted.data


class MyQueue:
    """
    queue class
    """
    def __init__(self):
        self.stack = Stack()

    def push(self, x: int) -> None:
        """
        pushes to the front
        """
        self.stack.push(x)

    def pop(self) -> int:
        """
        pops last el
        """
        if self.stack.head is None or self.stack.head.next is None:
            numb = self.stack.head.next.data if self.stack.head.next else self.stack.head.data
            self.stack.head = None
            return numb

        head1 = self.stack.head
        while head1.next.next is not None:
            head1 = head1.next

        numb = head1.next.data
        head1.next = head1.next.next
        return numb

    def peek(self) -> int:
        """
        peek first el
        """
        if self.stack.head is None or self.stack.head.next is None:
            numb = self.stack.head.next.data if self.stack.head.next else self.stack.head.data
            return numb

        head1 = self.stack.head
        while head1.next.next is not None:
            head1 = head1.next

        numb = head1.next.data
        return numb

    def empty(self) -> bool:
        """
        check if the queue is empty
        """
        return self.stack.head is None
