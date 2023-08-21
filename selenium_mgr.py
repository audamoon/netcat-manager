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

# class SeleniumManager:

#     def __init__(self) -> None:
#         self.driver = SeleniumChromeProfile()

#     def wait_until_presence(self,__xpath,__time=600):
#         WebDriverWait(self,__time).until(EC.presence_of_element_located((By.XPATH, __xpath)))

#     def find_element_by_xpath(self,__xpath):
#         return self.find_element(By.XPATH,__xpath)

#     def find_all_by_xpath(self,__xpath):
#         return self.find_elements(By.XPATH,__xpath)
