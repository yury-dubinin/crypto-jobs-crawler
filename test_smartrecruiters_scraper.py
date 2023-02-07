from selenium import webdriver
import scrapeSmartrecruiters


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
jobs = scrapeSmartrecruiters.getJobs(driver, "https://careers.smartrecruiters.com/Swissquote")
for job in jobs:
    print(job)

driver.close()
