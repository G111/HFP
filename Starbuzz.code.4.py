import urllib.request
import time


def get_price():
    page = urllib.request.urlopen("https://www.fastfoodmenuprices.com/starbucks-prices/")
    text = page.read().decode("utf8")
    where_is_price = text.find('"table-press-ori" value="')
    start_of_price = where_is_price + 26
    end_of_price = where_is_price + 30
    return float((text[start_of_price:end_of_price]))


price_now = input("Do you want to see the price now (Y/N)?")
if price_now == "Y":
    print(get_price())
else:
    price = 99.99
    while price > 4.79:
        print("Action will be shown in 9 seconds")
        time.sleep(9)
        price = get_price()
    print("Buy!")
