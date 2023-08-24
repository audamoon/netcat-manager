from selenium.webdriver.common.by import By
import re
import os
from common.controllers import JSONElement, JSONController
from undetected_chromedriver import Chrome
import common.finders as finders
import common.readers as readers
from base.frames import LeftFrame
from time import sleep
# Subdivision


class Subdivsion:
    pass

# ".//img[@alt='Раскрыть список']"
# ".//a[@title = '{name}']/parent::li"


class SubdivisionCollector:
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver

    def set_options(self, frame: LeftFrame = None, reader: readers.IReader = None, finder: finders.IFinder = None, link=False, el_id: int = None, json_controller: JSONController = None):
        self.frame = frame
        self.reader = reader
        self.finder = finder
        self.el_id = el_id
        self.link = link
        self.json_controller = JSONController()

    def __get_link(self):
        if not self.link:
            url = self.json_controller.find_element(self.el_id,"json/subdivisions.json")["url"]
            self.driver.get(url)
        else:
            self.driver.get(self.link)

    def set_start_element(self):
        self.__get_link()
        sleep(3)
        self.frame.to_frame()
        self.start_element = self.finder.get_ul_by_id(
            el_id=self.el_id, driver=self.driver, frame=self.frame)

    def __collect_children_to_json(self):
        self.frame.to_frame()

        children = self.start_element.find_elements(
            By.XPATH, ".//a[contains(@class,'menu_left_a')]")

        to_json = {}

        for child in children:
            self.reader.set_element(child)
            to_json.update(self.reader.get_data())

        return to_json

    def save_subs(self):
        to_json = self.__collect_children_to_json()
        self.json_controller.save("json/subdivisions.json", to_json)

    def save_as_children(self):
        children = self.__collect_children_to_json()
        to_json = {
            "subdivisions":children
        }
        self.json_controller.add_element(self.el_id,"json/subdivisions.json",to_json)

class SubdivisionController():
    def write_subs_to_delete(self):
        os.startfile("subdivision_to_delete.txt")

    def delete_subs(self, controller: JSONController, source: str):
        with open(source, "r", encoding="UTF-8") as f:
            sub_names = f.readlines()
        for name in sub_names:
            try:
                to_delete = re.search(r'([\d]+)', name.strip())[0]
                controller.delete_element(to_delete, "json/subdivisions.json")
            except:
                pass
            