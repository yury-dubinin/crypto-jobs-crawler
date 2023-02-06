from selenium import webdriver
from pathlib import Path
import scrapeLever
import scrapeGreenhouse
import scrapeSmartrecruiters
import scrapeRecruitee
from datetime import datetime
import json

# remove index.html to re-create from new data set
index_file = Path("./index.html")
index_file.unlink(missing_ok=True)
# set up headless webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

lever_web_pages = [
    "https://jobs.lever.co/chainlink", 
    "https://jobs.lever.co/kraken", 
    "https://jobs.lever.co/swissborg", 
    "https://jobs.lever.co/OpenSea", 
    "https://jobs.lever.co/storyprotocol", 
    "https://jobs.lever.co/ethereumfoundation", 
    "https://jobs.eu.lever.co/aave", 
    "https://jobs.lever.co/crypto"
]

greenhouse_web_pages = [
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
    "https://boards.greenhouse.io/magiceden"
]

smartrecruiters_web_pages = [
    "https://careers.smartrecruiters.com/B6/coinmarketcap",
    "https://careers.smartrecruiters.com/B6/trustwallet"
]

recruitee_web_pages = [
    "https://bitfinex.recruitee.com"
]

def setColor(title):
    testTags = ["qa", "test", "sdet"]
    devTags = ['software engineer', 'stack engineer', 'java engineer', 'backend developer']
    if any(ext in title.lower() for ext in testTags):
        return ' bgcolor="lightgreen" '
    elif any(ext in title.lower() for ext in devTags):
        return ' bgcolor="lightblue" '
    else:
        return ""

def dict_to_html_table_with_header(header, dictionary:tuple):
    html_table = '<table width="72%" align="center" border="1">'
    jobs_total = f"Total Jobs: {len(dictionary)}"
    html_table += "<tr><th>" + header.upper() + "</th><th>"+ jobs_total + "</th></tr>"
    for elem in dictionary:
        color_code = setColor(elem[0])
        wrappedLink = f"<a href='{elem[1]}' target='_blank' >Apply</a>"
        html_table += "<tr"+color_code+"><td>" + elem[0] + "</td><td width='20%' >" + wrappedLink + "</td></tr>"
    html_table += "</table>"
    return html_table

# count open positions
total_number_of_jobs:int = 0
current_jobs = {}
def printAndCollectNumbers(company:str, total:int):
    now = datetime.date(datetime.now())
    print(f'Company {company} has {total} open positions on {now}')
    global total_number_of_jobs
    total_number_of_jobs = total_number_of_jobs + total
    global current_jobs
    current_jobs[company]= total

def writeNumbers():
    now = datetime.date(datetime.now())
    global total_number_of_jobs
    print(f'In Total {total_number_of_jobs} of open positions on {now}')
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

for page in greenhouse_web_pages:
    addJobsToIndex(page, scrapeGreenhouse.getJobs(driver, page))

for page in lever_web_pages:
    addJobsToIndex(page, scrapeLever.getJobs(driver, page))

for page in smartrecruiters_web_pages:
    addJobsToIndex(page, scrapeSmartrecruiters.getJobs(driver, page))

for page in recruitee_web_pages:
    addJobsToIndex(page, scrapeRecruitee.getJobs(driver, page))

driver.close()

writeNumbers()
