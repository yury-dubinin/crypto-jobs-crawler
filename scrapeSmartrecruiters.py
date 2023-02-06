from selenium.webdriver.common.by import By

def cleanLocation(location):
    if "remote" in location.lower():
        return "REMOTE"
    return location.lower()

def getJobs(driver, web_page):
    print(f'Scrap page: {web_page}')
    driver.get(web_page)
    more_links = driver.find_elements(By.XPATH, '//a[.="Show more jobs"]')
    print(f'Found more jobs: {len(more_links)}')
    # TODO: need to click that link
    # for link in more_links:
    #    link.click() -> Error: element click intercepted
    groupElements = driver.find_elements(By.XPATH, '//li[contains(@class,"opening-job") and not(contains(@class,"js-more-container"))]')
    print(f'Found jobs: {len(groupElements)}')
    result = []
    for elem in groupElements:
        linkElem = elem.find_element(By.CSS_SELECTOR, 'a')
        job_title = elem.find_element(By.CSS_SELECTOR, 'h4').text
        locationElem = elem.find_element(By.CSS_SELECTOR, 'span')
        jobUrl = linkElem.get_attribute('href')
        location = cleanLocation(locationElem.text)
        result.append((f'{job_title} From:{location}', jobUrl))
    print(f'Scraped {len(result)} jobs from {web_page}')
    return result
