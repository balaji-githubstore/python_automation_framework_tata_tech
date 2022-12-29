""" test data for valid login test """
import config
from utilities import read_data
from importlib import import_module

# d=import_module('py-src')
# module_name = __import__('py-src')
from python_code import demo1

print(module_name.demo1.a)

test_valid_login_data = [
    ("admin", "pass", "English (Indian)", "OpenEMR"),
    ("physician", "physician", "English (Indian)", "OpenEMR"),
    ("accountant", "accountant", "English (Indian)", "OpenEMR")
]

test_invalid_login = [["john", "john123", "Dutch", "Invalid username or password"],
                      ["peter", "peter123", "Greek", "Invalid username or password"]]


test_valid_login_data_csv = read_data.get_csv_data("test_valid_login.csv")

test_valid_login_data_excel = read_data.get_excel_data("open_emr_data.xlsx", "test_valid_login")

print(config.test_data_path)


