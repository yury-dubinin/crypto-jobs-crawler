from selenium.webdriver.common.by import By
from src.scrape_it import ScrapeIt


def clean_location(location):
    if 'remote' in location.lower() or 'global' in location.lower():
        return {"REMOTE"}
    return set(([x.strip() for x in location.split(',')]))


class ScrapeSmartrecruiters(ScrapeIt):
    def getJobs(self, driver, web_page) -> list():
        print(f'Scrap page: {web_page}')
        driver.get(web_page)
        more_links = driver.find_elements(By.XPATH, '//a[.="Show more jobs"]')
        print(f'Found more jobs: {len(more_links)}')
        # TODO: need to click that link
        # for link in more_links:
        #    link.click() -> Error: element click intercepted
        group_elements = driver.find_elements(By.XPATH,
                                              '//li[contains(@class,"opening-job") and not(contains(@class,"js-more-container"))]')
        print(f'Found jobs: {len(group_elements)}')
        result = []
        for elem in group_elements:
            link_elem = elem.find_element(By.CSS_SELECTOR, 'a')
            job_title = elem.find_element(By.CSS_SELECTOR, 'h4').text
            location_elem = elem.find_element(By.CSS_SELECTOR, 'span')
            job_url = link_elem.get_attribute('href')
            location = clean_location(location_elem.text)
            result.append((f'{job_title} From:{location}', job_url))
        print(f'Scraped {len(result)} jobs from {web_page}')
        return result
