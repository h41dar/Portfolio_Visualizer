import mysql.connector as conn
import exteact_data as ex


def get_company_name(symbol):
    for fetch in ex.dict_database():
        if fetch['symbol'] == symbol:
            return fetch['company']


def get_company_price(symbol):
    for fetch in ex.dict_database():
        if fetch['symbol'] == symbol:
            return fetch['price']


def get_company_sector(symbol):
    for fetch in ex.dict_database():
        if fetch['symbol'] == symbol:
            return fetch['sector']


def update_price():
    mycursor.execute("SELECT symbol , amount FROM stock")

    myresult = mycursor.fetchall()

    for k, v in myresult:
        sql = f"UPDATE stock SET price = '{get_company_price(k) * v}' WHERE symbol = '{k}'"
        mycursor.execute(sql)
        stockDB.commit()


def buy_stack():
    symbol = int(input('Enter symbol number :'))

    mycursor.execute("SELECT symbol FROM stock")

    myresult = mycursor.fetchall()

    mylist = []

    for index in myresult:
        mylist.append(index[0])

    if symbol in mylist:
        amount = int(input('Enter the amount stack you bought:'))
        cost = float(input('Enter the cost stack you bought'))
        for fetch in to_dict():
            if fetch['symbol'] == symbol:
                new_info = fetch
                break
        new_info['amount'] = new_info['amount']+ amount
        new_info['cost'] = new_info['cost'] + cost
        new_info['price'] = new_info['price'] + get_company_price(symbol) * amount

        for key , value in new_info.items():
            sql = f"UPDATE stock SET {key} = '{value}' WHERE symbol = '{symbol}'"
            mycursor.execute(sql)
            stockDB.commit()

    else:
        print(f'there is not any a company with this symbol => {symbol}')


def to_dict():
    mycursor.execute("SELECT * FROM stock")

    myresult = mycursor.fetchall()

    dict_database = {
        'symbol': 0,
        'company': '',
        'amount': 0,
        'cost': 0,
        'price':0,
        'sector': ''
    }
    dict_database_list = []
    for index in myresult:
        dict_database['symbol'] = index[0]
        dict_database['company'] = index[1]
        dict_database['amount'] = index[2]
        dict_database['cost'] = index[3]
        dict_database['price'] = index[4]
        dict_database['sector'] = index[5]


        dict_database_list.append(dict_database.copy())
    return dict_database_list


def insert_company():
    symbol = int(input('Enter the symbol of stock company :'))
    company = get_company_name(symbol)

    sector = get_company_sector(symbol)

    cost = float(input(f'Enter the cost of {company} :'))

    amount = int(input(f'Enter the number of stock {company} :'))

    price = get_company_price(symbol) * amount

    sql = "INSERT INTO stock (symbol, company, amount, cost, price , sector) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (symbol, company, amount, cost, price, sector)
    mycursor.execute(sql, val)

    stockDB.commit()


def delete_company():
    company = input('Enter a company name :')

    sql = f"DELETE FROM stock WHERE company = '{company}'"

    mycursor.execute(sql)

    stockDB.commit()


def update_information():
    company = input('Enter a company name :')
    sql = ''
    while True:
        print('1 => update cost ')
        print('2 => update amount ')
        print('3 => update price ')
        print('4 => update symbol ')
        print('0 => quit ')
        option = int(input('Enter your option: '))
        if 0 == option:
            print('the function end ')
            break
        elif 1 == option:
            cost = float(input(f'Enter the cost of {company} :'))
            sql = f"UPDATE stock SET cost = '{cost}' WHERE company = '{company}'"
        elif 2 == option:
            amount = int(input(f'Enter the number of stock {company} :'))
            sql = f"UPDATE stock SET amount = '{amount}' WHERE company = '{company}'"
        elif 3 == option:
            price = float(input(f'Enter the price of {company} :'))
            sql = f"UPDATE stock SET price = '{price}' WHERE company = '{company}'"
        elif 4 == option:
            symbol = int(input(f'Enter the symbol of {company} :'))
            sql = f"UPDATE stock SET symbol = '{symbol}' WHERE company = '{company}'"
        mycursor.execute(sql)
        stockDB.commit()


def percentage_companies_prices():
    mycursor.execute("SELECT company , price FROM stock")

    myresult = mycursor.fetchall()
    total = 0
    for i in myresult:
        total += i[1]

    percentage = dict(myresult)

    for key, value in percentage.items():
        percentage[key] = round((value * 100) / total, 2)

    sorted_dict = dict(sorted(percentage.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict


def percentage_companies_cost():
    mycursor.execute("SELECT company , cost FROM stock")

    myresult = mycursor.fetchall()
    total = 0
    for i in myresult:
        total += i[1]

    percentage = dict(myresult)

    for key, value in percentage.items():
        percentage[key] = round((value * 100) / total, 2)

    sorted_dict = dict(sorted(percentage.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict


def percentage_sectors_prices():
    mycursor.execute("SELECT sector , price FROM stock")

    myresult = mycursor.fetchall()
    total = 0
    for i in myresult:
        total += i[1]

    my_dict = {}
    for k, v in myresult:
        my_dict[k] = my_dict.get(k, 0) + v

    for key, value in my_dict.items():
        my_dict[key] = round((value * 100) / total, 2)

    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict


def percentage_sectors_cost():
    mycursor.execute("SELECT sector , cost FROM stock")

    myresult = mycursor.fetchall()
    total = 0
    for i in myresult:
        total += i[1]

    my_dict = {}
    for k, v in myresult:
        my_dict[k] = my_dict.get(k, 0) + v

    for key, value in my_dict.items():
        my_dict[key] = round((value * 100) / total, 2)

    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict


def display():
    mycursor.execute("SELECT * FROM stock")

    myresult = mycursor.fetchall()

    # The following code snippet has been directly copied and pasted from ChatGPT.
    data = list(myresult)
    # Calculate the maximum width of each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # Print the table
    for row in data:
        formatted_row = [f"{item:{width}}" for item, width in zip(row, column_widths)]
        print(" | ".join(formatted_row))


stockDB = conn.connect(
    host="localhost",
    user="root",
    password="???????????",
    database="stockDB"
)

mycursor = stockDB.cursor()


