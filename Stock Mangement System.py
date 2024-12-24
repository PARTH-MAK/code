import random

class Stock:
    def __init__(self, name, symbol, price):
        self.name = name
        self.symbol=symbol
        self.price = price
        
    def update_price(self, new_price):
        self.price = new_price
        
    def __str__(self):
        return f'{self.name} ({self.symbol}) - ${self.price}'
    
class StockMarket:
    def __init__(self):
        self.stock = {}
        
    def add_stock(self, stock):
        if stock.symbol in self.stock:
            print(f'Stock {stock.symbol} already exists')
        else:
            self.stock[stock.symbol] = stock
            print(f"stock {stock.symbol} added successfully..")
            
    def remove_stock(self,symbol):
        if symbol in self.stock:
            del self.stock[symbol]
            print(f"stock {symbol} removed.")
        else:
            print(f"stock {symbol} does not exist!")
            
    def update_stock_price(self, symbol, new_price):
        if symbol in self.stock:
            self.stock[symbol].update_price(new_price)
            print(f"stock {symbol} price updated to ${new_price}")
        else:
            print(f"stock {symbol} does not exist!")
            
    def get_stock(self, symbol):
        if symbol in self.stock:
            return self.stocks[symbol]
        else:
            print(f"stock {symbol} not found!")
            return None
        
    def list_stocks(self):
        if not self.stocks:
            print("no stocks available in the market!!")
        else:
            for stock in self.stock.values():
                print(stock)
                
class portfolio:
    def __init__(self, owner):
        self.owner = owner
        self.holdings = {}
        self.balance = 100,000
        
    def buy_stock(self, stock, quantity):
        cost = stock.price * quantity
        if cost <= self.balance:
            self.balance -= cost
            if stock.symbol in self.holdings:
                self.holdings[stock.symbol] += quantity
            else:
                self.holdings[stock.symbol] = quantity
            print(f"bought { quantity} shares of { stock.symbol}.remaining balanace: ${self.balance:2f}")
        else:
            print(f"insufficient balance to buy {quantity} shares of {stock.symbol}")
            
    def sell_stock(self, stock, quantity):
        if stock.symbol in self.holdings and self.holdings[stock.symbol] >= quantity:
            self.holdings[stock.symbol] -=quantity
            if self.holdings[stock.symbol] ==0:
                del self.holdings[stock.symbol]
            revenue = stock.price * quantity
            self.balance += revenue
            print(f"Sold {quantity} shares of {stock.symbol}. remaining balance: ${self.balance:.2f}")
        else:
            print (f"you do not own {stock.symbol} or you do not have enough shares to sell!")

    def portfolio_value(self, market):
        value = 0
        for symbol, quantity in self.holdings.items():
            stock = market.get_stock(symbol)
            if stock:
                value += stock.price * quantity
            return value
        
    def __str__(self):
        return f"portfolio of {self.owner} with balance of ${self.balance:.2f}, holding: {self.holdings}"
    
class StockTransactionSystem:
    def __init__(self):
        self.market = StockMarket()
        self.portfolio = {}
        
    def create_portfolio(self, owner_name):
        if owner_name not in self.portfolio:
            self.portfolio[owner_name] = portfolio(owner_name)
            print(f"portfolio for {owner_name} created successfully...")
        else:
            print(f"portfolio for {owner_name} already exists..")
    
    def get_portfolio(self, owner_name):
        return self.portfolio.get(owner_name, None)
    
    def perform_stock_transaction(self):
        while True:
            print("\n--- STOCK EXCHANGE ---")
            print("1.Add stock to market:")
            print("2.Update stock price:")
            print("3.Buy Stock:")
            print("4.Sell stock:")
            print("5.View portfolio:")
            print("6.View market stocks:")
            print("7. Exit:")
            choice = int(input("Enter your choice: "))
            
            if choice ==1:
                name = input("Enter stock name: ")
                symbol = input("Enter stock symbol: ")
                price = float(input("Enter stock price: "))
                stock = Stock(name, symbol, price)
                self.market.add_stock(stock)
            
            elif choice == 2:
                symbol = input("Enter stock symbol: ")
                new_price = float(input("Enter new stock price:"))
                self.market.update_stock_price(symbol, new_price)
                
            elif choice == 3:
                owner = input("Enter your name: ")
                portfolio = self.get_portfolio(owner)
                if portfolio is None:
                    print("Portfolio does not exist!! Creating one now....")
                    self.create_portfolio(owner)
                    portfolio = self.get_portfolio(owner)
                    
                symbol = input("Enter stock symbol to buy: ")
                stock = self.market.get_stock(symbol)
                if stock:
                    quantity = int(input("how many shares of {stock.symbol} do you want to buy? "))
                    portfolio.buy_stock(stock, quantity)
                    
                elif choice ==4:
                    owner = input("Enter your name: ")
                    portfolio = self.get_portfolio(owner)
                    if  portfolio is None:
                        print(" you do not have a portfolio. please create one first. ")
                    else:
                        symbol = input("Enter stock symbol to sell: ")
                        stock = self.market.get_stock(symbol)
                        if stock:
                            quantity = int(input("how many shares of {stock.symbol} do you want to sell?"))
                            portfolio.sell_stock(stock, quantity)
                            
                elif choice ==5:
                    owner = input("Enter your name: ")
                    portfolio = self.get_portfolio(owner)
                    if portfolio:
                        market_stock = portfolio.portfolio_value(self.market)
                        print(f"\n{portfolio}")
                        print(f"Total portfolio value: ${market_stock + portfolio.balance:.2f}")
                    else:
                        print(" No portfolio found.")
                        
                elif choice ==6:
                    self.market.list_stocks()
                    
                elif choice ==7:
                    print("Exit the App...")
                    break
                
                else:
                    print("Invaild choice. please try again.")
                    
if __name__ == "__main__":
    system = StockTransactionSystem()
    
    initial_stock = [
        
        Stock("Apple", "APPl", 200.00),
        Stock("Tesla", "TSL", 150.00),
        Stock("Google", "GOOG", 330.00),
        Stock("Amazon", "AMZ", 250.00),
        Stock("Neflix", "NFX", 300.00),
        Stock("Gold", "GLD", 500.00),
        Stock("Silver", "SLR", 476.00),
        Stock("Patinum", "PTM", 537.00),
        Stock("Nvidia", "NVDA", 238.07),
        Stock("Microsoft", "MS", 546.70),
        
    ]
    
    for stock in initial_stock:
        system.market.add_stock(stock)
        
    system.perform_stock_transaction()
