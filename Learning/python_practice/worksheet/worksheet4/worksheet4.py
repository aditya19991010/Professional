from Coursework_shyam.worksheet.worksheet4.CSVProcessor import load_csv, cal_cols,cal_rows, fillna

file = "/home/group_nithya01/PycharmProjects/Work_update/Coursework_shyam/Python_data/Python/titanic.csv"


def main():
    csv = load_csv(file)
    cal_cols(csv)
    cal_rows(csv)
    fillna(csv)

if __name__=="__main__":
    main()