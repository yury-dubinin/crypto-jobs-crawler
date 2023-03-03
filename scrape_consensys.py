from selenium.webdriver.common.by import By
from scrapeIt import ScrapeIt


class ScrapeConsensys(ScrapeIt):
    def getJobs(self, driver, web_page) -> list():
        print(f'[CONSENSYS] Scrap page: {web_page}')
        driver.get(web_page)
        groupElements = driver.find_elements(By.XPATH, '//div[@id="careers"]//div[contains(@class, "careersSectionItem_itemOuter")]')
        print(f'[CONSENSYS] Found {len(groupElements)} jobs on {web_page}')
        result = []
        for elem in groupElements:
            linkElem = elem.find_element(By.CSS_SELECTOR, 'a')
            job_name_elem = elem.find_element(By.CSS_SELECTOR, 'h5')
            locationElem = elem.find_element(By.XPATH, '//div[contains(@class, "careersSectionItem_location")]')
            jobUrl = linkElem.get_attribute('href')
            job_name = job_name_elem.text
            location = locationElem.text
            result.append((f'{job_name} From:{location}', jobUrl))
        print(f'[CONSENSYS] Scraped {len(result)} jobs from {web_page}')
        return result
