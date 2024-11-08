class stacks:
    def __init__(self,list_stacks):
        self.list_stacks = list_stacks

    def push(self,n):
        return self.list_stacks.append(n)

    def pop(self):
        self.list_stacks.pop()

list1 = [1,2,3,4,5,6]
x = stacks(list1)
print(x)

x.pop()
# print(x)