## Functions
from sys import platlibdir


def functions():
    do_nothing()

def do_nothing():
    pass

value = do_nothing()
print(value)

if value:
    print('Its some thing')
else:
    print("it's no thing")

    #positional argument
        #values are copied to corresponding parameters
        #Need to remember the meaning of each position


def players(bat, bowl, keep, all="Hardik"):
    return {'batsman': bat, 'bowler': bowl, 'keeper' : keep, 'allrounder' : all }

p = players('Rohit', 'Ishan', 'Kohli')
print(p)

# keyword argument
p = players(bat='Dhoni',bowl='kohli', keep='Ishan')
print(p)


    # default parameter values
    # Gather positional argument
    # gather keyword argument
    # inner functions
    # lambda
    # passing function


# Generate triangle
# num_of_lines = 5
# num = 1
# delimiter = "\t"
#
# for i in num_of_lines:


