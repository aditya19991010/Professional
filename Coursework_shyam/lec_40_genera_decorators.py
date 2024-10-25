#Generators
#Need --> reading csv file,


def csv_reader(filename):
    file = open(filename)
    result = file.read().split("\n")
    return result

csv_gen = csv_reader("/home/ibab/Documents/word_file.txt")
row_count = 0

for row in csv_gen:
    row_count +=1

print(f"Row count is {row_count}")

def csv_reader(file_name):
    for row in open(file_name,"r"):
        yield row

infinite_num = list()

def infinite_num():
    y = 0
    while True:
        yield y
        y += 1
        print(y)


def decorator(func):
    def wrapper():
        print("Something is happening before function.")
        func()
        print("Something is happening after function.")
    return wrapper
def say_whee():
    print("Wheeee!!")

say_whee = decorator(say_whee)
say_whee()

def main():
    gen = infinite_num()
    print(next(gen))
    print(next(gen))

#generate all the palindrome of digits between 0 and infinity.



if __name__=="__main__":
    main()