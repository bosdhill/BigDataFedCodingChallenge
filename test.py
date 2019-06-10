from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

d = webdriver.Chrome()

def display_all_dates():
    d.find_element_by_id('widgetFieldDateRange').click()
    sDate  = d.find_element_by_id('startDate')
    sDate.clear()
    sDate.send_keys('01/01/2019')
    eDate = d.find_element_by_id('endDate')
    eDate.clear()
    eDate.send_keys('06/06/2020')
    d.find_element_by_id('applyBtn').click()
    time.sleep(3)

def print_table():
    try:
        resultsBox = d.find_element_by_id("results_box")
        tbody = resultsBox.find_element_by_tag_name('tbody')
        rows = tbody.find_elements_by_tag_name('tr')
        for row in rows:
            col = row.find_elements_by_tag_name('td')
            print("Date", col[0].text, "Price", col[1].text)
    except:
        close_pop_up()
        print_table()

def close_pop_up():
    d.execute_script("""
    (function() {
        document.getElementsByClassName("popupCloseIcon largeBannerCloser")[0].click();
    })()
""")
    time.sleep(3) # wait for it to dismiss

if __name__ == "__main__":
    d.get('https://www.investing.com/commodities/gold-historical-data')
    time.sleep(2)
    try:
        close_pop_up()
        display_all_dates()
        print_table()
    except:
        close_pop_up()
        display_all_dates()
        print_table()
