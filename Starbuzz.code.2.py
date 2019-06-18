import urllib.request
page = urllib.request.urlopen("https://www.fastfoodmenuprices.com/starbucks-prices/")
text = page.read().decode("utf8")
where_is_price = text.find('"table-press-ori" value="')
start_of_price = where_is_price + 25
end_of_price = where_is_price + 30
price = text[start_of_price : end_of_price]
print("Tall Latte is " + price)