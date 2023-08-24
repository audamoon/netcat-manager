from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from base.frames import LeftFrame
# Finder

class IFinder:
    def get_ul_by_id(self, el_id: int, driver: Chrome,
                     frame): raise NotImplementedError

class SiteListFinder(IFinder):
    def get_ul_by_id(self, el_id: int, driver: Chrome, frame: LeftFrame):
        frame.to_frame()
        return driver.find_element(By.XPATH, f"//ul[@id='siteTree_site-{el_id}_children']")


class SubsListFinder(IFinder):
    def get_ul_by_id(self, el_id: int, driver: Chrome, frame: LeftFrame):
        frame.to_frame()
        return driver.find_element(By.XPATH, f"//ul[@id='siteTree_sub-{el_id}_children']")
