import pandas
import csv
import os

# tables =pandas.read_html('https://www.argaam.com/en/monitors/market-analytics/3/8-28-2023/8-29-2023/0/9') tables =
# pandas.read_html('https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch/!ut/p/z1
# /04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziTR3NDIw8LAz8LVxcnA0C3bwtPLwM_I0MzMz1w1EVGAQHmAIVBPga-xgEGbgbmOlHEaPfAAdwNCCsPwpNia
# -7mUGgn2Ogv5G5qYFBsBG6AixOBCvA44bgxCL9gtzQCIPMgHQAVrLIOQ!!/dz/d5/L0lHSkovd0RNQUZrQUVnQSEhLzROVkUvZW4!/')


# print(type(tables[0]))

# print(len(tables))

temp = 'temp.csv'
file_stack = 'file_stack.csv'

sectors = ['Energy', 'Materials', 'Capital Goods', 'Commercial & Professional', 'Transportation',
           'Consumer Durables & Apparel', 'Consumer Services', 'Media and Entertainment', 'Retailing',
           'Food & Staples Retailing', 'Food & Beverages', 'Health Care Equipment', 'Pharma, Biotech & Life Sciences',
           'Banks', 'Diversified Financials', 'Insurance', 'Telecommunication Services', 'Utilities', 'REITs',
           'Real Estate Mgmt', 'Software & Services', 'Index Funds']


def only_two_word(text):
    return " ".join(text.split()[0:2])


def update_data():
    tables = pandas.read_html('https://www.argaam.com/en/company/companies-prices')

    if os.path.exists(file_stack):
        os.remove(file_stack)

    for table, sector in zip(tables[1::], sectors):
        table.to_csv(temp, index=False)
        with open(temp) as csv_file:
            if table is not tables[1]:
                next(csv_file)
            data = csv.reader(csv_file)
            for fetch in data:
                fetch[2] = sector
                with open(file_stack, 'a') as csv_file_w:
                    csv.writer(csv_file_w).writerow(fetch)


def get_column(option):
    list_data = []
    with open(file_stack) as csv_file:
        data = csv.reader(csv_file)
        next(csv_file)
        for fetch in data:
            list_data.append(fetch[option])

    return list_data


def get_header():
    list_data = []
    with open(file_stack) as csv_file:
        data = csv.reader(csv_file)
        for fetch in data:
            list_data.append(fetch)
    return list_data[0]


def get_data():
    list_data = []
    with open(file_stack) as csv_file:
        data = csv.reader(csv_file)
        next(csv_file)
        for fetch in data:
            list_data.append(fetch)

    return list_data


def dict_database():
    list_dict_data = []
    stack = {
        'symbol': '',
        'company': '',
        'price': 0,
        'sector': ''

    }

    for fetch in get_data():
        stack['symbol'] = int(fetch[0])
        stack['company'] = only_two_word(fetch[1])
        stack['price'] = float(fetch[5])
        stack['sector'] = fetch[2]

        list_dict_data.append(stack.copy())

    return list_dict_data

