
import requests

from bs4 import BeautifulSoup

symbol = input("Enter the Stock Symbol: ")

url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + symbol

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
container = soup.find(id="responseDiv").getText().strip().split(":")

for item in container:
    if 'lastPrice' in item:
        index = container.index(item)+1

latestprice = container[index].split('"')

for item in container:
    if 'open' in item:
        index = container.index(item)+1

open = container[index].split('"')

for item in container:
    if 'dayHigh' in item:
        index = container.index(item)+1

high = container[index].split('"')

for item in container:
    if 'dayLow' in item:
        index = container.index(item)+1

low = container[index].split('"')

for item in container:
    if 'totalTradedVolume' in item:
        index = container.index(item)+1

volume = container[index].split('"')

print("Open: "+open[1])
print("High: "+high[1])
print("Low : "+low[1])
print("LTP : "+latestprice[1])
print("Vol : "+volume[1])

