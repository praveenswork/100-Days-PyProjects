import json

data_obj = {"obj":{
    "name":"praveen",
    "age":19,
}}
new_data = {"greet":{
    "name":"morning",
    "age":7,
}}
try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)

except FileNotFoundError:
        with open ("data.json", "w") as data_file:
         json.dump(data_obj,data_file,indent=4)

else:
        data.update(new_data)

        with open ("data.json", "w") as data_file:
            datas = json.dump(data,data_file,indent=4)
finally:
        print("end")
    

    