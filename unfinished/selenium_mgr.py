# Other
from typing import Any
import undetected_chromedriver as uc
import os


class SeleniumChromeProfile():

    __user_path = (os.environ['LOCALAPPDATA'] + "\\Google\\Chrome\\User Data")

    def __init__(self):
        self.__options = uc.ChromeOptions()
        self.__options.add_argument(f"--user-data-dir={self.__user_path}")
        self.driver = uc.Chrome(
            browser_executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe",
            options=self.__options)
    
    def __call__(self):
        return self.driver