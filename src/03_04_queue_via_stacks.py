class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, data):
        node = self.Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            raise IndexError('pop from an empty stack')
        data = self.head.data
        self.head = self.head.next
        return data

    def peak(self):
        if self.head is None:
            raise IndexError('pop from an empty stack')
        return self.head.data

    def is_empty(self):
        return self.head is None


class StacksQueue:
    def __init__(self):
        self.new = Stack()
        self.old = Stack()

    def enqueue(self, data):
        self.new.push(data)

    def dequeue(self):
        self.move_items()
        if self.old.is_empty():
            raise IndexError('dequeue from an empty queue')
        return self.old.pop()

    def move_items(self):
        if not self.old.is_empty():
            return
        while not self.new.is_empty():
            data = self.new.pop()
            self.old.push(data)

    def peak(self):
        self.move_items()
        if self.old.__init__():
            raise IndexError('peak from an empty queue')
        return self.old.peak()

    def is_empty(self):
        return self.new.is_empty() and self.old.is_empty()


def main():
    q = StacksQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())


if __name__ == '__main__':
    main()
