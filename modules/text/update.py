from common.controllers import JSONController

js = JSONController()


texts = js.load("json/result.json")

for text in texts:
    a = input(
        f"Введите sub_id для текста \"{list(texts[text]['h1_block'].keys())[0].replace('<h1>','').replace('</h1>','')}\", id = ")
    texts[text].update({
        "sub_id": a
    })

js.save("json/result.json", texts)
