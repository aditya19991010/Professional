import time

# Question set with consistent order for options
question_set = [
    {"Which keyword is used to define a function in Python?": ["def", "func", "function", "define"]},
    {"What is the data type of the result of `5 / 2` in Python?": ["int", "float", "str", "bool"]},
    {"Which of these data types is immutable in Python?": ["list", "set", "dictionary", "tuple"]},
    {"What does `len()` function return?": [ "The size of memory","The length of an object", "The number of data types", "None of these"]},
    {"What is the correct syntax to create a dictionary in Python?": ["{'key': 'value'}", "{key = value}", "[key: value]", "key -> value"]},
    {"What is the result of `2 ** 3`?": [ "6", "9", "Error","8"]},
    {"Which module in Python is used for working with JSON data?": [ "os", "sys", "math", "json"]},
    {"What is the purpose of the `yield` keyword in Python?": ["To create a generator", "To return multiple values", "To stop a function", "None of these"]},
    {"Which symbol is used for comments in Python?": ["#", "//", "/* */", "--"]},
    {"How do you declare a lambda function in Python?": [ "def lambda():", "lambda arguments: expression","lambda -> expression", "lambda(arguments)"]}
]

answer_key = [1, 2, 4, 2, 1, 1, 4, 1, 1, 2]

#decorator
def time_log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"This quiz is finished in {total_time: .2f} seconds")
        return result
    return wrapper

#Generating questions
@time_log
def question_generator(question_set, answer_key):
    user_answers = []
    user_answers_text = []
    for q_index, question in enumerate(question_set):
        for question_text, options in question.items():
            print(f"\n{q_index + 1}. {question_text}")
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
            while True:
                try:
                    user_input = int(input("\nEnter your answer (1/2/3/4): "))
                    if 1 <= user_input <= 4:
                        user_answers.append(user_input) #adding into the list
                        user_answers_text.append(options[user_input - 1]) #adding options in a list, substracting for correct index
                        break
                    else:
                        print("Please choose a valid option (1/2/3/4).")
                except ValueError:
                    print("Invalid input. Please enter a number (1/2/3/4).")
    return user_answers, user_answers_text

#function for marksheet
def marksheet(user_answers, user_answers_text, question_set, answer_key):
    u_marks = 0 #initialize user marks
    for i in range(len(user_answers)):
        if user_answers[i] == answer_key[i]:
            u_marks += 1
        print(f"\nQuestion {i + 1}:")
        print(f"Your Answer: {user_answers_text[i]}")
        print(f"Correct Answer: {list(question_set[i].values())[0][answer_key[i] - 1]}")
    print(f"\nTotal Marks: {u_marks}/{len(answer_key)}")

def main():
    user_answers, user_answers_text = question_generator(question_set, answer_key)
    marksheet(user_answers, user_answers_text, question_set, answer_key)

if __name__ == "__main__":
    main()
