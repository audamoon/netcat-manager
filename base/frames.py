from undetected_chromedriver import Chrome
from common.block import ModalWindow,MenuSwitcher
from  common.controllers import AreaController
from time import sleep
from selenium.webdriver.common.by import By


class IFrame:
    def to_frame(self): raise NotImplementedError

class Frame(IFrame):
    def __init__(self, driver: Chrome):
        self.driver = driver

    def to_frame(self):
        self.driver.switch_to.frame(self._frame_name)

#Наследники

class DefaultFrame(Frame):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__modal = ModalWindow(self.driver)
        self.__menu = MenuSwitcher(self.driver)
        self.area = AreaController(self.driver, self)

    def to_frame(self):
        self.driver.switch_to.default_content()
    
    def save_modal(self):
        self.to_frame()
        self.__modal.save()
    
    def open_modal(self):
        self.to_frame()
        self.driver.find_element(By.XPATH, "//div[@class='save']").click()


class LeftFrame(Frame):
    _frame_name = "treeIframe"

    def __init__(self, driver,__default_frame) -> None:
        super().__init__(driver)
        self.__default = __default_frame

    def to_frame(self):
        self.__default.to_frame()
        return super().to_frame()


class CenterFrame(Frame):
    _frame_name = "mainViewIframe"

    def __init__(self, driver,__default_frame) -> None:
        super().__init__(driver)
        self.__default = __default_frame
        self.__modal = ModalWindow(self.driver)

    def to_frame(self):
        self.__default.to_frame()
        return super().to_frame()

    def open_modal(self):
        self.to_frame()
        self.__modal.open()