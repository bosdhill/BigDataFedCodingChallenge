from selenium import webdriver
import dateutil.parser as date_parser
import argparse

# Globals and Constants
GOLD_DATA_URL = "https://www.investing.com/commodities/gold-historical-data"
SILVER_DATA_URL = "https://www.investing.com/commodities/silver-historical-data"
GOLD_DATA_PATH = "data/golddateandprice.csv"
SILVER_DATA_PATH = "data/silverdateandprice.csv"
START_DATE = '01/01/2019'
END_DATE ='06/06/2020'
global driver

# Methods
# Enters dates to display data in date range START_DATE to END_DATE
def display_all_dates():
    driver.find_element_by_id('widgetFieldDateRange').click()
    driver.implicitly_wait(1)
    sDate = driver.find_element_by_id('startDate')
    sDate.clear()
    sDate.send_keys(START_DATE)
    eDate = driver.find_element_by_id('endDate')
    eDate.clear()
    eDate.send_keys(END_DATE)
    driver.implicitly_wait(1)
    driver.find_element_by_id('applyBtn').click()
    driver.implicitly_wait(2)

# Scrapes and writes out data table to file at path
def write_table(path):
    try:
        resultsBox = driver.find_element_by_id("results_box")
        tbody = resultsBox.find_element_by_tag_name('tbody')
        rows = tbody.find_elements_by_tag_name('tr')
        fp = open(path, "w")
        fp.truncate(0)
        for row in rows:
            col = row.find_elements_by_tag_name('td')
            date = date_parser.parse(col[0].text)
            fp.write(date.isoformat().split('T')[0] + ","
                + col[1].text.replace(',','') + "\n")
        fp.close()
        print(f"Wrote to {path}\n")
    except:
        close_pop_up()
        write_table(path)

# Closes email pop up banner
def close_pop_up():
    print("\tClosing pop up banner...\n")
    driver.implicitly_wait(2)
    try:
        driver.execute_script("""
        (function() {
            document.getElementsByClassName("popupCloseIcon largeBannerCloser")[0].click();
        })()
        """)
    except:
        pass
    driver.implicitly_wait(2)

# Generates CSV of data retrieved from url and writes it to file at path
def generate_csv(url, path):
    print(f"\tScraping from {url}...")
    driver.get(url)
    driver.implicitly_wait(4)
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
    global driver
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--driver",
                        help="The path to the chrome driver executable",
                        required=True)
    args = parser.parse_args()
    driver = webdriver.Chrome(args.driver)
    print("Generating CSV files...\n")
    try:
        generate_csv(GOLD_DATA_URL, GOLD_DATA_PATH)
        generate_csv(SILVER_DATA_URL, SILVER_DATA_PATH)
        print("Successfully generated CSV files!")
    except:
        print("Oh no! Something went wrong.")