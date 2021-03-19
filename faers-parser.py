
import pandas as pd


def main():
    get_demo_info()


def get_demo_info():
    file = open("./data_from_faers/ASCII/DEMO20Q4.txt")

    # set data in list
    total_info = []

    data = file.readlines()

    for readline in data:
        total_info.append(readline.split("$"))

    # for output in columns_info:
    #     print(output)

    columns_info = total_info[0]
    del total_info[0]
    save_as_csv(total_info, columns_info)


def save_as_csv(total_info, columns_info):
    df = pd.DataFrame(total_info, columns=columns_info)
    df.to_csv("./test3.csv", index=False, encoding='cp949')

main()
