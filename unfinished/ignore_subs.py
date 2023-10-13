import os
os.startfile("subdivision_to_delete.txt")
print("Добавьте в открывшийся файл подразделы, которые НЕ нужно заполнять")
#"(([\d]+[\.])( *[a-я]+ *)+)"giu - регулярка



from controllers.controllers import JSONController
controller = JSONController("json/text_structure.json")

def func(target,origin) -> None:
    for element_key in origin:
        if element_key == target:
            del origin[element_key]
            return
        if isinstance(origin[element_key], dict):
            func(target,origin[element_key])
subs = controller.load()
print(subs)
func("delete",subs)
print(subs)


