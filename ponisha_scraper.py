import re
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_ponisha_scraper(driver_path, price_threshold):

    BASE_URL = "https://ponisha.ir/search/projects?page={}&order=approved_at%7Cdesc&category=1&promotion=-&filterByProjectStatus=open"
    OUTPUT = "Ponisha_jobs_data.xlsx"

    service = Service(driver_path)
    driver = webdriver.Firefox(service=service)

    wait = WebDriverWait(driver, 20)

    seen_urls = set()
    data = []

    if os.path.exists(OUTPUT):
        df = pd.read_excel(OUTPUT)
        seen_urls = set(df["URL"])
        data = df.to_dict("records")

    page = 1

    while True:

        url = BASE_URL.format(page)
        print("Ponisha page:", page)

        driver.get(url)

        try:
            projects = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//article"))
            )
        except:
            break

        if not projects:
            break

        for p in projects:

            try:

                url = p.find_element(By.CSS_SELECTOR, "a[href*='/project/']").get_attribute("href")

                if url in seen_urls:
                    continue

                title = p.find_element(By.CSS_SELECTOR, "span.MuiTypography-h4").text

                budget_text = p.text

                match = re.search(r"([\d,]+)\s*تومان", budget_text)

                if not match:
                    continue

                price = int(match.group(1).replace(",", ""))

                if price >= price_threshold:

                    record = {
                        "URL": url,
                        "SUBJECT": title,
                        "PRICE": price
                    }

                    data.append(record)
                    seen_urls.add(url)

                    pd.DataFrame(data).to_excel(OUTPUT, index=False)

                    print("Saved:", title)

            except:
                continue

        page += 1

    driver.quit()
