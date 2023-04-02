from selenium.webdriver.common.by import By
from src.scrape_it import ScrapeIt


def clean_location(location):
    locations = set(filter(None, ([x.strip() for x in location.split(',')])))
    if len(locations) == 1:
        return next(iter(locations))
    joined = ' '.join(locations).lower()
    if joined.count('remote') > 1:
        return joined.replace('remote', '', 1)
    return joined.strip().strip('-')


class ScrapeBamboohr(ScrapeIt):
    name = 'bamboohr'

    def getJobs(self, driver, web_page) -> list():
        print(f'[{self.name}] Scrap page: {web_page}')
        driver.get(web_page)
        driver.implicitly_wait(5)
        group_elements = driver.find_elements(By.CSS_SELECTOR, 'div[itemscope].row')
        job_location_locator = 'div[itemprop="jobLocation"]'
        if len(group_elements) == 0:
            group_elements = driver.find_elements(By.XPATH, '//li/div/a/..')
            job_location_locator = 'div[class="jss-e78"]'
        print(f'[{self.name}] Found {len(group_elements)} jobs on {web_page}')
        result = []
        for elem in group_elements:
            link_elem = elem.find_element(By.CSS_SELECTOR, 'a')
            job_name_elem = elem.find_element(By.CSS_SELECTOR, 'a')
            location_elem = elem.find_element(By.CSS_SELECTOR, job_location_locator)
            job_url = link_elem.get_attribute('href')
            job_name = job_name_elem.text
            location = location_elem.text
            cleaned_location = location.replace('\n', ', ')
            result.append((f'{job_name} From:{clean_location(cleaned_location)}', job_url))
        print(f'[{self.name}] Scraped {len(result)} jobs from {web_page}')
        return result
