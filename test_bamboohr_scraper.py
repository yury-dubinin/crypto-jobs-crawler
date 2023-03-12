from selenium import webdriver
from companyItem import CompanyItem
from scrape_bamboohr import ScrapeBamboohr


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
company_list = []
company_list.append(CompanyItem('web3', 'https://web3.bamboohr.com/jobs', ScrapeBamboohr, 'https://web3.foundation', 'web3'))
company_list.append(CompanyItem('dappradar', 'https://dappradar.bamboohr.com/careers', ScrapeBamboohr, 'https://dappradar.com', 'Exchange & NFT'))
company_list.append(CompanyItem("cexio", "https://cexio.bamboohr.com/jobs", ScrapeBamboohr, "https://cex.io", "Exchange"))
company_list.append(CompanyItem("chainstack", "https://chainstack.bamboohr.com/jobs", ScrapeBamboohr, "https://chainstack.com", "Infra"))

for company in company_list:
    print(company.jobs_url)
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    print(data)

driver.close()
