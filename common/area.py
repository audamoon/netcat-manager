from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#AREAS
class Area:
    _type = None
    _text_attribute = None

    def __init__(self, _id, driver) -> None:
        self._id = _id
        self.driver = driver
        self.__get_DOM_elements()

    def __get_DOM_elements(self):
        _parent_xpath = f"//span[@id='{self._id}']/parent::div"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, _parent_xpath)))
        self._parent_element = self.driver.find_element(
            By.XPATH, _parent_xpath)
        self._DOM_element = self._parent_element.find_element(
            By.XPATH, f"./{self._type}")
        self._inner_text = self._DOM_element.get_attribute(
            f"{self._text_attribute}")

    def edit(self, old, new):
        if type(old) is list and type(new) is list:
            if bool(self._inner_text) == False:
                return
            self.__edit_from_list(old, new)
            self.input(self._inner_text)
        elif type(old) is str and type(new) is str:
            if bool(self._inner_text) == False:
                return
            self.__edit_from_str(old, new)
            self.input(self._inner_text)

    def __edit_from_list(self, old_input_list, new_input_list):
        for i in range(len(old_input_list)):
            self._inner_text = self._inner_text.replace(
                old_input_list[i], new_input_list[i])

    def __edit_from_str(self, old_input_str, new_input_str):
        self._inner_text = self._inner_text.replace(
            old_input_str, new_input_str)

    def input(self, new):
        self._DOM_element.click()
        self._DOM_element.clear()
        self._DOM_element.send_keys(new)


class InputArea(Area):
    _type = "input"
    _text_attribute = "value"

    def __init__(self, _id, driver) -> None:
        super().__init__(_id, driver)

    def edit(self, old, new):
        super().edit(old, new)

    def input(self, new):
        return super().input(new)


class TextArea(Area):
    _type = "textarea"
    _text_attribute = "textContent"

    def __init__(self, _id, driver) -> None:
        super().__init__(_id, driver)
        self.__show_source_btn = self._parent_element.find_element(
            By.XPATH, ".//a[@class='cke_button cke_button__source cke_button_off']")

    def edit(self, old, new):
        super().edit(old, new)

    def input(self, new):
        self.__show_source_btn.click()
        self._DOM_element = self._parent_element.find_element(
            By.XPATH, ".//textarea[@dir]")
        super().input(new)
        self.__show_source_btn.click()