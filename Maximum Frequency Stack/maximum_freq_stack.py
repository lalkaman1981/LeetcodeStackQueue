"""
freq stack maximum finder
"""

class Node:
    """
    node class
    """
    def __init__(self, data, frequency = None) -> None:
        self.data = data
        self.frequency = frequency if frequency else 1
        self.next = None

    def __repr__(self) -> str:
        return f"data: {self.data}, frequency: {self.frequency}"

class FreqStack:
    """
    freq stack class
    """
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        """
        pushes
        """
        if not self.head:
            self.head = Node(val)

        else:
            head1 = self.head
            head2 = head1

            while head1 is not None:
                if val == head1.data:
                    new_node = Node(val,  head1.frequency + 1)
                    new_node.next = head2
                    self.head = new_node
                    break
                head1 = head1.next

            if head1 is None:
                new_node = Node(val)
                new_node.next = self.head
                self.head = new_node

    def pop(self) -> int:
        """
        pops from stack
        """
        head1 = self.head
        head2 = head1
        maximum = 0

        while head1 is not None:
            if head1.frequency > maximum:
                maximum = head1.frequency
            head1 = head1.next

        if head2.frequency == maximum:
            self.head = self.head.next
            return head2.data

        while head2.next.next is not None:

            if head2.next.frequency == maximum:

                data = head2.next.data
                head2.next = head2.next.next

                return data

            head2 = head2.next

        if head2.frequency == maximum:
            return head2.data
        return head2.next.data

obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
