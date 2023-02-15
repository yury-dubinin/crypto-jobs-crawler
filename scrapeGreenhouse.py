from selenium.webdriver.common.by import By

def cleanLocation(location):
    return set(([x.strip() for x in location.split(',')]))

def getJobs(driver, web_page):
    print(f'[GREENHOUSE] Scrap page: {web_page}')
    driver.get(web_page)
    iframe = driver.find_elements(By.TAG_NAME, 'iframe')
    if len(iframe)>0:
        print('iFrame detected..')
        driver.switch_to.frame(iframe[0])
    groupElements = driver.find_elements(By.CSS_SELECTOR, 'div [class="opening"]')
    print(f'[GREENHOUSE] Found {len(groupElements)} jobs.')
    result = []
    for elem in groupElements:
        linkElem = elem.find_element(By.CSS_SELECTOR, 'a')
        locationElem = elem.find_element(By.CSS_SELECTOR, 'span')
        jobUrl = linkElem.get_attribute('href')
        location = cleanLocation(locationElem.text)
        result.append((f'{linkElem.text} From:{location}', jobUrl))
    print(f'[GREENHOUSE] Scraped {len(result)} jobs from {web_page}')
    return result
