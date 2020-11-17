class Stack:
    def __init__(self):
        self.items = []

    def peek(self):
        # get the top item of the stack
        return self.items[-1]

    def pop(self):
        # remove the top item of the stack
        self.items.pop()

    def push(self, item):
        # add an item to the top of the stack
        self.items.append(item)
