# // NotImplement stack using an array
class Stack:
    # demo
    def __init__(self):
        self.array = []
        self.max = 100
        self.count=0
    
    def peek(self):
        if not self.isEmpty():
            return True if self.count ==0 else False
        else:
            print("exception: list is empty")
            
    def push(self, element):
        if count<max:
            self.array[self.count]= element
            count+=1
        else:
            print("exception: list is full")
            
    def pop(self):
        if not self.isEmpty():
            last = self.peek()
            count-=1
            return last
        else:
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

