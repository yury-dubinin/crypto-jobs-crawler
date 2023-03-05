from selenium.webdriver.common.by import By
from scrapeIt import ScrapeIt


class ScrapeBamboohr(ScrapeIt):
    def getJobs(self, driver, web_page) -> list():
        print(f'[bamboohr] Scrap page: {web_page}')
        driver.get(web_page)
        groupElements = driver.find_elements(By.CSS_SELECTOR, 'div[itemscope].row')
        print(f'[bamboohr] Found {len(groupElements)} jobs on {web_page}')
        result = []
        for elem in groupElements:
            linkElem = elem.find_element(By.CSS_SELECTOR, 'a')
            job_name_elem = elem.find_element(By.CSS_SELECTOR, 'a')
            locationElem = elem.find_element(By.CSS_SELECTOR, 'div[itemprop="jobLocation"]')
            jobUrl = linkElem.get_attribute('href')
            job_name = job_name_elem.text
            location = locationElem.text
            result.append((f'{job_name} From:{location}', jobUrl))
        print(f'[bamboohr] Scraped {len(result)} jobs from {web_page}')
        return result
