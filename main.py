import myDB
import charts


def display_percentage(sorted_dict):
    for i in sorted_dict:
        print(f" {i} => {sorted_dict[i]}%")


def percentage_option():
    while True:
        print('1 => percentage companies prices of your portfolios ')
        print('2 => percentage sectors prices of your portfolios ')
        print('3 => percentage companies cost of your portfolios ')
        print('4 => percentage sectors cost of your portfolios ')
        print('0 => quit')
        print('*' * 100)
        option = int(input('Please, enter your option :'))
        if option == 0:
            print('end of percentage option')
            break
        elif option == 1:
            display_percentage(myDB.percentage_companies_prices())
            print('*' * 100)
        elif option == 2:
            display_percentage(myDB.percentage_sectors_prices())
            print('*' * 100)
        elif option == 3:
            display_percentage(myDB.percentage_companies_cost())
            print('*' * 100)
        elif option == 4:
            display_percentage(myDB.percentage_sectors_cost())
            print('*' * 100)
        else:
            pass


def charts_pie_option():
    while True:
        print('1 => a chart pie percentage companies prices of your portfolios ')
        print('2 => a chart pie percentage sectors prices of your portfolios ')
        print('3 => a chart pie percentage companies cost of your portfolios ')
        print('4 => a chart pie percentage sectors cost of your portfolios ')
        print('0 => quit')
        print('*' * 100)
        option = int(input('Please, enter your option :'))
        if option == 0:
            print('end of percentage option')
            break
        elif option == 1:
            charts.chart_pie_percentage(myDB.percentage_companies_prices())
            print('*' * 100)
        elif option == 2:
            charts.chart_pie_percentage(myDB.percentage_sectors_prices())
            print('*' * 100)
        elif option == 3:
            charts.chart_pie_percentage(myDB.percentage_companies_cost())
            print('*' * 100)
        elif option == 4:
            charts.chart_pie_percentage(myDB.percentage_sectors_cost())
            print('*' * 100)
        else:
            pass


def charts_bar_option():
    while True:
        print('1 => a chart bar percentage companies prices of your portfolios ')
        print('2 => a chart bar percentage sectors prices of your portfolios ')
        print('3 => a chart bar percentage companies cost of your portfolios ')
        print('4 => a chart bar percentage sectors cost of your portfolios ')
        print('0 => quit')
        print('*' * 100)
        option = int(input('Please, enter your option :'))
        if option == 0:
            print('end of percentage option')
            break
        elif option == 1:
            charts.chart_bar_percentage(myDB.percentage_companies_prices())
            print('*' * 100)
        elif option == 2:
            charts.chart_bar_percentage(myDB.percentage_sectors_prices())
            print('*' * 100)
        elif option == 3:
            charts.chart_bar_percentage(myDB.percentage_companies_cost())
            print('*' * 100)
        elif option == 4:
            charts.chart_bar_percentage(myDB.percentage_sectors_cost())
            print('*' * 100)
        else:
            pass


# Define a list of sectors
sectors = ["Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples", "Healthcare",
           "Financials", "Information Technology", "Communication Services", "Utilities", "Real Estate"]
while True:
    print('1 => Add a company.')
    print('2 => delete a company.')
    print(r'3 => Display table')
    print(r'4 => The percentage of statistics')
    print('5 => update a company information.')
    print('6 => display chart pie.')
    print('7 => display chart bar.')
    print('0 => quit')
    print('*' * 100)
    index = int(input('Enter option :'))
    if 0 == index:
        print('The program end.')
        break
    elif 1 == index:
        myDB.insert_company()
        print('*' * 100)
    elif 2 == index:
        myDB.delete_company()
        print('*' * 100)
    elif 3 == index:
        myDB.display()
        print('*' * 100)
    elif 4 == index:
        percentage_option()
    elif 5 == index:
        myDB.update_price()
        myDB.update_information()
        print('*' * 100)
    elif 6 == index:
        charts_pie_option()
        print('*' * 100)
    elif 7 == index:
        charts_bar_option()
        print('*' * 100)
    else:
        pass
