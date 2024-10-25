#fibbonacci
# Write a generator function fibonacci that yields the Finocacci series number infinitely.
# Create a generator expression fib_gen that calls this function. Print the 10 numbers of
# this generator expression using next()
# B. Repeat the same for generating even_numbers
#
# C. Repeat the same for generating expressions for powers of 2

def fibbonacci():
    a=0
    b = 1
    c = 0
    while True:
        yield a
        a = c
        c = b
        b += a

fib_gen = (num for num in fibbonacci())

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))

print("\nPrinting even numbers")
def even_num_series():
    n = 2
    while True:
        yield n
        n += n

even_gen = (num for num in even_num_series())

for i in range(0,5):
    print(next(even_gen))

print("\nGenerating expression with power 2")

def exp_power_2():
    num = 1
    power = 2
    while True:
        yield num**power
        num += 1

power_gen = (x for x in exp_power_2())

for i in range(0,5):
    print(next(power_gen))

