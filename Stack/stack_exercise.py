from collections import deque


class Stack:
    def __init__(self):
        self.container= deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
       return self.container.pop()

    def peak(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)






def reverse_string(string):
    stack = Stack()
    new_string = ""
    for s in string:
        stack.push(s)

    while not stack.is_empty():
        new_string+=stack.pop()

    print(new_string)


if __name__ == "__main__":
    s = Stack()
    s.push(12)
    s.peak()
    reverse_string("hello")

