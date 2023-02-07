from selenium import webdriver
import scrapeLever


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
jobs = scrapeLever.getJobs(driver, "https://jobs.lever.co/tokenmetrics")
for job in jobs:
    print(job)

driver.close()
