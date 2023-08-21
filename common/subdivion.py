from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# SUBDIVISIONS


class HasMainElement:
    def __init__(self, main_id):
        self.set_main_menu_el(main_id)

    def set_main_menu_el(self, id):
        main_menu_id = id
        main_xpath = f"//ul[@id='siteTree_site-{main_menu_id}_children']"
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, main_xpath)))
        try:
            self.main_menu_el = self.driver.find_element(
            By.XPATH, main_xpath)
        except:
            print(f"Гланый элемент с id = {id} не найден")


class Subdivision():
    def __init__(self,driver, name, url, main_element) -> None:
        self.driver = driver
        self.name = name
        self.url = url
        #id regexp: "[0-9]{1,}"g
        try:
            self.li_element = self.main_menu_el.find_element(
                By.XPATH, f".//a[@title = '{self.name}']/parent::li")
        except:
            print(f"Элемент: '{name}' не найден")

    def expand(self):
        try:
            self.li_element.driver.find_element(
                By.XPATH, ".//img[@alt='Раскрыть список']").click()
        except:
            return
        
    def open_url(self):
        self.driver.get(self.url)

    def click():
        pass


class SubdivisionCollector(HasMainElement):
    def __init__(self, driver, main_id):
        self.driver = driver
        super().__init__(main_id)


    def collect_all_names(self):
        els = self.main_menu_el.find_elements(By.XPATH,".//a[contains(@class,'menu_left_a')]")
        for el in els:
            print(el.get_attribute("title"),end=" ")

    def collect_all_url():
        pass

    def expand_all(self):
        try:
            all_expand_btns = self.main_menu_el.find_elements(
                By.XPATH, ".//img[@alt='Раскрыть список']")
            for btn in all_expand_btns:
                btn.click()
        except:
            return

