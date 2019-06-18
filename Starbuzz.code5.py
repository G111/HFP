import urllib.request
import time

headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36'
}

def send_to_twitter(msg):

    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                                  "https://twitter.com", "ibrahimakcivan@gmail.com", "07&4jT0OwjakAgaAGKUz")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    parameters = urllib.parse.urlencode({'status' : msg})
    resp = urllib.request.urlopen("https://api.twitter.com/1.1/statuses/update.json", parameters.encode('utf-8'))
    resp.read()

def get_price():
    page = urllib.request.urlopen("https://www.fastfoodmenuprices.com/starbucks-prices/")
    text = page.read().decode("utf8")
    where_is_price = text.find('"table-press-ori" value="')
    start_of_price = where_is_price + 26
    end_of_price = where_is_price + 30
    return float((text[start_of_price:end_of_price]))

price_now = input("Do you want to see the price now (Y/N)?")
if price_now == "Y":
    send_to_twitter(get_price())
else:
    price = 99.99
    while price > 4.79:
        print("Action will be shown in 9 seconds")
        time.sleep(9)
        price = get_price()
    send_to_twitter("Buy!")