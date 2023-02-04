import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

# create folder to 
Path("./resources").mkdir(parents=True, exist_ok=True)
# remove index.html to re-create from new data set
index_file = Path("./index.html")
index_file.unlink(missing_ok=True)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
chainlink = "https://jobs.lever.co/chainlink"
kraken = "https://jobs.lever.co/kraken"
swissborg = "https://jobs.lever.co/swissborg"
opensea = "https://jobs.lever.co/OpenSea"
storyprotocol = "https://jobs.lever.co/storyprotocol"
ethereumfoundation = "https://jobs.lever.co/ethereumfoundation"
aave = "https://jobs.eu.lever.co/aave"

lever_web_pages = [chainlink, kraken, swissborg, opensea, storyprotocol, ethereumfoundation, aave]

bitgo = "https://boards.greenhouse.io/bitgo"
genesisglobaltradinginc = "https://boards.greenhouse.io/genesisglobaltradinginc"
amun = "https://boards.greenhouse.io/amun"
exodus54 =  "https://boards.greenhouse.io/exodus54"
bitpanda = "https://boards.eu.greenhouse.io/bitpanda"
quiknodeinc = "https://boards.greenhouse.io/quiknodeinc"
uniswaplabs = "https://boards.greenhouse.io/uniswaplabs"
alchemy = "https://boards.greenhouse.io/alchemy"
chainalysis = "https://boards.greenhouse.io/chainalysis"
nethermind = "https://boards.eu.greenhouse.io/nethermind"

greenhouse_web_pages = [bitgo, genesisglobaltradinginc, amun, exodus54, bitpanda, quiknodeinc, uniswaplabs, alchemy, chainalysis, nethermind]

def getJobsFromLever(web_page):
    print(f'Scrap page: {web_page}')
    driver.get(web_page)
    titleElems = driver.find_elements(By.CSS_SELECTOR, 'a [data-qa="posting-name"]')
    linkElements = driver.find_elements(By.XPATH, '//*[@data-qa="posting-name"]/..')
    print(f'Elements with name: {len(titleElems)} vs Links: {len(linkElements)}')
    titles = list(map(lambda title: title.text, titleElems))
    links = list(map(lambda link: link.get_attribute('href'), linkElements))
    wrappedLinks = list(map(lambda link: f"<a href='{link}'>Apply</a>", links))
    print(f'Records with Name: {len(titles)} vs Links: {len(links)}')
    res = dict(zip(titles, wrappedLinks))
    #print(res)
    return res

def getJobsFromGreenhouse(web_page):
    print(f'Scrap page: {web_page}')
    driver.get(web_page)
    titleElems = driver.find_elements(By.CSS_SELECTOR, 'div [class="opening"] a')
    linkElements = driver.find_elements(By.XPATH, '//div[@class="opening"]/a')
    print(f'Elements with name: {len(titleElems)} vs Links: {len(linkElements)}')
    titles = list(map(lambda title: title.text, titleElems))
    links = list(map(lambda link: link.get_attribute('href'), linkElements))
    wrappedLinks = list(map(lambda link: f"<a href='{link}'>Apply</a>", links))
    print(f'Records with Name: {len(titles)} vs Links: {len(links)}')
    res = dict(zip(titles, wrappedLinks))
    #print(res)
    return res

# not used but idea is to use json files as sourse for UI/BI 
def writeJobs(company_name, data):
    with open(f"resources/{company_name}.json", "w") as file:
        json.dump(data, file, indent=4)

def dict_to_html_table_with_header(header, dictionary):
    html_table = '<table width="72%" align="center" border="1">'
    jobs_total = f"Total Jobs: {len(dictionary)}"
    html_table += "<tr><th>" + header.upper() + "</th><th>"+ jobs_total + "</th></tr>"
    for key, value in dictionary.items():
        html_table += "<tr><td>" + key + "</td><td width='20%' >" + value + "</td></tr>"
    html_table += "</table>"
    return html_table

def convertJobs(company_name, data):
    html = dict_to_html_table_with_header(company_name, data)
    with open('index.html', 'a') as f:
        f.write(html)

for page in greenhouse_web_pages:
    convertJobs(page.split('/')[3], getJobsFromGreenhouse(page))

for page in lever_web_pages:
    convertJobs(page.split('/')[3], getJobsFromLever(page))

driver.close()
