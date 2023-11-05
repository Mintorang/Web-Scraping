from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.ebay.co.uk/sch/i.html?_nkw=faulty+ps4+consoles&_sop=12"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

#Get the Items
confused_prices = soup.find_all("span", class_="s-item__price")
num = 1
re_arranged_prices = []
for i in range(60):
        
    x = str(confused_prices[num]).split("-->", 4)
    num += 1
    y = x[2].split("<!-", -3)
    re_arranged_prices.append(y[0])
print(len(re_arranged_prices))
num = 0
for i in range(60):
    re_arranged_prices[num] = float(re_arranged_prices[num].replace("£", ""))
    num +=1
re_arranged_prices.sort()
print(re_arranged_prices)


#Get the links
confused_links = soup.find_all("a", class_="s-item__link")
print(confused_links[0])