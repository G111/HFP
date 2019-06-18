import urllib.request
page = urllib.request.urlopen("https://www.fastfoodmenuprices.com/starbucks-prices/")
text = page.read().decode("utf8")
price = text[57967:57972]
print("Venti Latte is " + price)