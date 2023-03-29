from selenium import webdriver
from scrapeSmartrecruiters import ScrapeSmartrecruiters


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
jobs = ScrapeSmartrecruiters().getJobs(driver, "https://careers.smartrecruiters.com/Swissquote")
for job in jobs:
    print(job)

driver.close()
