import csv
import pandas

# using csv
with open('weather_data.csv') as datas:
    data = csv.reader(datas)
    temp = []
    for i in data:
        if i[1] != "temp":
            temp.append(int(i[1]))

    print(temp)

#using pandas
data = pandas.read_csv('weather_data.csv')

#maximun temparature data
print(data[data.temp == data.temp.max()])

# convert temperature c to f
farenheit = data.temp.max() * (9/5)+32
print(farenheit)

# mean
mean = data.temp.mean()
print(mean)

# avg
temps = data['temp']
avg = sum(temps) / len(temps)
print(avg)
