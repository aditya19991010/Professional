import time
question_set = [
    {"Which keyword is used to define a function in Python?": {"def", "func", "function", "define"}},
    {"What is the data type of the result of `5 / 2` in Python?": { "int", "float","str", "bool"}},
    {"Which of these data types is immutable in Python?": {"list", "set","tuple", "dictionary"}},
    {"What does `len()` function return?": {"The length of an object", "The size of memory", "The number of data types", "None of these"}},
    {"What is the correct syntax to create a dictionary in Python?": { "{key = value}", "[key: value]", "key -> value", "{'key': 'value'}"}},
    {"What is the result of `2 ** 3`?": {"8", "6", "9", "Error"}},
    {"Which module in Python is used for working with JSON data?": { "os", "json","sys", "math"}},
    {"What is the purpose of the `yield` keyword in Python?": { "To return multiple values", "To stop a function", "None of these","To create a generator"}},
    {"Which symbol is used for comments in Python?": {"#", "//", "/* */", "--"}},
    {"How do you declare a lambda function in Python?": {"lambda arguments: expression", "def lambda():", "lambda -> expression", "lambda(arguments)"}}
]

answer_key = [1,2,3,1,4,1,2,4,1]

#time decorator
def time_log(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(args,kwargs)
        end_time= time.time()
        total_time = end_time - start_time
        print(f"This task is finished in {total_time}")
    return wrapper

# question_set = "question_py_quiz.txt"

# @time_log
def question_generator(question_set, answer_key):
    q_index = 0
    user_answers_text = []
    user_answer = []
    total_marks = 10
    while q_index != len(question_set):
        qindex = 0
        for quest in question_set:
            qindex += 1
            for key,value in quest.items():
                print(f"\n{qindex}.{key}", "\nChoose one:\n")
                opt_index = 0
                for opt in value:
                    opt_index += 1
                    print(f"{opt_index}.{opt}", end="\n")
                n = int(input("\nEnter your answer(1/2/3/4): "))
                user_answer.append(n)
                user_answers_text.append(list(value)[n - 1])
                q_index += 1
    return user_answer,user_answers_text

def marksheet(user_answer,user_answers_text,question_set, answer_key):
    u_marks = 0
    for i in range(len(user_answer)):
        if user_answer[i] == answer_key[i]:
            u_marks +=1
        else:
            u_marks -=1
        print(f"{question_set[i].keys()}", end="\n")
        print(f"{i+1}.{user_answers_text[i]}", end="\n")
    print(f"Obtained marks: {u_marks}")


def main():
    question_set = "questions_py_quiz.txt"
    answer_key = [1, 2]
    # start = str(input("Typer 'start' to begin the test: ")).lower()
    # while True:
    #     if start == "start":
    question_generator(question_set,answer_key)
        # else:
        #     break
    marksheet(user_answer,user_answers_text,question_set, answer_key)

if __name__=="__main__":
    main()

