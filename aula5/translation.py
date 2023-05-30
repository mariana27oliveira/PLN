from deep_translator import GoogleTranslator
#translated = GoogleTranslator(source='pt', target='en').translate("Hoje está um dia bonito")

translator=GoogleTranslator(source='pt', target='en')

import json

file_in = open ("dicionario_medico_aula_teste.json", encoding="utf-8")

dici=json.load(file_in)

new_dici = {}

for designation, description in dici.items():
    en_translation = translator.translate(designation)
    print(en_translation)
    new_dici[designation] = {"des":description, 
                             "en": en_translation
                             }
    
file_out=open("dicionario_translation.json", "w", encoding="utf8")
json.dump(new_dici, file_out, ensure_ascii=False, indent=4)
file_out.close()


#HOMEWORK: create a data structure em vez de usar o module do translator é para usar o ficheiro com as palavras traduzidas