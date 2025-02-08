import pandas

data = pandas.read_csv("squirrel_data.csv")
grey_count = len(data["Primary Fur Color"] == "Grey")
cinnamon_count = len(data["Primary Fur Color"] == "Cinnamon")
black_count = len(data["Primary Fur Color"] == "Black")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squiirel.csv")
