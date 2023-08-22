from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.controllers import JSONElement, JSONController
from undetected_chromedriver import Chrome


###########################     Finder

class IFinder:
    def get_ul_by_id(self, el_id:int, driver: Chrome, url: str): raise NotImplementedError


class SiteListFinder(IFinder):
    def get_ul_by_id(self, el_id: int, driver: Chrome, url: str):
        driver.get(url)
        return driver.find_element(By.XPATH, f"//ul[@id='siteTree_site-{el_id}_children']")


class SubsListFinder(IFinder):
    def get_ul_by_id(self, el_id: int, driver: Chrome, url: str):
        driver.get(url)
        return driver.find_element(By.XPATH, f"//ul[@id='siteTree_sub-{el_id}_children']" )


###########################     Reader

class IReader:
    def get_data(self): raise NotImplementedError

class Reader(IReader):
    def get_data(self):
        pass


class JsonReader(Reader): 
    def __init__(self, element_name: str, filepath: str, json_controller: JSONController) -> None:
        self.element_name = element_name
        self.filepath = filepath
        self.json_controller = json_controller

    def get_data(self) -> dict:
        return self.json_controller.find_element(JSONElement, self.element_name, self.filepath)
        

class WebReader(Reader): 
    def __init__(self, driver:Chrome) -> None:
        self.driver = Chrome

    def set_element(self, chrome_element):
        self.element = chrome_element

    def get_data(self) -> dict:
        to_json = {}
        to_json[self.__get_title].update(
            {
                "type":self.__get_type(),
                "url":self.__get_link()
            }
        )
        return to_json

    def __get_link(self) -> str:
        self.element.click()
        return self.driver.current_url

    def __get_title(self) -> str:
        return self.element.get_attribute("title")

    def __get_type(self) -> str:
        element_class = self.element.get_attribure("class")
        if "active" in element_class:
            return "active"
        if "unactive" in element_class:
            return "unactive"
        else:
            return "undefined"

###########################     Subdivision

class Subdivsion:
    pass

# ".//img[@alt='Раскрыть список']"
# ".//a[@title = '{name}']/parent::li"

class SubdivisionCollector:
    def __init__(self, finder: IFinder, driver:Chrome, url: str) -> None:
        self.driver = driver
        self.finder = finder
        self.url = url
        self.start_element = self.finder.get_ul_by_id(1, self.driver, self.url)
        
    def get_info(self, reader: IReader):
        for element in self.collect_all_elements():
            reader.set_element(element)
            return reader.get_data()

    def collect_all_elements(self):
        return self.start_element.find_elements(By.XPATH(".//a[contains(@class,'menu_left_a')]"))
    
