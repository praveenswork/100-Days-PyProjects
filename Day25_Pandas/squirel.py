import pandas

data = pandas.read_csv('squirrel_data.csv')


black_squirrel = (len(data[data['Primary Fur Color'] == 'Black']))
red_squirrel = (len(data[data['Primary Fur Color'] == 'Cinnamon']))
gray_squirrel = (len(data[data['Primary Fur Color'] == 'Gray']))

dict_1 = {
    "colors": ["Black", "Cinnamon", "Gray "],
    "count": [black_squirrel, red_squirrel, gray_squirrel]
    }

df = pandas.DataFrame(dict_1)
print(df)
df.to_csv('squirrel_count.csv')