import pandas

data = pandas.read_csv("1_2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_count = data["Primary Fur Color"].value_counts()
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [fur_count[0], fur_count[1], fur_count[2]]
}

data = pandas.DataFrame(data_dict)
data.to_csv("1_squirrel_count.csv")
