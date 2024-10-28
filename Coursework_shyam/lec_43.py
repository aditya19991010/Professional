#try #except

'''exception --> beyond the error, to handle the errors,
it is an expensive block, therefore, it is not suggested to use.
uses stacks for execution
'''

def try_except():
    short_list = [11,22,33]
    while True:
        value = input('Position [q for quit]: ')
        if value == 'q':
            break
        try:
            position = int(value)
            print(short_list[position])
        except IndexError as err:
            print('Bad index: ', position)
        except SyntaxError as syn:
            print("Syntax error: ", syn)
        except Exception as other:
            print('Something else broken', other)

try_except()

#Modules
# import --> imports module into the program and grab the function avail in the module func.

