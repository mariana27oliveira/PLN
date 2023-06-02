import json

with open('final_original.json', 'r', encoding="UTF-8") as f:
    final_original = json.load(f)

new_dict = {}

for key, value in final_original.items():
    if "categoria" in value:
        new_dict[key] = value
       

out2 = open ("final.json", "w", encoding="utf8")
json.dump(new_dict, out2, ensure_ascii=False, indent=4)