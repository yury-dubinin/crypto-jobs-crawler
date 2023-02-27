from selenium import webdriver
from companyItem import CompanyItem
from scrapeGreenhouse import ScrapeGreenhouse


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

company_list = []
company_list.append(CompanyItem("paxos",  "https://paxos.com/careers/role", ScrapeGreenhouse, "https://paxos.com", "Stable Coin"))
company_list.append(CompanyItem("status",  "https://jobs.status.im", ScrapeGreenhouse, "https://status.im","Messanger"))
company_list.append(CompanyItem("digitalasset",  "https://boards.greenhouse.io/digitalasset", ScrapeGreenhouse, "https://www.digitalasset.com","Custody"))
company_list.append(CompanyItem("copperco",  "https://boards.eu.greenhouse.io/copperco", ScrapeGreenhouse, "https://copper.co","Custody"))
company_list.append(CompanyItem("messari",  "https://boards.greenhouse.io/messari", ScrapeGreenhouse, "https://messari.io","Information"))
company_list.append(CompanyItem("layerzerolabs",  "https://boards.greenhouse.io/layerzerolabs", ScrapeGreenhouse, "https://layerzero.network","Infra"))
company_list.append(CompanyItem("jumpcrypto",  "https://boards.greenhouse.io/jumpcrypto", ScrapeGreenhouse, "https://jumpcrypto.com","Infra"))
company_list.append(CompanyItem("oasisnetwork",  "https://boards.greenhouse.io/oasisnetwork", ScrapeGreenhouse, "https://oasisprotocol.org","Protocol"))

for company in company_list:
    print(company.jobs_url)
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    print(data)

driver.close()
