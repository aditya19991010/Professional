from random import choice

def get_description():
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)

if __name__ == "__main__":
    print("Inside report")
    get_description()
