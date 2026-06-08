# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 350
}

total_investment = 0

print("Available Stocks:")
for stock in stock_prices:
    print(stock)

num_stocks = int(input("\nHow many stocks do you want to add? "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found!")

print("\n----- Portfolio Summary -----")
print(f"Total Investment Value: ${total_investment}")