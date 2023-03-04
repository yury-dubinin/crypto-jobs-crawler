from selenium.webdriver.common.by import By
from scrapeIt import ScrapeIt


class ScrapeRipple(ScrapeIt):
    name = 'RIPPLE'
    def getJobs(self, driver, web_page) -> list():
        print(f'[{self.name}] Scrap page: {web_page}')
        driver.get(web_page)
        groupElements = driver.find_elements(By.XPATH, '//p[contains(@class, "mb-6")]')
        print(f'[{self.name}] Found {len(groupElements)} jobs on {web_page}')
        result = []
        for elem in groupElements:
            linkElem = elem.find_element(By.CSS_SELECTOR, 'a')
            job_name_elem = elem.find_element(By.CSS_SELECTOR, 'a span')
            locationElem = elem.find_element(By.CSS_SELECTOR, 'a span span')
            jobUrl = linkElem.get_attribute('href')
            job_name = job_name_elem.text
            location = locationElem.text
            result.append((f'{job_name} From:{location}', jobUrl))
        print(f'[{self.name}] Scraped {len(result)} jobs from {web_page}')
        return result
