import re
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_karlancer_scraper(driver_path, price_threshold):
    print(price_threshold) 

    BASE_URL = "https://www.karlancer.com/jobs/programming?category_id=6&page={}"

    OUTPUT = "Karlancer_jobs_data.xlsx"

    service = Service(driver_path)
    driver = webdriver.Firefox(service=service)

    wait = WebDriverWait(driver, 20)

    scraped_urls = set()

    if os.path.exists(OUTPUT):
        df = pd.read_excel(OUTPUT)
        scraped_urls = set(df["URL"])

    page = 1
    data = []

    while True:

        url = BASE_URL.format(page)
        print("Karlancer page:", page)

        driver.get(url)

        try:

            cards = wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "card-hover"))
            )

        except:
            break

        if not cards:
            break

        for card in cards:

            try:

                title_el = card.find_element(By.CSS_SELECTOR, "a")

                title = title_el.text
                url = title_el.get_attribute("href")

                if url in scraped_urls:
                    continue

                price_text = card.find_element(By.XPATH, './/div[contains(text(),"تومان")]').text


                price = int(re.sub(r"\D", "", price_text))

                if price >= price_threshold:

                    record = {
                        "URL": url,
                        "TITLE": title,
                        "PRICE": price
                    }

                    data.append(record)
                    scraped_urls.add(url)

                    if os.path.exists(OUTPUT):

                        old = pd.read_excel(OUTPUT)

                        df = pd.concat([old, pd.DataFrame([record])])

                    else:

                        df = pd.DataFrame([record])

                    df.drop_duplicates("URL").to_excel(OUTPUT, index=False)

                    print("Saved:", title,price)

            except:
                continue

        page += 1

    driver.quit()
