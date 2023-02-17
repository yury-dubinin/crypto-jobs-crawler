from selenium import webdriver
from scrapeLever import ScrapeLever
from scrapeGreenhouse import ScrapeGreenhouse
from scrapeSmartrecruiters import ScrapeSmartrecruiters
from scrapeRecruitee import ScrapeRecruitee
from scrapeBinance import ScrapeBinance
from datetime import datetime
import json
from companyItem import CompanyItem

# remove index.html to re-create from new data set
with open('index.html', 'w') as f:
        f.write('<p><a href="test.html" target="_blank">Just Test jobs</a> || <a href="dev.html" target="_blank">Just Dev jobs</a>  || <a href="devops.html" target="_blank">Just DevOps/SRE jobs</a></p>')
with open('test.html', 'w') as f:
        f.write('<!DOCTYPE html>')
with open('dev.html', 'w') as f:
        f.write('<!DOCTYPE html>')
with open('devops.html', 'w') as f:
        f.write('<!DOCTYPE html>')
# set up headless webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

company_list = []
company_list.append(CompanyItem("paxos",  "https://paxos.com/careers/role", ScrapeGreenhouse, "https://paxos.com", "Stable Coin"))
company_list.append(CompanyItem("circle",  "https://boards.greenhouse.io/circle", ScrapeGreenhouse, "https://circle.com", "Stable Coin"))
company_list.append(CompanyItem("status",  "https://jobs.status.im", ScrapeGreenhouse, "https://status.im","Messanger"))
company_list.append(CompanyItem("OKX",  "https://boards.greenhouse.io/OKX", ScrapeGreenhouse, "https://okx.com","Exchange"))
company_list.append(CompanyItem("bitmex",  "https://boards.greenhouse.io/bitmex", ScrapeGreenhouse, "https://bitmex.com","Exchange"))
company_list.append(CompanyItem("bitgo",  "https://boards.greenhouse.io/bitgo", ScrapeGreenhouse, "https://bitgo.com","Exchange"))
company_list.append(CompanyItem("bitpanda",  "https://boards.eu.greenhouse.io/bitpanda", ScrapeGreenhouse, "https://bitpanda.com","Exchange"))
company_list.append(CompanyItem("uniswaplabs",  "https://boards.greenhouse.io/uniswaplabs", ScrapeGreenhouse, "https://uniswap.org","Exchange Protocol"))
company_list.append(CompanyItem("moonpay",  "https://boards.greenhouse.io/moonpay", ScrapeGreenhouse, "https://www.moonpay.com","Payments"))
company_list.append(CompanyItem("blockdaemon",  "https://boards.greenhouse.io/blockdaemon", ScrapeGreenhouse, "https://www.blockdaemon.com","Staking & Infra"))
company_list.append(CompanyItem("figment",  "https://boards.greenhouse.io/figment", ScrapeGreenhouse, "https://www.figment.io","Staking & Infra"))
company_list.append(CompanyItem("quiknodeinc",  "https://boards.greenhouse.io/quiknodeinc", ScrapeGreenhouse, "https://www.quicknode.com","Staking & Infra"))
company_list.append(CompanyItem("genesisglobaltradinginc",  "https://boards.greenhouse.io/genesisglobaltradinginc", ScrapeGreenhouse, "https://genesistrading.com","OTC Trading"))
company_list.append(CompanyItem("amun",  "https://boards.greenhouse.io/amun", ScrapeGreenhouse, "https://www.21.co","OTC"))
company_list.append(CompanyItem("exodus54",  "https://boards.greenhouse.io/exodus54", ScrapeGreenhouse, "https://www.exodus.com","Wallet"))
company_list.append(CompanyItem("alchemy",  "https://boards.greenhouse.io/alchemy", ScrapeGreenhouse, "https://www.alchemy.com","Dev & Infra"))
company_list.append(CompanyItem("chainalysis",  "https://boards.greenhouse.io/chainalysis", ScrapeGreenhouse, "https://www.chainalysis.com","Crypto Research"))
company_list.append(CompanyItem("magiceden",  "https://boards.greenhouse.io/magiceden", ScrapeGreenhouse, "https://www.magiceden.io","NFT"))
company_list.append(CompanyItem("nethermind",  "https://boards.eu.greenhouse.io/nethermind", ScrapeGreenhouse, "https://nethermind.io","Crypto software"))
company_list.append(CompanyItem("dfinity",  "https://boards.greenhouse.io/dfinity", ScrapeGreenhouse, "https://dfinity.org","Blockchain"))
company_list.append(CompanyItem("parity",  "https://boards.greenhouse.io/parity", ScrapeGreenhouse, "https://www.parity.io","Infra"))
company_list.append(CompanyItem("optimism",  "https://boards.greenhouse.io/optimism", ScrapeGreenhouse, "https://www.optimism.io","L2 protocol"))
company_list.append(CompanyItem("flashbots",  "https://boards.greenhouse.io/flashbots", ScrapeGreenhouse, "https://www.flashbots.net","ETH MEV"))
company_list.append(CompanyItem("oplabs",  "https://boards.greenhouse.io/oplabs", ScrapeGreenhouse, "https://www.oplabs.co","L2 protocol"))
company_list.append(CompanyItem("bitfinex",  "https://bitfinex.recruitee.com", ScrapeRecruitee, "https://www.bitfinex.com","Exchange"))
company_list.append(CompanyItem("binance",  "https://www.binance.com/en/careers/job-openings", ScrapeBinance, "https://www.binance.com","Exchange"))
company_list.append(CompanyItem("coinmarketcap",  "https://careers.smartrecruiters.com/B6/coinmarketcap", ScrapeSmartrecruiters, "https://coinmarketcap.com","Information"))
company_list.append(CompanyItem("trustwallet",  "https://careers.smartrecruiters.com/B6/trustwallet", ScrapeSmartrecruiters, "https://trustwallet.com","Wallet"))
company_list.append(CompanyItem("Swissquote",  "https://careers.smartrecruiters.com/Swissquote", ScrapeSmartrecruiters, "https://en.swissquote.com","Exchange"))
company_list.append(CompanyItem("Coinshift",  "https://jobs.lever.co/Coinshift", ScrapeLever, "https://coinshift.xyz","Custody software"))
company_list.append(CompanyItem("chainlink",  "https://jobs.lever.co/chainlink", ScrapeLever, "https://chain.link","Blockchain"))
company_list.append(CompanyItem("kraken",  "https://jobs.lever.co/kraken", ScrapeLever, "https://kraken.com","Exchange"))
company_list.append(CompanyItem("swissborg",  "https://jobs.lever.co/swissborg", ScrapeLever, "https://swissborg.com","Exchange"))
company_list.append(CompanyItem("OpenSea",  "https://jobs.lever.co/OpenSea", ScrapeLever, "https://opensea.io","NFT"))
company_list.append(CompanyItem("storyprotocol",  "https://jobs.lever.co/storyprotocol", ScrapeLever, "https://www.storyprotocol.xyz","Protocol"))
company_list.append(CompanyItem("ethereumfoundation",  "https://jobs.lever.co/ethereumfoundation", ScrapeLever, "https://ethereum.org","Blockchain"))
company_list.append(CompanyItem("aave",  "https://jobs.eu.lever.co/aave", ScrapeLever, "https://aave.com","Protocol"))
company_list.append(CompanyItem("crypto",  "https://jobs.lever.co/crypto", ScrapeLever, "https://crypto.com","Exchange"))
company_list.append(CompanyItem("Polygon",  "https://jobs.lever.co/Polygon", ScrapeLever, "https://polygon.technology","Blockchain"))
company_list.append(CompanyItem("tokenmetrics",  "https://jobs.lever.co/tokenmetrics", ScrapeLever, "https://www.tokenmetrics.com","Information"))
company_list.append(CompanyItem("offchainlabs",  "https://jobs.lever.co/offchainlabs", ScrapeLever, "https://offchainlabs.com","Protocol"))
company_list.append(CompanyItem("subspacelabs",  "https://jobs.lever.co/subspacelabs", ScrapeLever, "https://subspace.network","Blockchain Infra"))
company_list.append(CompanyItem("tron",  "https://boards.greenhouse.io/rainberry", ScrapeGreenhouse, "https://tron.network","Blockchain"))


