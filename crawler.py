from selenium import webdriver
from pathlib import Path
import scrapeLever
import scrapeGreenhouse


# remove index.html to re-create from new data set
index_file = Path("./index.html")
index_file.unlink(missing_ok=True)
# set up headless webdriver
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
crypto = "https://jobs.lever.co/crypto"

lever_web_pages = [chainlink, kraken, swissborg, opensea, storyprotocol, ethereumfoundation, aave, crypto]

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

def setColor(title):
    testTags = ["qa", "test", "sdet"]
    if any(ext in title.lower() for ext in testTags):
        return ' bgcolor="green" '
    else:
        return ""

def dict_to_html_table_with_header(header, dictionary:tuple):
    html_table = '<table width="72%" align="center" border="1">'
    jobs_total = f"Total Jobs: {len(dictionary)}"
    html_table += "<tr><th>" + header.upper() + "</th><th>"+ jobs_total + "</th></tr>"
    for elem in dictionary:
        color_code = setColor(elem[0])
        wrappedLink = f"<a href='{elem[1]}'>Apply</a>"
        html_table += "<tr"+color_code+"><td>" + elem[0] + "</td><td width='20%' >" + wrappedLink + "</td></tr>"
    html_table += "</table>"
    return html_table

def convertJobs(company_name, data):
    html = dict_to_html_table_with_header(company_name, data)
    with open('index.html', 'a') as f:
        f.write(html)

for page in greenhouse_web_pages:
    convertJobs(page.split('/')[3], scrapeGreenhouse.getJobs(driver, page))

for page in lever_web_pages:
    convertJobs(page.split('/')[3], scrapeLever.getJobs(driver, page))

driver.close()
