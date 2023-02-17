from selenium.webdriver.common.by import By
from scrapeIt import ScrapeIt


def cleanLocation(location):
    return set(([x.strip() for x in location.split(',')]))

class ScrapeLever(ScrapeIt):
    def getJobs(self, driver, web_page):
        print(f'[LEVER] Scrap page: {web_page}')
        driver.get(web_page)
        groupElements = driver.find_elements(By.CSS_SELECTOR, 'a[class="posting-title"]')
        print(f'[LEVER] Found {len(groupElements)} jobs.')
        result = []
        for elem in groupElements:
            linkElem = elem.find_element(By.CSS_SELECTOR, '[data-qa="posting-name"]')
            locationElem = elem.find_element(By.CSS_SELECTOR, 'span')
            jobUrl = elem.get_attribute('href')
            location = cleanLocation(locationElem.text)
            result.append((f'{linkElem.text} From:{location}', jobUrl))
        print(f'[LEVER]  Scraped {len(result)} jobs from {web_page}')
        return result
