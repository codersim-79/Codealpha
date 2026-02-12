# Stock Portfolio Tracker
stocks = {
    "AAPL ":180,
    "TSLA " : 250,
    "GOOGL":140,
    "MSFT":320,
    "AMZN":260,
    "META":300,
    "NFLX":420,
    "NVDA":230,
    "TCS":390,
    "WIPRO":280,
    "HCL":310,
    "IBM":330

}
total_investment =0
print("STOCK PORTFOLIO TRACKER")
print("!---------------------------------------------!")

print("Available Stocks:")
for stock , price in stocks.items():
    print(stock, "\u20B9",price)
while True:
    stock_name =input("Enter the stock name(or 'Done if Stop'): ").upper()
    if stock_name == "DONE" :
        break
    if stock_name in stocks:
        quantity = int(input("Enter the quantity : "))
        total_investment += stocks[stock_name] * quantity 
    else:
        print("Stock not found")

print("Total Investment: ", total_investment)   
print("Thank You! Good Day😊")     
print("!----------------------------------------------!")