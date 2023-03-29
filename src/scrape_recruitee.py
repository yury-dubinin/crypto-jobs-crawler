from selenium.webdriver.common.by import By
from src.scrape_it import ScrapeIt


def clean_location(location):
    if 'remote' in location.lower() or 'global' in location.lower():
        return {"REMOTE"}
    return set(([x.strip() for x in location.split(',')]))


class ScrapeRecruitee(ScrapeIt):
    def getJobs(self, driver, web_page) -> list():
        print(f'[RECRUITEE] Scrap page: {web_page}')
        driver.get(web_page)
        group_elements = driver.find_elements(By.CSS_SELECTOR, 'div [class="job"]')
        print(f'[RECRUITEE] Found {len(group_elements)} jobs.')
        result = []
        for elem in group_elements:
            link_elem = elem.find_element(By.CSS_SELECTOR, '[class="job-title"] a')
            location_elem = elem.find_element(By.CSS_SELECTOR, '[class="job-location"]')
            job_url = link_elem.get_attribute('href')
            location = clean_location(location_elem.text)
            result.append((f'{link_elem.text} From:{location}', job_url))
        print(f'[RECRUITEE] Scraped {len(result)} jobs from {web_page}')
        return result
