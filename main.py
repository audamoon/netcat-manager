from base.netcat_mgr import NetcatManager
from selenium_mgr import SeleniumChromeProfile
from selenium.webdriver.common.by import By
from time import sleep
from common.subdivion import SubdivisionCollector, WebReader, SiteListFinder


driver = SeleniumChromeProfile().get_driver()
netcat = NetcatManager(driver=driver)


netcat.set_main_url("https://garmonia-stacionar.ru/netcat/admin/#site.map(1)")
netcat.open()
sleep(5)
netcat.left.to_frame()

site_finder = SiteListFinder
web_reader = WebReader(driver=driver)

collector = SubdivisionCollector(site_finder , driver=driver, url=netcat.get_main_url())

collector.get_info(WebReader(driver=driver))