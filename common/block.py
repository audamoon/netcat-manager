from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from  common.controllers import JSONController

class Block:
    driver = None

    def wait_then_click(self,_xpath):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, _xpath)))
        self.driver.find_element(By.XPATH,_xpath).click()

class ModalWindow(Block):
    __json_controller = JSONController()

    def __init__(self, driver) -> None:
        self.driver = driver

    def open(self):
        open_btn_xpath = "//i[@class='nc-icon nc--edit']/parent::a"
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, open_btn_xpath)))
        self.driver.find_element(By.XPATH,open_btn_xpath).click()

    def save(self):
        save_btn_xpath = "//div[@class='nc-modal-dialog-footer']/button[text()='Сохранить']"
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, save_btn_xpath)))
        self.driver.find_element(By.XPATH, save_btn_xpath).click()

    def collect_fields():
        pass

    def choose_fields():
        pass


class MenuSwitcher(Block):
    def __init__(self, driver) -> None:
        self.driver = driver
