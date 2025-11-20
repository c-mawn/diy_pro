import requests
import urllib.parse

# Scrape.do API token
TOKEN = "3215b4ff8af24f7dbfaaad397ba39371e56ef89211c"

# Updated eBay product URL
target_url = "https://www.ebay.com/itm/125575167955"
encoded_url = urllib.parse.quote_plus(target_url)

# Scrape.do API endpoint
api_url = f"https://api.scrape.do/?token={TOKEN}&url={encoded_url}&geocode=us"

response = requests.get(api_url)

print(response.status_code)
