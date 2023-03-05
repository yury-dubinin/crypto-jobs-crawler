from selenium import webdriver
from datetime import datetime
import json
from companyItem import CompanyItem
import companyList


company_list = companyList.getCompanyList()
print(f'[CRAWLER] Number of companies: {len(company_list)}')
# remove index.html to re-create from new data set
with open('index.html', 'w') as f:
    f.write(f'<p align="center"> Number of companies: {len(company_list)} Last Updated at: {datetime.date(datetime.now())} </p>')
    f.write('<p align="center"><a href="test.html" target="_blank">Just Test jobs</a> || <a href="dev.html" target="_blank">Just Dev jobs</a>  || <a href="devops.html" target="_blank">Just DevOps/SRE jobs</a></p>')
with open('test.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('dev.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('devops.html', 'w') as f:
    f.write('<!DOCTYPE html>')

# setup headless webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

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
        'full-stack dev',
        'python developer',
        'engineer – java',
        'java development lead'
    ]
    devOpsTags = [
        'devops',
        'sre',
        'site reliability',
        'platforms engineer',
        'infrastructure engineer',
        'network engineer',
        'devsecops',
        'Platform Engineer'
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
    if any(ext.lower() in job_title.lower() for ext in filters):
        return True
    return False

def dict_to_html_table_with_header(company:CompanyItem, dictionary):
    html_table = '<table width="72%" align="center" border="1">'
    jobs_total = f"Total Jobs: {len(dictionary)}"
    wrappedHeaderLink = f"<a href='{company.company_url}' target='_blank' >{company.company_name.upper()}</a>"
    html_table += "<tr><th>" + wrappedHeaderLink + "</th><th width='20%' >"+ jobs_total + "</th></tr>"
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

def addJobsToIndex(company:CompanyItem, data):
    printAndCollectNumbers(company.company_name, len(data))
    html = dict_to_html_table_with_header(company, data)
    with open('index.html', 'a') as f:
        f.write(html)

def addJobsToTest(company:CompanyItem, data):
    html = dict_to_html_table_with_header_and_filter(company.company_name, data)
    with open('test.html', 'a') as f:
        f.write(html)

def addJobsToDev(company:CompanyItem, data):
    filter_dev = ['software engineer', 'stack engineer', 'java engineer', 'backend engineer', 'backend developer', 'java developer']
    html = dict_to_html_table_with_header_and_filter(company.company_name, data, filter=filter_dev)
    with open('dev.html', 'a') as f:
        f.write(html)

def addJobsToDevOps(company:CompanyItem, data):
    devOpsTags = [
        'devops engineer',
        'sre',
        'sre engineer',
        'site reliability',
        'platforms engineer',
        'infrastructure engineer',
        'network engineer',
        'observability engineer'
    ]
    html = dict_to_html_table_with_header_and_filter(company.company_name, data, filter=devOpsTags)
    with open('devops.html', 'a') as f:
        f.write(html)

for company in company_list:
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    addJobsToIndex(company, data)
    addJobsToTest(company, data)
    addJobsToDev(company, data)
    addJobsToDevOps(company, data)

driver.close()

writeNumbers()
