from base.netcat_mgr import NetcatManager
from selenium_mgr import SeleniumChromeProfile

from selenium.webdriver.common.by import By
main
from time import sleep
from controllers.controllers import AreaController, SubdivisionCollector

driver = SeleniumChromeProfile()
nc = NetcatManager(driver=driver.driver)


nc.set_main_url("https://garmonia-stacionar.ru/netcat/admin/#site.map(1)")
nc.open_netcat()
nc.left.to_frame()

collector = SubdivisionCollector(driver.driver,1)
sleep(10)
main
