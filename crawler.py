from selenium import webdriver
from datetime import datetime
import json
from companyItem import CompanyItem
import companyList

company_list = companyList.getCompanyList()
print(f'[CRAWLER] Number of companies: {len(company_list)}')
# remove index.html to re-create from new data set
with open('index.html', 'w') as f:
    f.write(
        f'<p align="center"> Number of companies: {len(company_list)} Last Updated at: {datetime.date(datetime.now())} </p>')
    test_link = '<a href="test.html" target="_blank">Test jobs</a>'
    dev_link = '<a href="dev.html" target="_blank">Dev jobs</a>'
    devops_link = '<a href="devops.html" target="_blank">DevOps/SRE jobs</a>'
    data_link = '<a href="data.html" target="_blank">Data jobs</a>'
    finance_link = '<a href="finance.html" target="_blank">Finance jobs</a>'
    f.write(f'<p align="center"> {test_link} || {dev_link} || {devops_link} || {data_link} || {finance_link} </p>')
with open('test.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('dev.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('devops.html', 'w') as f:
    f.write('<!DOCTYPE html>')
with open('finance.html', 'w') as f:
    f.write('<!DOCTYPE html>')

# setup headless webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


def filter_jobs(job_title: str, filters):
    if any(ext.lower() in job_title.lower() for ext in filters):
        return True
    return False


def is_dev_job(title):
    tags = [
        'software engineer',
        'stack engineer',
        'systems engineer',
        'System Engineer',
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
        'java development lead',
        'python dev',
        'Golang Developer',
        'Engineer - Java',
        'Java Development Engineer',
        'Frontend Developer',
        'Software Development Engineer',
        'Software Architect',
        'Frontend Engineer',
        'Front End Developer',
        'Frontend Architect ',
        'Front-end Developer',
        'Web Developer',
        'Front-End Engineer',
        'Lead Engineer',
        'Fullstack Developer',
        'Solutions Engineer',
        'Compiler Engineer',
        '(Front-End) Engineer',
        'Solutions Engineer',
        'TypeScript Toolkit Engineer',
        'Technical Lead',
        'Backend / Fullstack',
        'Front End Architect',
        'Solution Architect ',
        'Golang Team Lead',
        'Senior Engineer, Frontend',
        'C++ '
    ]
    result = filter_jobs(title, tags)
    anti_filters = ['test', 'qa', 'manager', 'sdet', 'director']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_test_job(title):
    tags = ['qa', 'test', 'sdet', 'quality assurance']
    result = filter_jobs(title, tags)
    anti_filters = ['manager', 'director', 'head']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_finance_job(title):
    tags = ['Accountant', 'Treasury', 'Finance', 'Accounting', 'Tax Specialist', 'Financial', 'FinCrime', 'Accounts Payable']
    result = filter_jobs(title, tags)
    anti_filters = ['manager', 'director', 'head of', 'Scientist', 'Engineer']
    if any(ext.lower() in title.lower() for ext in anti_filters):
        return False
    return result


def is_dev_ops_job(title):
    tags = [
        'devops',
        'sre',
        'site reliability',
        'platforms engineer',
        'infrastructure engineer',
        'network engineer',
        'devsecops',
        'Platform Engineer',
        'Tooling Engineer',
        'Infrastructure Development Engineer',
        'Infrastructure & Tooling'
    ]
    return filter_jobs(title, tags)


def is_data_job(title):
    tags = ['Data Engineer', 'Data Analyst', 'Data Scientist', 'Data Engineer', 'Data Analytics Engineer', 'Data Science']
    return filter_jobs(title, tags)


def set_color(title):
    if is_test_job(title):
        return ' bgcolor="lightgreen" '
    elif is_dev_job(title):
        return ' bgcolor="lightblue" '
    elif is_dev_ops_job(title):
        return ' bgcolor="lightyellow" '
    elif is_data_job(title):
        return ' bgcolor="cyan" '
    elif is_finance_job(title):
        return ' bgcolor="magenta" '
    else:
        return ""


def dict_to_html_table_with_header(company: CompanyItem, dictionary, logo=''):
    html_table = '<table width="72%" align="center" border="1">'
    jobs_total = f"Total Jobs: {len(dictionary)}"
    wrapped_header_link = f"<a href='{company.company_url}' target='_blank' > {logo} </a>"
    html_table += "<tr><th>" + wrapped_header_link + "</th><th width='20%' >" + jobs_total + "</th></tr>"
    for elem in dictionary:
        color_code = set_color(elem[0])
        wrapped_link = f"<a href='{elem[1]}' target='_blank' >Apply</a>"
        html_table += "<tr" + color_code + "><td>" + elem[0] + "</td><td width='20%' >" + wrapped_link + "</td></tr>"
    html_table += "</table>"
    return html_table


def dict_to_html_table_with_header_and_filter(header, dictionary, filter):
    filtered = []
    for elem in dictionary:
        if filter(elem[0]):
            filtered.append(elem)

    jobs_total = f'No {filter.__name__}'
    if len(filtered) > 0:
        jobs_total = f"Total {filter.__name__}(s): {len(filtered)}"
    print(f'[CRAWLER] {jobs_total} at {header}')
    # For now keep the table
    html_table = '<table width="80%" align="center" border="1">'
    html_table += "<tr><th>" + header.upper() + "</th><th width='20%' >" + jobs_total + "</th></tr>"

    for elem in filtered:
        wrapped_link = f"<a href='{elem[1]}' target='_blank' >Apply</a>"
        html_table += "<tr><td>" + elem[0] + "</td><td width='20%' >" + wrapped_link + "</td></tr>"

    html_table += "</table>"
    return html_table


# count open positions
total_number_of_jobs: int = 0
current_jobs = {}


def print_and_collect_numbers(company_name: str, total: int):
    now = datetime.date(datetime.now())
    print(f'[CRAWLER] Company {company_name} has {total} open positions on {now}')
    global total_number_of_jobs
    total_number_of_jobs = total_number_of_jobs + total
    global current_jobs
    current_jobs[company_name] = total


def write_numbers():
    now = datetime.date(datetime.now())
    global total_number_of_jobs
    print(f'[CRAWLER] In Total {total_number_of_jobs} of open positions on {now}')
    global current_jobs
    current_jobs["Total Jobs"] = total_number_of_jobs
    with open(f"current.json", "w") as file:
        json.dump(current_jobs, file, indent=4)


def add_jobs_to_index(company: CompanyItem, data, logo):
    print_and_collect_numbers(company.company_name, len(data))
    html = dict_to_html_table_with_header(company, data, logo)
    with open('index.html', 'a') as f:
        f.write(html)


def add_jobs_to_test(company: CompanyItem, data):
    html = dict_to_html_table_with_header_and_filter(company.company_name, data, filter=is_test_job)
    with open('test.html', 'a') as f:
        f.write(html)


def add_jobs_to_dev(company: CompanyItem, data):
    html = dict_to_html_table_with_header_and_filter(company.company_name, data, filter=is_dev_job)
    with open('dev.html', 'a') as f:
        f.write(html)


def add_jobs_to_dev_ops(company: CompanyItem, data):
    html = dict_to_html_table_with_header_and_filter(company.company_name, data, filter=is_dev_ops_job)
    with open('devops.html', 'a') as f:
        f.write(html)


def add_jobs_to_data(company: CompanyItem, data):
    html = dict_to_html_table_with_header_and_filter(company.company_name, data, filter=is_data_job)
    with open('data.html', 'a') as f:
        f.write(html)


def add_jobs_to_finance(company: CompanyItem, data):
    html = dict_to_html_table_with_header_and_filter(company.company_name, data, filter=is_finance_job)
    with open('finance.html', 'a') as f:
        f.write(html)


for company in company_list:
    data = company.scraper_type().getJobs(driver, company.jobs_url)
    company_logo = companyList.get_logo(company_name=company.company_name)
    add_jobs_to_index(company, data, company_logo)
    add_jobs_to_test(company, data)
    add_jobs_to_dev(company, data)
    add_jobs_to_dev_ops(company, data)
    add_jobs_to_data(company, data)
    add_jobs_to_finance(company, data)

driver.close()

write_numbers()
