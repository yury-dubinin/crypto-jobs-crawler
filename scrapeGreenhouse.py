from selenium.webdriver.common.by import By
from scrapeIt import ScrapeIt


class ScrapeGreenhouse(ScrapeIt):
    name = 'GREENHOUSE'
    def getJobs(self, driver, web_page) -> list():
        print(f'[{self.name}] Scrap page: {web_page}')
        driver.get(web_page)
        iframe = driver.find_elements(By.TAG_NAME, 'iframe')
        if len(iframe)>0:
            print(f'[{self.name}] iFrame detected..')
            driver.switch_to.frame(iframe[0])
        group_elements = driver.find_elements(By.CSS_SELECTOR, 'div [class="opening"]')
        print(f'[{self.name}] Found {len(group_elements)} jobs.')
        result = []
        for elem in group_elements:
            link_elem = elem.find_element(By.CSS_SELECTOR, 'a')
            location_elem = elem.find_element(By.CSS_SELECTOR, 'span')
            job_url = link_elem.get_attribute('href')
            location = set(([x.strip() for x in location_elem.text.split(',')]))
            result.append((f'{link_elem.text} From:{location}', job_url))
        print(f'[{self.name}] Scraped {len(result)} jobs from {web_page}')
        return result
