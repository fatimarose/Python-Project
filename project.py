import csv
import pandas as pd

#MUST be able to read the data from the spreadsheet
def read_data():

    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data

#read_data()

#MUST collect all of the sales from each month into a single list
def sales_for_each_month():

    data = read_data()

    for d in data:
        print(d['month'], ' £',d['sales'])

#sales_for_each_month()


#MUST output the total sales across all the months
def total_sales():

    data = read_data()

    sales =[]
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    print('Total sales is £{}'.format(total))

#total_sales()


#SHOULD calculate profit/loss
#SHOULD output results to a spreadsheet
def profit_or_loss():
    df = pd.read_csv('sales.csv')

    df['profit or loss'] = df['sales'] - df['expenditure']

    df.to_csv('profit.csv', index=False)

    print(df)

#profit_or_loss()


#SHOULD calculate the average sales
def average_sales_1():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    average = int(total)/len(data)

    print('The average sales is £{}'.format("%.2f" % average))

#average_sales_1()

def average_sales_2():

    df = pd.read_csv('sales.csv')

    mean_sales = df['sales'].mean()

    print('The average sales is £{}'.format("%.2f" % mean_sales))

#average_sales_2()


#SHOULD calculate the months with the highest and lowest sales
def max_min_sales_1():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    print('Maximum sales £', max(sales))
    print('Minimum sales £', min(sales))

#max_min_sales_1()

def max_min_sales_2():
    df = pd.read_csv('sales.csv')

    min_sales = df[df.sales == df.sales.min()]
    max_sales = df[df.sales == df.sales.max()]

    print('Minium sales:\n{}'.format(min_sales))
    print('Maximum sales:\n{}'.format(max_sales))

#max_min_sales_2()

