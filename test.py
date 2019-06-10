from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

d = webdriver.Chrome()

def display_all_dates():
    d.find_element_by_id('widgetFieldDateRange').click() #show the date picker
    sDate  = d.find_element_by_id('startDate') # set start date input element into variable
    sDate.clear() #clear existing entry
    sDate.send_keys('01/01/2019') #add custom entry
    eDate = d.find_element_by_id('endDate') #repeat for end date
    eDate.clear()
    eDate.send_keys('06/06/2020')
    d.find_element_by_id('applyBtn').click() #submit changes

def print_table():
    baseTable = d.find_element_by_class_name("genTbl closedTbl historicalTbl")
    print(baseTable)
    for elt in baseTable:
        print(elt)

if __name__ == "__main__":
    d.get('https://www.investing.com/commodities/gold-historical-data')
    time.sleep(25)

    try:
        display_all_dates()
        print_table()
    except:
        print("Error! Could not display dates.")
        print(d.page_source)
        # d.find_element_by_class_name('closePopup').click()
        d.execute_script("""
    (function() {
        document.getElementsByClassName("popupCloseIcon largeBannerCloser")[0].click();
    })()
""")
        time.sleep(3) # wait for it to dismiss
        display_all_dates()
