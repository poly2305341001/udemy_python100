import pandas
import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# # print(data)
# # print(type(data))
# # print(data["temp"])
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# # print(data_dict)
# # print(type(data_dict))
#
# temp_list = data["temp"].to_list()
# # print(temp_list)
# # print(type(temp_list))
#
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)
# mean_temp = data["temp"].mean()
# # print(mean_temp)
#
# max_temp = data["temp"].max()
# # print(max_temp)
#
# # TODO get data in columns
# # print(data["temp"])
# # print(data.temp)
#
# # TODO get data in row
# # print(data[data.day == "Monday"])
# #
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# mon_temp_c = monday.temp
# mon_temp_f = mon_temp_c*(9/5) + 32
# # print(mon_temp_f)

# TODO create df from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
print(data_dict)
data.to_csv("new_data.csv")