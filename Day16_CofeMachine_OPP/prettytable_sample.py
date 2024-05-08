from prettytable import PrettyTable

table =PrettyTable()
table.field_names=['name','regno','class']
table.add_rows([
                ["Praveen",22107045,"BSC IT"],
                ["Nithees",22107041,"BSC IT"],
                ["Dharshan",22107015,"BSC IT"],
                ["Elango",22107019,"BSC IT"],
                ["Kalyan",22107025,"BSC IT"],
                ["sibi",22107054,"BSC IT"],
                ["Mahesh",22107034,"BSC IT"]
               ])


print(table.get_string(sortby="regno"))
from prettytable.colortable import ColorTable, Themes

table = ColorTable(theme=Themes.OCEAN)
table.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])

print(table)