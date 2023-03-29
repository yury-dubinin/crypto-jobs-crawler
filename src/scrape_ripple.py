from selenium.webdriver.common.by import By
from src.scrape_it import ScrapeIt


class ScrapeRipple(ScrapeIt):
    name = 'RIPPLE'

    def getJobs(self, driver, web_page) -> list():
        print(f'[{self.name}] Scrap page: {web_page}')
        driver.get(web_page)
        group_elements = driver.find_elements(By.XPATH, '//p[contains(@class, "mb-6")]')
        print(f'[{self.name}] Found {len(group_elements)} jobs on {web_page}')
        result = []
        for elem in group_elements:
            link_elem = elem.find_element(By.CSS_SELECTOR, 'a')
            job_name_elem = elem.find_element(By.CSS_SELECTOR, 'a span')
            location_elem = elem.find_element(By.CSS_SELECTOR, 'a span span')
            job_url = link_elem.get_attribute('href')
            job_name = job_name_elem.text
            location = location_elem.text
            result.append((f'{job_name} From:{location}', job_url))
        print(f'[{self.name}] Scraped {len(result)} jobs from {web_page}')
        return result
