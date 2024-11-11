import csv

students = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]
with open('students_file.csv', mode='w') as file:
    student_csv_writer = csv.writer(file) #call a writer function
    student_csv_writer.writerows(students) #write in rows

with open("students_file.csv", mode='r') as file:
    student_csv_read = csv.reader(file, delimiter=",")
    print()

with open("states_by_country.csv", mode="r") as file:
    state_reader = csv.reader(file,delimiter=",")
    countries = [x[3] for x in state_reader]
    countries = set(countries)
    print(countries)

