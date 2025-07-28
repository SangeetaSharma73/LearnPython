from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import pandas as pd
import time

# Setup headless browser
options = Options()
options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# Suppress logs
service = Service(log_path='NUL')
driver = webdriver.Chrome(options=options,service=service)

url = "https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y"

driver.get(url)
time.sleep(5)  # Let page load

# Scroll down to load more
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
for _ in range(3):  # scroll a few times to load more data
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(2)

# Scrape RFQs
rfqs = driver.find_elements(By.CSS_SELECTOR, "ul.rfq-card-wrapper li.rfq-item")

data = []
for rfq in rfqs:
    try:
        title = rfq.find_element(By.CLASS_NAME, "title").text
        category = rfq.find_element(By.CLASS_NAME, "category").text
        quantity = rfq.find_element(By.CLASS_NAME, "quantity").text
        posted = rfq.find_element(By.CLASS_NAME, "time").text
        buyer_country = rfq.find_element(By.CLASS_NAME, "country-name").text
    except:
        continue

    data.append({
        "Title": title,
        "Category": category,
        "Quantity": quantity,
        "Posted": posted,
        "Buyer Country": buyer_country
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("alibaba_rfq_data.csv", index=False)

driver.quit()
