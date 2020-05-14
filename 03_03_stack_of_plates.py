class Stack:

    def __init__(self, capacity):
        self.list = [None] * capacity
        self.head = -1

    def push(self, data):
        if self.is_full():
            raise IndexError('push to a full stack')
        self.head += 1
        self.list[self.head] = data

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from an empty stack')
        data = self.list[self.head]
        self.head -= 1
        return data

    def peak(self):
        if self.is_empty():
            raise IndexError('peak from an empty stack')
        return self.list[self.head]

    def is_full(self):
        return self.head == len(self.list) - 1

    def is_empty(self):
        return self.head == -1


class MultiStack:

    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.stacks = []

    def push(self, data):
        last = self.get_last_stack()
        if last is not None and not last.is_full():
            last.push(data)
        else:
            stack = Stack(self.stack_capacity)
            stack.push(data)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if last is None:
            raise IndexError('pop from an empty multi stack')
        data = last.pop()
        if last.is_empty():
            self.stacks.pop()
        return data

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]


def main():
    multi_stack = MultiStack(2)
    multi_stack.push(11)
    multi_stack.push(12)
    multi_stack.push(21)
    print(multi_stack.pop())
    multi_stack.push(21)
    multi_stack.push(22)
    multi_stack.push(31)
    print(multi_stack.pop())
    print(multi_stack.pop())
    print(multi_stack.pop())
    print(multi_stack.pop())
    print(multi_stack.pop())


if __name__ == '__main__':
    main()
