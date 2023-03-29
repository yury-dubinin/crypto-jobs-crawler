from selenium import webdriver
from companyItem import CompanyItem
from scrapeRecruitee import ScrapeRecruitee


company_list = []
company_list.append(CompanyItem("ramp.network",  "https://metrika.recruitee.com", ScrapeRecruitee, "https://ramp.network", "Payments"))

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

for company in company_list:
    print(company.jobs_url)
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    print(data)

driver.close()
