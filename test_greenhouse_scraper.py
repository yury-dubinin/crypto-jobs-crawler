from selenium import webdriver
from companyItem import CompanyItem
from scrapeGreenhouse import ScrapeGreenhouse


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

company_list = []
company_list.append(CompanyItem("paxos",  "https://paxos.com/careers/role", ScrapeGreenhouse, "https://paxos.com", "Stable Coin"))
company_list.append(CompanyItem("status",  "https://jobs.status.im", ScrapeGreenhouse, "https://status.im","Messanger"))
company_list.append(CompanyItem("OKX",  "https://boards.greenhouse.io/OKX", ScrapeGreenhouse, "https://okx.com","Exchange"))
company_list.append(CompanyItem("tron",  "https://boards.greenhouse.io/rainberry", ScrapeGreenhouse, "https://tron.network","Blockchain"))

for company in company_list:
    print(company.jobs_url)
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    print(data)

driver.close()
