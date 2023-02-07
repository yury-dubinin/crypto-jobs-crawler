from selenium import webdriver
import scrapeBinance


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
jobs = scrapeBinance.getJobs(driver, "https://www.binance.com/en/careers/job-openings")
for job in jobs:
    print(job)

driver.close()
