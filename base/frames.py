from typing import Any
from common.block import ModalWindow,MenuSwitcher
from controllers.controllers import AreaController, SubdivisionCollector
from time import sleep

#Класс-родитель
class Frame:
    def __init__(self, driver) -> None:
        self.driver = driver

    def to_frame(self):
        self.driver.switch_to.frame(self._frame_name)

#Наследники
class LeftFrame(Frame):
    _frame_name = "treeIframe"

    def __init__(self, driver,__default_frame) -> None:
        super().__init__(driver)
        self.__default = __default_frame
        # self.subdivision = Subdivison

    def to_frame(self):
        self.__default.to_frame()
        return super().to_frame()

class DefaultFrame(Frame):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__modal = ModalWindow(self.driver)
        self.__menu = MenuSwitcher(self.driver)
        self.area = AreaController(self.driver,self)

    def to_frame(self):
        self.driver.switch_to.default_content()

    def switch_tab(self,__tab_name):
        self.to_frame()
        self.__menu.switch(__tab_name)
    
    def save_modal(self):
        self.to_frame()
        self.__modal.save()

class CenterFrame(Frame):
    _frame_name = "mainViewIframe"

    def __init__(self, driver,__default_frame) -> None:
        super().__init__(driver)
        self.__default = __default_frame
        self.__modal = ModalWindow(self.driver)
        self.__menu = MenuSwitcher(self.driver)


    def to_frame(self):
        self.__default.to_frame()
        return super().to_frame()

    def open_modal(self):
        self.to_frame()
        self.__modal.open()