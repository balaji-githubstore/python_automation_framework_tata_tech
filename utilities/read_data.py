import pandas

import config


def get_csv_data(file_name):
    df = pandas.read_csv(filepath_or_buffer=config.test_data_path + file_name, delimiter=";")
    return df.values.tolist()


def get_excel_data(file_name, sheet_name):
    df = pandas.read_excel(io=config.test_data_path + file_name, sheet_name=sheet_name)
    return df.values.tolist()
