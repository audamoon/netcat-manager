# import os
# os.startfile("subdivision_to_delete.txt")
# print("Добавьте в открывшийся файл подразделы, которые НЕ нужно заполнять")
#"(([\d]+[\.])( *[a-я]+ *)+)"giu - регулярка

from common.controllers import JSONController, JSONElement
# import common.controllers as controllers
# controller = controllers.JSONController()
controller = JSONController()
# def func(target,origin) -> None:
#     for element_key in origin:
#         if element_key == target:
#             del origin[element_key]
#             return
#         if isinstance(origin[element_key], dict):
#             func(target,origin[element_key])

# def func(target:str,origin:dict):
#     for element_key in origin:
#         if element_key == target:
#             yield origin[element_key]
#         if isinstance(origin[element_key], dict):
#             yield from func(target,origin[element_key])
controller.delete_element(JSONElement(), "subdivision_name3", "json/text_structure.json")



# subs = controller.load("json/text_structure.json")
# a = next(func("sfefefe",subs))
# print(a)

