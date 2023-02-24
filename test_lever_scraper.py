from selenium import webdriver
from companyItem import CompanyItem
from scrapeLever import ScrapeLever


company_list = []
company_list.append(CompanyItem("ramp.network",  "https://jobs.lever.co/careers.ramp.network", ScrapeLever, "https://ramp.network", "Payments"))
company_list.append(CompanyItem("ledger",  "https://jobs.lever.co/ledger", ScrapeLever, "https://www.ledger.com", "Wallet"))
company_list.append(CompanyItem("request",  "https://jobs.lever.co/request", ScrapeLever, "https://request.network", "Payments"))
company_list.append(CompanyItem("immutable",  "https://jobs.lever.co/immutable", ScrapeLever, "https://www.immutable.com", "NFT"))

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

for company in company_list:
    print(company.jobs_url)
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    print(data)

driver.close()
