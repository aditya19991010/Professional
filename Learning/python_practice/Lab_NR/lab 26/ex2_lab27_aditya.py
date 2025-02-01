class StackOverflow(Exception):
    pass
class Stachunderflow(Exception):
    pass

class stacks:
    def __init__(self,list_stacks):
        capacity = 5
        self.list_stacks = list_stacks

    def push(self,n):
        return self.list_stacks.append(n)

    def pop(self):
        self.list_stacks.pop()

    def peek(self):
        return print(self.list_stacks[-1])



def main():
    list1 = list(map(int, input("Enter a numbers to create a list, separated by ',':").split(",")))
    x = stacks(list1)
    x.pop()
    print("Pop an element-->",list1)
    num_push = input("Enter a number to push in the list:")
    x.push(num_push)
    print("Pushing an element-->",list1)
    print("Peeking in a list.")
    x.peek()

if __name__=="__main__":
    main()