from common.controllers import JSONElement, JSONController
from undetected_chromedriver import Chrome
import re
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
                "url": self.__get_link(),
                "id": re.search(r'([\d]+)',title)[0]
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