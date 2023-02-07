from selenium.webdriver.common.by import By

def cleanLocation(location:str):
    location = location.replace("/ Full-time", "")
    if 'global' in location.lower() or 'remote : remote' in location.lower():
        return {"REMOTE"}
    return set(([x.strip() for x in location.split(',')]))

def getJobs(driver, web_page="https://www.binance.com/en/careers/job-openings"):
    print(f'Scrap page: {web_page}')
    driver.get(web_page)
    groupElements = driver.find_elements(By.XPATH, '//div[contains(@class,"posting")]')
    print(f'Found {len(groupElements)} jobs')
    result = []
    for elem in groupElements:
        linkElem = elem.find_element(By.CSS_SELECTOR, 'a')
        locationElem = elem.find_element(By.CSS_SELECTOR, 'div[data-bn-type="text"]')
        jobUrl = linkElem.get_attribute('href')
        location = cleanLocation(locationElem.text)
        result.append((f'{linkElem.text} From:{location}', jobUrl))
    print(f'Scraped {len(result)} jobs from {web_page}')
    return result
