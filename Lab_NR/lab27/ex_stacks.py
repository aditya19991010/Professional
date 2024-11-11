class StackOverflow(Exception):
    pass

class StackUnderflow(Exception):
    pass

class Stacks:
    def __init__(self,stack, capacity):
        self.stack = stack
        self.capacity = int(capacity)

    def push(self,n):
        try:
            if len(self.stack) >= self.capacity:
                raise StackOverflow
            else:
                return self.stack.append(n)
        except StackOverflow:
            print("Error StackOverflow")

    def pop(self):
        try:
            if len(self.stack) == 0:
                raise StackUnderflow("Error StackUnderflow")
            else:
                return self.stack.pop()
        except StackUnderflow:
            print("Error StackUnderflow")

    def peek(self):
        return print(self.stack[0])

    def traverse(self):
        return print("Printing traversed stack",self.stack[::-1])



def main():
    capacity = input("Enter max capacity: ")
    list1 = list(map(int, input("Enter a numbers to create a list, separated by ',':").split(",")))
    x = Stacks(list1,capacity)
    num_push = input("Enter a number to push in the list:")
    x.push(num_push)
    print("Pushing an element-->",list1)
    x.pop()
    print("Pop an element-->",list1)
    print("Peeking in the stack.")
    x.peek()
    x.traverse()

if __name__=="__main__":
    main()