from selenium import webdriver
from companyItem import CompanyItem
from scrapeLever import ScrapeLever


company_list = []
company_list.append(CompanyItem("cere-network",  "https://jobs.lever.co/cere-network", ScrapeLever, "https://cere.network", "Infra"))
company_list.append(CompanyItem("ramp.network",  "https://jobs.lever.co/careers.ramp.network", ScrapeLever, "https://ramp.network", "Payments"))
company_list.append(CompanyItem("ledger",  "https://jobs.lever.co/ledger", ScrapeLever, "https://www.ledger.com", "Wallet"))
company_list.append(CompanyItem("request",  "https://jobs.lever.co/request", ScrapeLever, "https://request.network", "Payments"))
company_list.append(CompanyItem("immutable",  "https://jobs.lever.co/immutable", ScrapeLever, "https://www.immutable.com", "NFT"))
company_list.append(CompanyItem("web3auth",  "https://jobs.lever.co/TorusLabs", ScrapeLever, "https://web3auth.io", "Auth"))

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

for company in company_list:
    print(company.jobs_url)
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    print(data)

driver.close()
