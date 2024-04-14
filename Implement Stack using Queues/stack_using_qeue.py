"""
stack using queue
"""

class Node:
    """
    class node
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    """
    class queue
    """
    def __init__(self) -> None:
        self.head = None

    def push(self, val):
        """
        pushes to the bottom
        """
        val = Node(val)

        if not self.head:
            self.head = val

        else:
            val.next = self.head
            self.head = val

    def pop(self):
        """
        pops top element is queue
        """
        head1 = self.head

        if head1.next is None:
            self.head = None
            return head1.data

        while head1.next.next is not None:
            head1 = head1.next

        data = head1.next.data
        head1.next = None
        return data


class MyStack:
    """
    my stack using queue
    """

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        """
        Pushes element x to the top of the stack.
        """
        self.queue.push(x)

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.
        """
        data = self.queue.head.data
        self.queue.head = self.queue.head.next
        return data

    def top(self) -> int:
        """
        Returns the element on the top of the stack.
        """
        return self.queue.head.data


    def empty(self) -> bool:
        """
        Returns true if the stack is empty, false otherwise.
        """
        return not bool(self.queue.head)



obj = MyStack()
obj.push(1)
print(obj.top())
print(obj.pop())
print(obj.empty())
