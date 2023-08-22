from base.netcat_mgr import NetcatManager
from selenium_mgr import SeleniumChromeProfile
from selenium.webdriver.common.by import By
from time import sleep
from common.subdivion import SubdivisionCollector, WebReader, SiteListFinder, SubsListFinder
from common.controllers import JSONController

driver = SeleniumChromeProfile().get_driver()
netcat = NetcatManager(driver=driver)

netcat.set_main_url("https://garmonia-stacionar.ru/netcat/admin/#site.map(1)")
site_finder = SiteListFinder()
web_reader = WebReader(driver)
sub_finder = SubsListFinder()
controller = JSONController()
collector = SubdivisionCollector(site_finder, driver, netcat.get_main_url(), netcat.left)
collector.save_subs(WebReader(driver), controller)
