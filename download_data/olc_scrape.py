from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import time

start_date = date(2006, 10, 10)
end_date = date(2024, 9, 30)

date_ranges = []

current_start = start_date
while current_start <= end_date:
    if current_start.day != 1:
        # For the first range starting on the 10th
        current_end = date(current_start.year, current_start.month, 1) + relativedelta(months=1) - timedelta(days=1)
    else:
        # For all other ranges
        current_end = current_start + relativedelta(months=1) - timedelta(days=1)
    
    if current_end > end_date:
        current_end = end_date
    
    date_ranges.append([current_start, current_end])
    
    current_start = current_end + timedelta(days=1)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

print(len(date_ranges))

for date in date_ranges:
    driver.get(f"https://www.onlinecontest.org/olc-3.0/gliding/finder.html?st=olc&c=C0&sr=AU&cc=&aa=&pi=&ap=&sdt={date[0]}&edt={date[1]}&sedte=&sedts=&mp=")
    xpath_button = '//*[@id="OLCcontentBlock"]/div/div[1]/div/div/div[3]/div[1]/button[3]'
    time.sleep(4)

    button = driver.find_element(By.XPATH, value=xpath_button)
    button.send_keys(Keys.ENTER)
    time.sleep(2)

    driver.quit()



 