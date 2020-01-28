import camelot
import urllib
import requests

from bs4 import BeautifulSoup, SoupStrainer
import requests

#url = "https://www.python.org/downloads/"
url = "https://www.sberbank-am.ru/disclosure/fund/etf-sp-500/"

page = requests.get(url, verify=False)
print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")

links = soup.find_all('a', class_='', text="Отчетность за 2019 год")
print(links)

#for i in range(len(links))
#    if links[i].find()

#for link in soup.find_all('a', class_='file'):
#    print(link.get('href'))

# Downloading the file:
# https://www.sberbank-am.ru/disclosure/fund/etf-sp-500/
# Прирост:
# https://www.sberbank-am.ru/upload/iblock/287/287c6c9433d1ed70b7284b7dab7475e8.pdf
# Стоимость:
# https://www.sberbank-am.ru/upload/iblock/728/7280ae4e0f1938f4539ab4211fbaed73.pdf
#with urllib.request.urlopen('https://www.sberbank-am.ru/disclosure/fund/etf-sp-500/') as response:
#   html = response.read()

# Mandatory (read the file):
#tables = camelot.read_pdf('D://Work//stoimost.pdf', process_background=False, pages='18', line_scale=45)

# See some metrics about read tables:
#for x in tables:
#    print (x.parsing_report)

# Visual debugging:
#plt = camelot.plot(tables[1], kind='text')
#plt = camelot.plot(tables[1], kind='joint')
#plt.show()

# Wait for input when seeing the plot:
#input()

# Mandatory (writing the tables):
#tables.export('D://Work//test.html', f='html', compress=False)

