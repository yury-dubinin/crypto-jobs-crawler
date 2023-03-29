from dataclasses import dataclass
from scrapeIt import ScrapeIt


@dataclass(init=True)
class CompanyItem:
    company_name: str
    jobs_url: str
    scraper_type: ScrapeIt
    company_url: str
    company_type: str
