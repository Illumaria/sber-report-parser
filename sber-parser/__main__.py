import ssl
import camelot
import urllib.request as urlrq
from selenium import webdriver

ssl._create_default_https_context = ssl._create_unverified_context

# Set the full path to the driver executable
# or specify the driver location in other way.
# Change to webdriver.Chrome() to use Chrome instead.
#driver = webdriver.Firefox(executable_path='D:\\Work\\geckodriver.exe')
driver = webdriver.Chrome()

url = "https://www.sberbank-am.ru/disclosure/fund/etf-sp-500/"
driver.get(url)

driver.find_element_by_link_text("Отчетность за 2019 год").click()

# Get the file links:
#prop_reval_report = driver.find_element_by_partial_link_text("Отчет о приросте").get_attribute("href")
# Uncomment the next line for debugging:
#print("Link to the property revaluation report: {0}".format(prop_reval_report))
nav_report = driver.find_element_by_partial_link_text("Справка о стоимости").get_attribute("href")
# Uncomment the next line for debugging:
#print("Link to the net asset value report: {0}".format(nav_report), end='\n')

# Quit the driver since we don't need it anymore:
driver.quit()

# Read the files:
#prop_reval_tables = camelot.read_pdf(prop_reval_report, process_background=False, pages='1-end', line_scale=45)

# Print parsing statictics (uncomment if needed):
#for x in prop_reval_tables:
#    print(x.parsing_report)

nav_tables = camelot.read_pdf(nav_report, process_background=False, pages='4-end', line_scale=45)

#for x in nav_tables:
#    print(x.parsing_report)

# Visual debugging (if needed):
#plt = camelot.plot(prop_reval_tables[1], kind='text')
#plt = camelot.plot(prop_reval_tables[1], kind='joint')
#plt.show()
# Wait for input when using the plot or the window will close automatically:
#input()

# Export all tables as HTML files at the path specified.
# Alternative output formats: f='json', f='excel', f='html' or f='sqlite'
#prop_reval_tables.export('D://Work//prop_reval.html', f='html', compress=False)
#nav_tables.export('D://Work//nav.html', f='html', compress=False)
for x in range(len(nav_tables)):
    print(nav_tables[x].df, sep='\n\n')