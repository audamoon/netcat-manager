import json
import re
from common.area import InputArea, TextArea
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class JSONElement:
    def add_element(self, target_id: int, origin: dict, json_to_add: dict):
        for element_key in origin:
            reg = re.search(r'([\d]+)',element_key)
            if reg != None:
                if int(reg[0]) == target_id:
                    origin[element_key].update(json_to_add)
                    return
            if isinstance(origin[element_key], dict):
                self.add_element(target_id, origin[element_key], json_to_add)

    def find_element(self, target_id: int, origin: dict):
        for element_key in origin:
            reg = re.search(r'([\d]+)',element_key)
            if reg != None:
                if int(reg[0]) == target_id:
                    yield origin[element_key]
            if isinstance(origin[element_key], dict):
                yield from self.find_element(target_id, origin[element_key])

    def delete_element(self, target_id: int, origin: dict):
        for element_key in origin:
            reg = re.search(r'([\d]+)',element_key)
            if reg != None:
                if reg[0] == target_id:
                    del origin[element_key]
                    return
            if isinstance(origin[element_key], dict):
                self.delete_element(target_id, origin[element_key])


class JSONController:
    def __init__(self) -> None:
        self.element = JSONElement()

    def load(self, filepath: str):
        with open(filepath, "r", encoding="UTF-8") as json_file:
            return json.load(json_file)

    def save(self, filepath: str, to_json: dict):
        with open(filepath, "w", encoding="UTF-8") as json_file:
            json.dump(to_json, json_file, ensure_ascii=False)

    def find_element(self, element_name: int, filepath: str):
        origin = self.load(filepath)
        return next(self.element.find_element(element_name, origin))

    def delete_element(self, element_name: int, filepath: str):
        origin = self.load(filepath)
        self.element.delete_element(element_name, origin)
        self.save(filepath, origin)

    def add_element(self, element_name: int, filepath: str, json_to_add: dict):
        origin = self.load(filepath)
        self.element.add_element(element_name, origin, json_to_add)
        self.save(filepath,origin)

# class IArea:
#     def input_area(self, *args): raise NotImplementedError
#     def edit_area(self, *args): raise NotImplementedError


# class TextArea(IArea):
#     def input_area(self, *args):
#         return super().input_area(*args)

#     def edit_area(self, *args):
#         return super().edit(*args)


# class InputAreat(IArea):
#     def input_area(self, *args):
#         return super().input_area(*args)

#     def edit_area(self, *args):
#         return super().edit(*args)


# class AreaController:
#     def __init__(self, area: IArea) -> None:
#         self.area = area

#     def edit_area(self, *args):
#         self.area.edit_area()

#     def input_area(self, *args):
#         self.area.input_area()


class AreaController:
    __json_controller = JSONController()

    def __init__(self,driver,frame) -> None:
        self.driver = driver
        self.__frame = frame
        self.__fields_dict = self.__json_controller.load("json/fields.json")

    def edit_inputs(self,old,new):
        self.__frame.to_frame()
        for input_element in self.__fields_dict['string_array']:
            input = InputArea(input_element["string_id"],self.driver)
            input.edit(old,new)

    def edit_textarea(self,old,new):
        self.__frame.to_frame()
        for textarea_element in self.__fields_dict['text_array']:
            textarea = TextArea(textarea_element["textarea_id"],self.driver)
            textarea.edit(old,new)

    def input_input(self,type,text):
        self.__frame.to_frame()
        for input_element in self.__fields_dict['string_array']:
            if input_element["type"] == "h1":
                input_h1 = InputArea(input_element["string_id"],self.driver)
            if input_element["type"] == "h2_input":
                input_h2 = InputArea(input_element["string_id"],self.driver)
        if type == "h1":
            input_h1.input(text)
        elif type == "h2_input":
            input_h2.input(text)

    def input_text(self,type,text):
        self.__frame.to_frame()
        for textarea_element in self.__fields_dict['text_array']:
            if textarea_element["type"] == "h1_text":
                textarea_h1 = TextArea(textarea_element["textarea_id"],self.driver)
            if textarea_element["type"] == "h2_text":
                textarea_h2 = TextArea(textarea_element["textarea_id"],self.driver)

        if type == "h1_text":
            textarea_h1.input(text)
        elif type == "h2_text":
            textarea_h2.input(text)
