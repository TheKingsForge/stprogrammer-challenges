# Stack and Queue Data structures
# We already know: Lists, Tuples, and Dictionaries

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
    
    def size(self):
        return len(self.items)
    

class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    
stack = Stack()
for i in range (0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())

a_queue = Queue()

for i in range(5):
  a_queue.enqueue(i)

print(a_queue.size())

# Challenge 1
## Reverse the string "yesterday" using a stack.
string_stack = Stack()
for char in "yesterday":
    string_stack.push(char)

reverse_word = ""

for i in range(0, string_stack.size()):
    reverse_word += string_stack.pop()
print(reverse_word)

# Challenge 2
## Use a stack to create a new list with the items in the following list reversed: [1, 2, 3, 4 , 5]
number_list_stack = Stack()

for num in [1, 2, 3, 4 , 5]:
    number_list_stack.push(num)

reversed_num_stack = []
for i in range(0, number_list_stack.size()):
    reversed_num_stack.append(number_list_stack.pop())

print(reversed_num_stack)

