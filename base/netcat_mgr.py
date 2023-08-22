import base.frames as frames
from time import sleep

class NetcatManager:
    def __init__(self,driver) -> None:
        self.driver = driver
        self.default = frames.DefaultFrame(self.driver)
        self.left = frames.LeftFrame(self.driver,self.default)
        self.center = frames.CenterFrame(self.driver,self.default)

    def set_main_url(self,__main_url):
        self.__main_url = __main_url

    def get_main_url(self) -> str:
        return self.__main_url
        
        
    def open(self):
        self.driver.get(self.__main_url)
