from selenium import webdriver
import scrapeLever
import scrapeGreenhouse
import scrapeSmartrecruiters
import scrapeRecruitee
import scrapeBinance
from datetime import datetime
import json

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

lever_web_pages = [
    "https://jobs.lever.co/Coinshift",
    "https://jobs.lever.co/chainlink", 
    "https://jobs.lever.co/kraken", 
    "https://jobs.lever.co/swissborg", 
    "https://jobs.lever.co/OpenSea", 
    "https://jobs.lever.co/storyprotocol", 
    "https://jobs.lever.co/ethereumfoundation", 
    "https://jobs.eu.lever.co/aave", 
    "https://jobs.lever.co/crypto",
    "https://jobs.lever.co/Polygon",
    "https://jobs.lever.co/tokenmetrics",
    "https://jobs.lever.co/offchainlabs",
    "https://jobs.lever.co/subspacelabs"
]

greenhouse_web_pages = [
    "https://boards.greenhouse.io/moonpay",
    "https://boards.greenhouse.io/bitmex",
    "https://boards.greenhouse.io/bitgo", 
    "https://boards.greenhouse.io/genesisglobaltradinginc", 
    "https://boards.greenhouse.io/amun", 
    "https://boards.greenhouse.io/exodus54", 
    "https://boards.eu.greenhouse.io/bitpanda", 
    "https://boards.greenhouse.io/quiknodeinc", 
    "https://boards.greenhouse.io/uniswaplabs", 
    "https://boards.greenhouse.io/alchemy", 
    "https://boards.greenhouse.io/chainalysis", 
    "https://boards.eu.greenhouse.io/nethermind",
    "https://boards.greenhouse.io/magiceden",
    "https://boards.greenhouse.io/blockdaemon",
    "https://boards.greenhouse.io/dfinity",
    "https://boards.greenhouse.io/figment",
    "https://boards.greenhouse.io/parity",
    "https://boards.greenhouse.io/optimism",
    "https://boards.greenhouse.io/flashbots",
    "https://boards.greenhouse.io/oplabs"
]

smartrecruiters_web_pages = [
    "https://careers.smartrecruiters.com/B6/coinmarketcap",
    "https://careers.smartrecruiters.com/B6/trustwallet",
    "https://careers.smartrecruiters.com/Swissquote"
]

recruitee_web_pages = [
    "https://bitfinex.recruitee.com"
]

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

def addJobsToIndex(company_page, data):
    company_name = (company_page.split('/')[-1]).split('.')[0]
    printAndCollectNumbers(company_name, len(data))
    html = dict_to_html_table_with_header(company_name, data)
    with open('index.html', 'a') as f:
        f.write(html)

def addJobsToTest(company_page, data):
    company_name = (company_page.split('/')[-1]).split('.')[0]
    html = dict_to_html_table_with_header_and_filter(company_name, data)
    with open('test.html', 'a') as f:
        f.write(html)

def addJobsToDev(company_page, data):
    company_name = (company_page.split('/')[-1]).split('.')[0]
    filter_dev = ['software engineer', 'stack engineer', 'java engineer', 'backend engineer', 'backend developer', 'java developer']
    html = dict_to_html_table_with_header_and_filter(company_name, data, filter=filter_dev)
    with open('dev.html', 'a') as f:
        f.write(html)

def addJobsToDevOps(company_page, data):
    company_name = (company_page.split('/')[-1]).split('.')[0]
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

for page in greenhouse_web_pages:
    data = scrapeGreenhouse.getJobs(driver, page)
    addJobsToIndex(page, data)
    addJobsToTest(page, data)
    addJobsToDev(page, data)
    addJobsToDevOps(page, data)

for page in lever_web_pages:
    data = scrapeLever.getJobs(driver, page)
    addJobsToIndex(page, data)
    addJobsToTest(page, data)
    addJobsToDev(page, data)
    addJobsToDevOps(page, data)

for page in smartrecruiters_web_pages:
    data = scrapeSmartrecruiters.getJobs(driver, page)
    addJobsToIndex(page, data)
    addJobsToTest(page, data)
    addJobsToDev(page, data)
    addJobsToDevOps(page, data)

for page in recruitee_web_pages:
    data = scrapeRecruitee.getJobs(driver, page)
    addJobsToIndex(page, data)
    addJobsToTest(page, data)
    addJobsToDev(page, data)
    addJobsToDevOps(page, data)

# Custom jobs
paxos_data = scrapeGreenhouse.getJobs(driver, "https://paxos.com/careers/role")
addJobsToIndex('paxos', paxos_data)
addJobsToTest('paxos', paxos_data)
addJobsToDev('paxos', paxos_data)
addJobsToDevOps('paxos', paxos_data)
status_data = scrapeGreenhouse.getJobs(driver, "https://jobs.status.im")
addJobsToIndex('status', status_data)
addJobsToTest('status', status_data)
addJobsToDev('status', status_data)
addJobsToDevOps('status', status_data)
binance_data = scrapeBinance.getJobs(driver)
addJobsToIndex('binance', binance_data)
addJobsToTest('binance', binance_data)
addJobsToDev('binance', binance_data)
addJobsToDevOps('binance', binance_data)

driver.close()

writeNumbers()
