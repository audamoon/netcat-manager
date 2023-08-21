import json
from common.area import InputArea, TextArea
from common.subdivion import Subdivision, SubdivisionCollector

class JSONController:
    def __init__(self, __filepath) -> None:
        self.__filepath = __filepath

    def load(self):
        with open(self.__filepath, "r", encoding="UTF-8") as json_file:
            return json.load(json_file)

    def save(self, to_json):
        with open(self.__filepath, "w", encoding="UTF-8") as json_file:
            json.dump(to_json, json_file, ensure_ascii=False)


class AreaController:
    __json_controller = JSONController("json/fields.json")
    
    def __init__(self,driver,frame) -> None:
        self.driver = driver
        self.__frame = frame
        self.__fields_dict = self.__json_controller.load()

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
            
class SubdivisonController:
    def __init__(self) -> None:
        pass
