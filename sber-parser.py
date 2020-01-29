import camelot
from selenium import webdriver
import urllib3
import certifi
import requests

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

url = "https://www.sberbank-am.ru/disclosure/fund/etf-sp-500/"

# Указываем полный путь к geckodriver.exe на ПК:
#driver = webdriver.Firefox('D:\\Work\\geckodriver.exe')
driver = webdriver.Firefox(executable_path="D:\\Work\\geckodriver.exe")
driver.get(url)

driver.find_element_by_link_text("Отчетность за 2019 год").click()

href = driver.find_element_by_partial_link_text("Отчет о приросте").get_attribute("href")
print(href)

import urllib.request
import shutil

# Download the file from `url` and save it locally under `file_name`:
with requests.get(href, verify=False) as response, open("temp", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

#driver.quit()

tables = camelot.read_pdf(out_file)

# Link to the source page:
# https://www.sberbank-am.ru/disclosure/fund/etf-sp-500/
# Прирост:
# https://www.sberbank-am.ru/upload/iblock/287/287c6c9433d1ed70b7284b7dab7475e8.pdf
# Стоимость:
# https://www.sberbank-am.ru/upload/iblock/728/7280ae4e0f1938f4539ab4211fbaed73.pdf

# MANDATORY
# Read the file:
#tables = camelot.read_pdf('D://Work//stoimost.pdf', process_background=False, pages='18', line_scale=45)

# See some metrics about read tables:
for x in tables:
    print (x.parsing_report)

# Visual debugging:
#plt = camelot.plot(tables[1], kind='text')
#plt = camelot.plot(tables[1], kind='joint')
#plt.show()

# Wait for input when seeing the plot:
#input()

# MANDATORY
# Writing the tables:
#tables.export('D://Work//test.html', f='html', compress=False)

