import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
# print(data.columns)

fur_color_col = data["Primary Fur Color"]
gray_num = fur_color_col[fur_color_col == "Gray"].size
cinnamon_num = fur_color_col[fur_color_col == "Cinnamon"].size
black_num = fur_color_col[fur_color_col == "Black"].size

squirrel_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_num, cinnamon_num, black_num],
}

new_df = pd.DataFrame(squirrel_color_dict)
print(new_df)
new_df.to_csv("squirrel_count.csv")

