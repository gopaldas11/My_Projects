# import csv
#
# from sqlalchemy import column
#
# with open("./002 weather-data.csv") as csvfile:
#     reader = csv.reader(csvfile)
#     temprature = []
#     for row in reader:
#         if row[1] != "temp":
#             temprature.append(int(row[1]))
#     print(temprature)
import pandas

#data = pandas.read_csv("002 weather-data.csv")

#temp_list = data["temp"].to_list()
#print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_f = monday_temp * 9/5 + 32
# print(monday_f)

# dict_data = {
#     "students": ["Gopal","Niloy","Nayon"],
#     "marks": [67,56,55]
# }
# daya = pandas.DataFrame(dict_data)
# daya.to_csv("dict to csv.csv")

data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data-2018.csv")
gray_sqrl_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_sqrl_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sqrl_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_sqrl_count)
# print(Cinnamon_sqrl_count)
# print(black_sqrl_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sqrl_count, Cinnamon_sqrl_count, black_sqrl_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Fur Color and Count.csv")



































