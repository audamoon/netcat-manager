from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from common.controllers import JSONElement, JSONController
from undetected_chromedriver import Chrome
from time import sleep

# Finder

class IFinder:
    def get_ul_by_id(self, el_id: int, driver: Chrome,
                     url: str, frame): raise NotImplementedError


class SiteListFinder(IFinder):
    def get_ul_by_id(self, el_id: int, driver: Chrome, url: str, frame):
        driver.get(url)
        sleep(3)
        frame.to_frame() #НАДО РЕАЛИЗОВАТЬ LEFT FRAME КАК КЛАСС НИЗКОГО УРОВНЯ
        return driver.find_element(By.XPATH, f"//ul[@id='siteTree_site-{el_id}_children']")


class SubsListFinder(IFinder):
    def get_ul_by_id(self, el_id: int, driver: Chrome, url: str, frame):
        driver.get(url)
        sleep(3)
        frame.to_frame()
        return driver.find_element(By.XPATH, f"//ul[@id='siteTree_sub-{el_id}_children']")


# Reader

class IReader:
    def get_data(self) -> dict: raise NotImplementedError


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
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver

    def set_element(self, chrome_element):
        self.element = chrome_element

    def get_data(self) -> dict:
        title = self.__get_title()
        to_json = {}
        to_json[title] = {}
        to_json[title].update(
            {
                "type": self.__get_type(),
                "url": self.__get_link()
            }
        )
        return to_json

    def __get_link(self) -> str:
        self.element.click()
        return self.driver.current_url
    
    def __get_title(self) -> str:
        return self.element.get_attribute("title")

    def __get_type(self) -> str:
        element_class = self.element.get_attribute("class")
        if "unactive" in element_class:
            return "unactive"
        if "active" in element_class:
            return "active"
        else:
            return "undefined"

# Subdivision


class Subdivsion:
    pass

# ".//img[@alt='Раскрыть список']"
# ".//a[@title = '{name}']/parent::li"


class SubdivisionCollector:
    def __init__(self, finder: IFinder, driver: Chrome, url: str, frame, ) -> None:
        self.driver = driver
        self.finder = finder
        self.url = url
        self.start_element = self.finder.get_ul_by_id(
            el_id=1, driver=self.driver, url=self.url, frame=frame)

    def save_subs(self, reader: IReader, json_controller: JSONController):
        to_json = {}

        for element in self.collect_all_elements():
            reader.set_element(element)
            to_json.update(reader.get_data())
        
        json_controller.save("json/subdivisions.json",to_json)
        

    def collect_all_elements(self):
        return self.start_element.find_elements(By.XPATH,".//a[contains(@class,'menu_left_a')]")

  
        