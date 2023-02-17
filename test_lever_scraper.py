from selenium import webdriver
from scrapeLever import ScrapeLever


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
jobs = ScrapeLever().getJobs(driver, "https://jobs.lever.co/subspacelabs")
for job in jobs:
    print(job)

driver.close()
