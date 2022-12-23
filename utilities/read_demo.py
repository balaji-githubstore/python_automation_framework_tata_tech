""" Will be deleted. Not part of the framework """
import pandas

from utilities import read_data

df = pandas.read_csv(filepath_or_buffer="../test_data/test_valid_login.csv", delimiter=";")

print(df)
print(20 * "-")

print(df.to_string())
print(20 * "-")

""" to read 1 st row"""
print(df.loc[0].tolist())
print(df.loc[0].tolist())
print(list(df.loc[0]))
print(tuple(df.loc[0]))

print(list(df.loc[1]))

""" to read 1st cell  """
print(20 * "-")

print(df.loc[0].tolist()[0])

""" get using column name  """
print(df.get(["password", "username"]))

""" to get the index """
print(df.index)

""" to print all the index """
for i in df.index:
    print(i)
    print(df.loc[i].tolist())
    print(tuple(df.loc[i]))

print(20 * "-")
""" converting each row to list """
for i in df.index:
    print(list(df.loc[i]))

print(20 * "-")
""" converting each row to tuple """
for i in df.index:
    print(tuple(df.loc[i]))

print(20 * "-")

""" converting each row to tuple and then loading to list """
rows = []
for i in df.index:
    print(tuple(df.loc[i]))
    rows.append(tuple(df.loc[i]))

print(rows)

""" converting each row to list and then loading to list - just use values  """
print(20 * "-")
print(df.values.tolist())

""" reading csv file and then converting each to list and then adding to one list"""
print(50 * "-")
df = pandas.read_csv(filepath_or_buffer="../test_data/test_valid_login.csv", delimiter=";")
print(df.values.tolist())

""" reading csv file using method """
print(50 * "-")
list=read_data.get_csv_data("../test_data/test_valid_login.csv")
print(list)