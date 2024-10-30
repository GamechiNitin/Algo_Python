import pandas as pd
import sys
import os

# Add the Domain folder to the path
base_dir = os.path.dirname(os.path.abspath(__file__))
domain_dir = os.path.join(base_dir, '..', 'Domain')
sys.path.insert(0, domain_dir)

from apimanager import fetch_stock_api
csv_file_path = os.path.join(base_dir, '..', 'data', 'sp_500_stocks.csv')
json_file_path = os.path.join(base_dir, '..', 'data', 'stocks_data.json')

# Load the CSV file into a DataFrame
stocks = pd.read_csv(csv_file_path)
print(stocks)

my_columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
data_rows = []

final_dataframe = pd.DataFrame(columns=my_columns)
for stock in stocks['Ticker'][:5]:
        api_url = f"https://api.example.com/stocks/{stock}"  
        data = fetch_stock_api(fallback_file=json_file_path)
        
        if "stocks" in data:
            for stock_data in data["stocks"]:
                ticker = stock_data.get('Ticker', 'NA')
                # Check if the ticker matches the target ticker
                if ticker == stock:
                    latest_price = stock_data.get('latestPrice', 'NA')
                    market_cap = stock_data.get('marketCap', 'NA')

                    # Append the data to the list
                    data_rows.append([
                        ticker,
                        latest_price,
                        market_cap,
                        'NA' 
                    ])

                    print(f"Ticker: {ticker}, Latest Price: {latest_price}, Market Cap: {market_cap}")
            else:
                print("No 'stocks' key found in the data.")
      

# Create the final DataFrame from the collected data
final_dataframe = pd.DataFrame(data_rows, columns=my_columns)

print(final_dataframe)
