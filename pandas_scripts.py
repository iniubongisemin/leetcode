import pandas as pd

my_data_set = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}
my_var = pd.DataFrame(my_data_set)
# print(my_var)

# print("Pandas Version", pd.__version__)

"PANDAS SERIES"
"A one-dimensional array holding data of any type like a column in a table"
"e.g Create a Pandas Series from a list"
a = ["a", "b", "c"]
my_var = pd.Series(a)
# print(my_var)

"LABELS"
# print(my_var[0])
"NAMING LABELS"
my_var = pd.Series(a, index=["x", "y", "z"])
# print(my_var)

"ACCESSING AN ITEM BY ITS LABELS"
# print(my_var["x"])


"KEY/VALUE OBJECTS AS SERIES"
calories = {
    "day_one": 420,
    "day_two": 380,
    "day_three": 390,
}
my_var = pd.Series(calories)
# print(my_var)

"GRANULAR CONTROL OVER DATA USED TO FORM A PANDAS SERIES"
my_var = pd.Series(calories, index=["day_one", "day_two"])
# print(my_var)

"DataFrames in PANDAS"
"A Pandas DataFrame is a 2 dimensional data structure e.g array or table with rows & columns"
data = {
    "cal_burnt": [500, 200, 50],
    "exercise_duration": [60, 30, 10],
}
df = pd.DataFrame(data)
# print(df)

"LOCATING A ROW IN A DataFrame"
# print(df.loc[0])
"2 Rows"
"PS: When using [], the result is a Pandas DataFrame"
# print(df.loc[[0, 1]])

"Named Indexes"
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# print(df)

"Locate Named Indexes"
# print(df.loc["day2"])

"LOAD FILES INTO A DATAFRAME"
df = pd.read_csv("data.csv")
# print(df)
# print(df.to_string())

# print(pd.options.display.max_rows)
pd.options.display.max_rows = 500
# print(df)

"Read JSON"
df = pd.read_json("data.json")
# print(df.to_string())

"LOADING PYTHON DICTIONARIES INTO A DataFrame"
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
# print(df)

"ANALYZING DATAFRAMES"
"Viewing Data with head()"
df = pd.read_csv("data.csv")
# print(df.head()) 
# print(df.tail())

"Info about the Data"
# print(df.info())

"DATA CLEANING"
"Cleaning Empty Cells"
df = pd.read_csv("csv_data.csv")
new_df = df.dropna()
# print(new_df.to_string())

"Replace Empty Values"
df = pd.read_csv("data.csv")
new_df = df.fillna(130, inplace = True)
print(new_df)

