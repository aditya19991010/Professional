import pandas as pd

def load_csv(file):
    csv_file = pd.read_csv(file)
    return csv_file

def cal_cols(load_csv):
    len_col = load_csv.shape[1]
    return print(f"Number of columns in the file: ",len_col)


def cal_rows(load_csv):
    len_rows = load_csv.shape[0]
    return print(f"Number of columns in the file: ",len_rows)


def fillna(load_csv):
    check_na = load_csv.isna()
    print(check_na.head())
    uinput = str(input("Enter 'yes/no' to proceed with filling NaN with 0: "))
    if uinput == "yes":
        csv_nona = load_csv.fillna(0)
    elif uinput == "no":
        print("Not filling ")
    return print(csv_nona.head())

