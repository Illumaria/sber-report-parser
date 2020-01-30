import ssl
import camelot
import urllib.request as urlrq
from selenium import webdriver

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.sberbank-am.ru/disclosure/fund/etf-sp-500/"

# Set the full path to the geckodriver.exe:
driver = webdriver.Firefox(executable_path='D:\\Work\\geckodriver.exe')
driver.get(url)

driver.find_element_by_link_text("Отчетность за 2019 год").click()

prop_reval_report = driver.find_element_by_partial_link_text("Отчет о приросте").get_attribute("href")
print("Link to the property revaluation report: {0}".format(prop_reval_report))

nav_report = driver.find_element_by_partial_link_text("Справка о стоимости").get_attribute("href")
print("Link to the net asset value report: {0}".format(nav_report), end='\n')

driver.quit()

# Read the file:
prop_reval_tables = camelot.read_pdf(prop_reval_report, process_background=False, pages='1-end', line_scale=45)

# Print parsing statictics:
for x in prop_reval_tables:
    print("{0}: {1}".format(x, x.parsing_report))

# Read the file:
nav_tables = camelot.read_pdf(nav_report, process_background=False, pages='1-end', line_scale=45)

# Print parsing statictics:
for x in nav_tables:
    print("{0}: {1}".format(x, x.parsing_report))

# Visual debugging (if needed):
#plt = camelot.plot(prop_reval_tables[1], kind='text')
#plt = camelot.plot(prop_reval_tables[1], kind='joint')
#plt.show()
# Wait for input when using the plot or the window will close automatically:
#input()

# Export the tables:
prop_reval_tables.export('D://Work//prop_reval.html', f='html', compress=False)
nav_tables.export('D://Work//nav.html', f='html', compress=False)

