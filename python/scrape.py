from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import dateutil.parser as parser

# Globals and Constants
d = webdriver.Chrome()
GOLD_DATA_URL = "https://www.investing.com/commodities/gold-historical-data"
SILVER_DATA_URL = "https://www.investing.com/commodities/silver-historical-data"
GOLD_DATA_PATH = "data/golddateandprice.csv"
SILVER_DATA_PATH = "data/silverdateandprice.csv"
START_DATE = '01/01/2019'
END_DATE ='06/06/2020'

# Methods
# Enters dates to display data in date range START_DATE to END_DATE
def display_all_dates():
    d.find_element_by_id('widgetFieldDateRange').click()
    d.implicitly_wait(1)
    sDate  = d.find_element_by_id('startDate')
    sDate.clear()
    d.implicitly_wait(1)
    sDate.send_keys(START_DATE)
    eDate = d.find_element_by_id('endDate')
    eDate.clear()
    eDate.send_keys(END_DATE)
    d.implicitly_wait(1)
    d.find_element_by_id('applyBtn').click()
    d.implicitly_wait(2)

# Writes out data table to file at path
def write_table(path):
    try:
        resultsBox = d.find_element_by_id("results_box")
        tbody = resultsBox.find_element_by_tag_name('tbody')
        rows = tbody.find_elements_by_tag_name('tr')
        fp = open(path, "w")
        fp.truncate(0)
        for row in rows:
            col = row.find_elements_by_tag_name('td')
            date = parser.parse(col[0].text)
            fp.write(date.isoformat().split('T')[0] + ","
                + col[1].text.replace(',','') + "\n")
    except:
        close_pop_up()
        write_table(path)

# Closes email pop up banner
def close_pop_up():
    d.implicitly_wait(2)
    d.execute_script("""
    (function() {
        document.getElementsByClassName("popupCloseIcon largeBannerCloser")[0].click();
    })()
    """)
    d.implicitly_wait(2)

# Generates CSV of data retrieved from url and writes it to file at path
def generate_csv(url, path):
    d.get(url)
    d.implicitly_wait(4)
    try:
        close_pop_up()
        display_all_dates()
        write_table(path)
    except:
        close_pop_up()
        display_all_dates()
        write_table(path)

# Main
if __name__ == "__main__":
    print("Generating CSV files...")
    # try:
    generate_csv(GOLD_DATA_URL, GOLD_DATA_PATH)
    generate_csv(SILVER_DATA_URL, SILVER_DATA_PATH)
    print("Successfully generated CSV files!")
    # except:
    #     print("Something went wrong.")

