# report.py
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        t = (s['name'], s['shares'], prices[s['name']], s['price']-prices[s['name']])
        report.append(t)
    return report


def print_report(report):
    header = ('Name', 'Shares', 'Price', 'Change')
    print(f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')
    print('-'*10, '-'*10, '-'*10, '-'*10)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices    = read_prices(prices_filename)
    report    = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')

# # Calculate the total cost of the portfolio
# total_cost = 0.0
# for s in portfolio:
#     total_cost += s['shares']*s['price']

# print('Total cost', total_cost)

# # Compute the current value of the portfolio
# total_value = 0.0
# for s in portfolio:
#     total_value += s['shares']*prices[s['name']]

# print('Current value', total_value)
# print('Gain', total_value - total_cost)
