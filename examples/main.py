from base.netcat_mgr import NetcatManager
from modules.selenium.selenium_mgr import SeleniumChromeProfile
from common.readers import WebReader
from common.finders import SiteListFinder, SubsListFinder
from common.subdivion import SubdivisionCollector
from common.controllers import JSONController
from time import sleep

driver = SeleniumChromeProfile().get_driver()
netcat = NetcatManager(driver)
collector_site = SubdivisionCollector(driver)
collector_sub = SubdivisionCollector(driver)


netcat.set_main_url("https://garmonia-stacionar.ru/netcat/admin/#site.map(1)")


def collect_main():
    collector_site.set_options(finder=SiteListFinder(), reader=WebReader(driver),
                               frame=netcat.left, el_id=1, json_controller=JSONController(), link=netcat.get_main_url())
    collector_site.set_start_element()
    collector_site.save_subs()


def collect_service():
    collector_sub.set_options(finder=SubsListFinder(), reader=WebReader(driver),
                              frame=netcat.left, el_id=20, json_controller=JSONController())
    collector_sub.set_start_element()
    collector_sub.save_as_children()


def collect_services():
    subs = [90, 101, 104, 131, 151, 152, 164, 166]

    for el in subs:
        collector_sub.set_options(finder=SubsListFinder(), reader=WebReader(driver),
                                  frame=netcat.left, el_id=el, json_controller=JSONController())
        collector_sub.set_start_element()
        collector_sub.save_as_children()


def load_texts():
    all_texts = JSONController().load("json/result.json")
    for i in range(len(all_texts)):
        try:
            with open("logs/log.txt", "a", encoding="UTF-8") as f:
                f.write(f"НАЧИНАЮ ЗАПОЛНЯТЬ text-{i}\n")
            text = all_texts[f"text-{i}"]
            h1_block = text["h1_block"]
            for h1 in h1_block:
                h1_tag = h1.replace("<h1>", "").replace("</h1>", "")
                h1_text = h1_block[h1]
            h2_blocks = text["h2_blocks"]
            h2_text = " "
            for h2 in h2_blocks:
                h2_text = h2_text + h2
                h2_text = h2_text + h2_blocks[h2]
            sub_id = text["sub_id"]
            url = JSONController().find_element(
                int(sub_id), "json/subdivisions.json")["url"]
            with open("logs/log.txt", "a", encoding="UTF-8") as f:
                f.write(
                    f"АЙДИ РАЗДЕЛА {sub_id}, ССЫЛКА {url}\nЗАГОЛОВОК РАЗДЕЛА {h1_tag}\n")
            driver.get(url)
            sleep(2)
            try:
                netcat.center.open_modal()
            except:
                netcat.default.open_modal()
            netcat.default.area.input_input("h1", h1_tag)
            netcat.default.area.input_text("h1_text", h1_text)
            netcat.default.area.input_text("h2_text", h2_text)
            netcat.default.save_modal()
            sleep(1)
        except:
            with open("logs/log.txt", "a", encoding="UTF-8") as f:
                f.write(f"ОШИБКА ЗАПОЛНЕНИЯ С text-{i}\n")




collect_main()

collect_service()

collect_services()

load_texts()
