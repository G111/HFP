import urllib.request
import time

price = 99.99
while price > 4.47:
    time.sleep(900)
    page = urllib.request.urlopen("https://www.fastfoodmenuprices.com/starbucks-prices/")
    text = page.read().decode("utf8")
    where_is_price = text.find('"table-press-ori" value="')
    start_of_price = where_is_price + 26
    end_of_price = where_is_price + 30
    price = float(text[start_of_price: end_of_price])
print("Buy!")