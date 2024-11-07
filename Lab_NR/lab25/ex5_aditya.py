class AgeTooYoungError(Exception):
    pass


def checkAge():
    age = int(input("Enter your age: "))
    try:
        if age < 18:
            raise AgeTooYoungError("Age must be more than 18")
        else:
            print("Age accepted")
    except AgeTooYoungError:
        print(f"Error: Invalid age")

checkAge()