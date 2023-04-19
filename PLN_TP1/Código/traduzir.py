from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='en', target='pt')

import json

file_in = open("dicio_en_es.json", encoding='UTF-8')
dici = json.load(file_in)

new_dici = {}

for designation, description in dici.items():
    en_translation = translator.translate(designation)
    print(en_translation)
    new_dici[en_translation]= description
    


with open("traduzido.json", "w", encoding='UTF-8') as fp:
    json.dump(new_dici, fp, ensure_ascii=False, indent=4)

