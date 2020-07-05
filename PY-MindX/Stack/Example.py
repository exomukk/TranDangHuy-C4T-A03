import sys


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "hello"

    def push(self):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

        else:
            return None

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# new_stack = Stack()
# new_stack.push(1)
# print(new_stack)
# new_stack.push(2)
# print(new_stack)


class StackTraining(Stack):
    def reverse(self, string_sample):
        for char in string_sample:
           self.push(char)

        reversed_string = ''

        for _ in string_sample:
            reversed_string += self.pop()

        return reversed_string 

    

