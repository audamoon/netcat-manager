from controllers.controllers import JSONController

json_controller = JSONController("result.json")
all_texts = json_controller.load()
for i in range(len(all_texts)):
    text = all_texts[f"text-{i}"]
    h1_block = text["h1_block"]
    for h1 in h1_block:
        h1_tag = h1
        h1_text = h1_block[h1]
    print(f"ТЭГ {h1_tag}")
    print(f"БЛОК {h1_text}")
    h2_blocks = text["h2_blocks"]