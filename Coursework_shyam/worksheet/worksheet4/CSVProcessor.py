import pandas as pd

class csv_data:
    def __init__(self, file):
        self.file = file

    file = "/home/ibab/PycharmProjects/Work/Coursework_shyam/Python_data/Python/titanic.csv"
    def load_csv(self):
        self.csv_file = pd.read_csv(self.file)
        return self.csv_file

    def cal_cols(self.csv_file):
        self.len_col = self.csv_data.shape[1]
        return print(f"Number of columns in the file: ",len_col)


    def cal_rows(self.csv_file):
        len_rows = csv_data.shape[0]
        return print(f"Number of columns in the file: ",len_rows)


    def fillna(self.csv_file):
        check_na = self.csv_file.isna()
        print(check_na.head())
        uinput = str(input("Enter 'yes/no' to proceed with filling NaN with 0: "))
        if uinput == "yes":
            csv_nona = self.csv_file.fillna(0)
        elif uinput == "no":
            print("Not filling ")
        return print(csv_nona.head())

