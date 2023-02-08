from selenium import webdriver
import scrapeGreenhouse


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
jobs = scrapeGreenhouse.getJobs(driver, "https://paxos.com/careers/role")
for job in jobs:
    print(job)

driver.close()
