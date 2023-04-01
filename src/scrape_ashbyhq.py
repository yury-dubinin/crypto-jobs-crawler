from selenium.webdriver.common.by import By
from src.scrape_it import ScrapeIt


def clean_location(location):
    locations = list(filter(None, ([x.strip() for x in location.split('•')])))
    result = locations[1]
    return result.strip()


class ScrapeAshbyhq(ScrapeIt):
    name = 'ashbyhq'

    def getJobs(self, driver, web_page) -> list():
        print(f'[{self.name}] Scrap page: {web_page}')
        driver.get(web_page)
        group_elements = driver.find_elements(By.CSS_SELECTOR, 'a[class*="container_"]')
        job_location_locator = 'div p'
        print(f'[{self.name}] Found {len(group_elements)} jobs on {web_page}')
        result = []
        for elem in group_elements:
            link_elem = elem
            job_name_elem = elem.find_element(By.CSS_SELECTOR, 'h3')
            location_elem = elem.find_element(By.CSS_SELECTOR, job_location_locator)
            job_url = link_elem.get_attribute('href')
            job_name = job_name_elem.text
            location = location_elem.text
            cleaned_location = location.replace('\n', ', ')
            result.append((f'{job_name} From:{clean_location(cleaned_location)}', job_url))
        print(f'[{self.name}] Scraped {len(result)} jobs from {web_page}')
        return result
