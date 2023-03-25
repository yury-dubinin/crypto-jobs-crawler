from selenium import webdriver
from companyItem import CompanyItem
from scrapeGreenhouse import ScrapeGreenhouse


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

company_list = []
company_list.append(CompanyItem('stellar', 'https://boards.greenhouse.io/stellar', ScrapeGreenhouse, 'https://stellar.org', 'Blockchain'))
company_list.append(CompanyItem('okcoin', 'https://boards.greenhouse.io/okcoin', ScrapeGreenhouse, 'https://www.okcoin.com', 'Exchange'))
company_list.append(CompanyItem("solanafoundation",  "https://boards.greenhouse.io/solanafoundation", ScrapeGreenhouse, "https://solana.org", "Blockchain"))
company_list.append(CompanyItem("worldcoinorg",  "https://boards.greenhouse.io/worldcoinorg", ScrapeGreenhouse, "https://worldcoin.org", "Blockchain"))
company_list.append(CompanyItem("edgeandnode",  "https://boards.greenhouse.io/edgeandnode", ScrapeGreenhouse, "https://edgeandnode.com", "Infra"))
company_list.append(CompanyItem("clearmatics",  "https://boards.greenhouse.io/clearmatics", ScrapeGreenhouse, "https://www.clearmatics.com", "Protocol"))
company_list.append(CompanyItem("aztec",  "https://boards.eu.greenhouse.io/aztec", ScrapeGreenhouse, "https://aztec.network", "Protocol"))
company_list.append(CompanyItem("avalabs",  "https://boards.greenhouse.io/avalabs", ScrapeGreenhouse, "https://www.avalabs.org", "Blockchain"))
company_list.append(CompanyItem("galaxydigitalservices", "https://boards.greenhouse.io/galaxydigitalservices", ScrapeGreenhouse, "https://www.galaxy.com", 'Trading'))
company_list.append(CompanyItem("bittrex", "https://boards.greenhouse.io/bittrex", ScrapeGreenhouse, "https://global.bittrex.com", 'Exchange'))
company_list.append(CompanyItem("bitcoin", "https://www.bitcoin.com/jobs/#joblist", ScrapeGreenhouse, "https://www.bitcoin.com", 'Exchange'))
company_list.append(CompanyItem("EigenLabs", "https://boards.greenhouse.io/layrlabs", ScrapeGreenhouse, "https://www.v1.eigenlayer.xyz", "Infra"))
company_list.append(CompanyItem("kadena", "https://boards.greenhouse.io/kadenallc", ScrapeGreenhouse, "https://kadena.io", "PoW chain"))
company_list.append(CompanyItem("poap", "https://boards.greenhouse.io/poaptheproofofattendanceprotocol", ScrapeGreenhouse, "https://poap.xyz", "Protocol"))
company_list.append(CompanyItem("chainsafesystems", "https://boards.greenhouse.io/chainsafesystems", ScrapeGreenhouse, "https://chainsafe.io", "Infra"))
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
    jobs_data = company.scraper_type().getJobs(driver, company.jobs_url)
    for entry in jobs_data:
        print(entry)

driver.close()
