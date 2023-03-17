import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from scrapeIt import ScrapeIt


def show_more(driver, locator):
    print(f'[workable] Show more jobs..')
    show_more_button = driver.find_elements(By.CSS_SELECTOR, locator)
    if len(show_more_button) > 0:
        driver.execute_script("arguments[0].scrollIntoView(true);", show_more_button[0])
        time.sleep(5)
        driver.execute_script("arguments[0].click();", show_more_button[0])
        time.sleep(5)
        show_more(driver, locator)


def clean_location(location):
    return ' '.join(set(([x.strip() for x in location.split(',')])))


class ScrapeWorkable(ScrapeIt):
    name = 'workable'.upper()

    def getJobs(self, driver, web_page) -> list():
        print(f'[{self.name}] Scrap page: {web_page}')
        driver.get(web_page)
        driver.implicitly_wait(20)
        wait = WebDriverWait(driver, 20)
        show_more_locator = 'button[data-ui="load-more-button"]'
        job_root_locator = 'li[data-ui^="job"]'
        show_more_buttons = driver.find_elements(By.CSS_SELECTOR, show_more_locator)
        if len(show_more_buttons) > 0:
            print(f'[{self.name}] Show more Jobs button found..')
            show_more(driver, show_more_locator)
        group_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, job_root_locator)))
        print(f'[{self.name}] Found {len(group_elements)} jobs on {web_page}')
        result = []
        driver.implicitly_wait(5)
        for elem in group_elements:
            link_elem = elem.find_element(By.CSS_SELECTOR, 'a')
            remote_elem = elem.find_elements(By.CSS_SELECTOR, '[data-ui="job-remote"]')
            job_name_elem = elem.find_element(By.CSS_SELECTOR, '[data-ui="job-title"],[data-id="job-item"]')
            location_elem = elem.find_element(By.CSS_SELECTOR, 'span[data-ui="job-location"]')
            job_url = link_elem.get_attribute('href')
            job_name = job_name_elem.text
            location = location_elem.text
            if len(remote_elem) > 0:
                location = location + ' REMOTE'
            result.append((f'{job_name} From:{clean_location(location)}', job_url))
        print(f'[{self.name}] Scraped {len(result)} jobs from {web_page}')
        return result
