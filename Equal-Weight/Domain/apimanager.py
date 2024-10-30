import requests
import json

def fetch_stock_api(api_url=None, fallback_file=None):
    """Fetch stock data from the API or load local data if the API call fails."""
    # Define a default API URL if not provided
    if api_url is None:
        print("Hererrr")
        print(fallback_file)
        with open(fallback_file, 'r') as json_file:
            return json.load(json_file)

  
    # try:
    #     response = requests.get(api_url)
    #     response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
    #     return response.json()  # Parse the JSON response
    # except (requests.RequestException, json.JSONDecodeError) as e:
    #     print(f"API request failed: {e}. Loading local JSON data instead.")
    #     # Fallback to loading local JSON data
    #     with open(fallback_file, 'r') as json_file:
    #         return json.load(json_file)
