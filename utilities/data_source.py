""" test data for valid login test """
test_valid_login_data = [
    ("admin", "pass", "English (Indian)", "OpenEMR"),
    ("physician", "physician", "English (Indian)", "OpenEMR"),
    ("accountant", "accountant", "English (Indian)", "OpenEMR")
]

test_invalid_login = [["john", "john123", "Dutch", "Invalid username or password"],
                      ["peter", "peter123", "Greek", "Invalid username or password"]]
