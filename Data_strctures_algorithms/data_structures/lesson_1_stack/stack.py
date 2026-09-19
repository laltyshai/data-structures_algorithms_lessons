# // NotImplement stack using an array
class Stack:
    # demo
    def __init__(self):
        self.array = []
        self.max = 100
        self.count=0
    
    def peek(self):
        if not self.isEmpty():
            return self.array[-1]
        else:
            print("exception: list is empty")
    def push(self, element):
            self.array.append(element)
    def pop(self):
        if not self.isEmpty():
            self.array.pop()
            print("exception: list is empty")
        
    def isEmpty(self):
        return False if self.array else True

spisok = Stack()
spisok.peek()
spisok.pop()
spisok.push(1)
spisok.push(2)
spisok.push(3)
spisok.push(4)

print(spisok.peek())
print(spisok.array)
spisok.pop()
print(spisok.peek())

print(spisok.array)