def setColor(title):
    testTags = ['qa', 'test', 'sdet', 'quality assurance']
    devTags = [
        'software engineer', 
        'stack engineer',
        'systems engineer', 
        'java engineer', 
        'backend engineer', 
        'backend developer', 
        'java developer',
        'rust engineer',
        'golang engineer',
        'principal engineer',
        'back-end engineer',
        'senior java',
        'staff engineer', 
        'api engineer',
        'rust developer',
        'full stack developer',
        'c++ developer',
        'full-stack dev'
    ]
    devOpsTags = [
        'devops',
        'sre',
        'site reliability',
        'platforms engineer',
        'infrastructure engineer',
        'network engineer'
    ]
    if any(ext in title.lower() for ext in testTags):
        return ' bgcolor="lightgreen" '
    elif any(ext in title.lower() for ext in devTags):
        return ' bgcolor="lightblue" '
    elif any(ext in title.lower() for ext in devOpsTags):
        return ' bgcolor="lightyellow" '
    else:
        return ""

def filterJobs(job_title:str, filters):
    if any(ext in job_title.lower() for ext in filters):
        return True
    return False

def dict_to_html_table_with_header(header, dictionary):
    html_table = '<table width="72%" align="center" border="1">'
    jobs_total = f"Total Jobs: {len(dictionary)}"
    html_table += "<tr><th>" + header.upper() + "</th><th width='20%' >"+ jobs_total + "</th></tr>"
    for elem in dictionary:
        color_code = setColor(elem[0])
        wrappedLink = f"<a href='{elem[1]}' target='_blank' >Apply</a>"
        html_table += "<tr"+color_code+"><td>" + elem[0] + "</td><td width='20%' >" + wrappedLink + "</td></tr>"
    html_table += "</table>"
    return html_table

