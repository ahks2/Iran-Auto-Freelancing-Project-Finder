import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

files = ['Ponisha_jobs_data.xlsx', 'Karlancer_jobs_data.xlsx']

def open_urls():

    service = Service(executable_path=r"C:\Users\User\Downloads\Compressed\geckodriver.exe")
    driver = webdriver.Firefox(service=service)

    
    first_url = True
    
    for file in files:
        try:
            df = pd.read_excel(file)
            urls = df.iloc[:, 0].dropna().tolist()
            
            for url in urls:
                if first_url:
                    driver.get(url)
                    first_url = False
                else:
                    driver.execute_script(f"window.open('{url}', '_blank');")
                    time.sleep(0.5)
            
            print(f"URLs from {file} opened successfully.")
            
        except Exception as e:
            print(f"Error processing {file}: {e}")



if __name__ == "__main__":
    open_urls()
