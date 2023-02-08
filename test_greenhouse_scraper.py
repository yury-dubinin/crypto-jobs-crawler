from selenium import webdriver
import scrapeGreenhouse


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
jobs = scrapeGreenhouse.getJobs(driver, "https://boards.greenhouse.io/dfinity")
for job in jobs:
    print(job)

driver.close()
