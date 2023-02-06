from selenium.webdriver.common.by import By

def cleanLocation(location):
    if 'remote' in location.lower() or 'global' in location.lower():
        return {"REMOTE"}
    return set(([x.strip() for x in location.split(',')]))

def getJobs(driver, web_page):
    print(f'Scrap page: {web_page}')
    driver.get(web_page)
    groupElements = driver.find_elements(By.CSS_SELECTOR, 'div [class="job"]')
    result = []
    for elem in groupElements:
        linkElem = elem.find_element(By.CSS_SELECTOR, '[class="job-title"] a')
        locationElem = elem.find_element(By.CSS_SELECTOR, '[class="job-location"]')
        jobUrl = linkElem.get_attribute('href')
        location = cleanLocation(locationElem.text)
        result.append((f'{linkElem.text} From:{location}', jobUrl))
    print(f'Scraped {len(result)} jobs from {web_page}')
    return result