def dict_to_html_table_with_header_and_filter(header, dictionary, filter=['qa', 'test', 'quality']):
    filtered = []
    for elem in dictionary:
        if filterJobs(elem[0], filter):
            filtered.append(elem)

    jobs_total = f'No {filter} jobs'
    if len(filtered) > 0:
        jobs_total = f"Total {filter} Jobs: {len(filtered)}"
    print(f'[CRAWLER] {jobs_total} at {header}')
    # For now keep the table
    html_table = '<table width="80%" align="center" border="1">'
    html_table += "<tr><th>" + header.upper() + "</th><th width='20%' >"+ jobs_total + "</th></tr>"

    for elem in filtered:
        wrappedLink = f"<a href='{elem[1]}' target='_blank' >Apply</a>"
        html_table += "<tr><td>" + elem[0] + "</td><td width='20%' >" + wrappedLink + "</td></tr>"

    html_table += "</table>"
    return html_table

# count open positions
total_number_of_jobs:int = 0
current_jobs = {}
def printAndCollectNumbers(company:str, total:int):
    now = datetime.date(datetime.now())
    print(f'[CRAWLER] Company {company} has {total} open positions on {now}')
    global total_number_of_jobs
    total_number_of_jobs = total_number_of_jobs + total
    global current_jobs
    current_jobs[company]= total

def writeNumbers():
    now = datetime.date(datetime.now())
    global total_number_of_jobs
    print(f'[CRAWLER] In Total {total_number_of_jobs} of open positions on {now}')
    global current_jobs
    current_jobs["Total Jobs"]= total_number_of_jobs
    with open(f"current.json", "w") as file:
        json.dump(current_jobs, file, indent=4)

def addJobsToIndex(company_name, data):
    printAndCollectNumbers(company_name, len(data))
    html = dict_to_html_table_with_header(company_name, data)
    with open('index.html', 'a') as f:
        f.write(html)

def addJobsToTest(company_name, data):
    html = dict_to_html_table_with_header_and_filter(company_name, data)
    with open('test.html', 'a') as f:
        f.write(html)

def addJobsToDev(company_name, data):
    filter_dev = ['software engineer', 'stack engineer', 'java engineer', 'backend engineer', 'backend developer', 'java developer']
    html = dict_to_html_table_with_header_and_filter(company_name, data, filter=filter_dev)
    with open('dev.html', 'a') as f:
        f.write(html)

def addJobsToDevOps(company_name, data):
    devOpsTags = [
        'devops engineer',
        'sre',
        'sre engineer'
        'site reliability',
        'platforms engineer',
        'infrastructure engineer',
        'network engineer',
        'observability engineer'
    ]
    html = dict_to_html_table_with_header_and_filter(company_name, data, filter=devOpsTags)
    with open('devops.html', 'a') as f:
        f.write(html)

for company in company_list:
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    addJobsToIndex(company.company_name, data)
    addJobsToTest(company.company_name, data)
    addJobsToDev(company.company_name, data)
    addJobsToDevOps(company.company_name, data)

driver.close()

writeNumbers()
