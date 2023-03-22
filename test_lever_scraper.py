from selenium import webdriver
from companyItem import CompanyItem
from scrapeLever import ScrapeLever


company_list = []
company_list.append(CompanyItem('fuellabs', 'https://jobs.lever.co/fuellabs', ScrapeLever, 'https://www.fuel.network/', 'Blockchain'))
company_list.append(
    CompanyItem("Luxor", "https://jobs.lever.co/LuxorTechnology", ScrapeLever, "https://www.luxor.tech", "Mining"))
company_list.append(
    CompanyItem("anchorage", "https://jobs.lever.co/anchorage", ScrapeLever, "https://www.anchorage.com", "Trading"))
company_list.append(
    CompanyItem("biconomy", "https://jobs.lever.co/biconomy", ScrapeLever, "https://www.biconomy.io", "Infra"))
company_list.append(
    CompanyItem("kraken", "https://jobs.lever.co/kraken", ScrapeLever, "https://kraken.com", "Exchange"))
company_list.append(
    CompanyItem("chainlink", "https://jobs.lever.co/chainlink", ScrapeLever, "https://chain.link", "Blockchain"))
company_list.append(CompanyItem("hiro",  "https://jobs.lever.co/hiro", ScrapeLever, "https://www.hiro.so", "Infra"))
company_list.append(CompanyItem("kaiko",  "https://jobs.eu.lever.co/kaiko", ScrapeLever, "https://www.kaiko.com", "Data"))
company_list.append(CompanyItem("tessera",  "https://jobs.lever.co/ftc", ScrapeLever, "https://tessera.co", "NFT"))
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
    for entry in data:
        print(entry)

driver.close()
