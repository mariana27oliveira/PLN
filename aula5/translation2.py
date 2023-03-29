import json
import re

file_in = open("dicionario_medico_aula_teste.json", encoding="utf-8")

dici = json.load(file_in)

file = open('termos_traduzidos.txt', encoding='utf8')
lines = file.readlines()
dicionario={}
for line in lines:
    desig = re.findall(r'^[^@ ]+', line) #retorna uma lista por palavra
    translation = re.findall(r'@\s(.+)$', line) #retorna uma lista por palavra
    desig_s = ''.join(desig) #transforma em strings
    translation_s = ''.join(translation) #transforma em strings
    dicionario[desig_s] = translation #constrói o dicionário

print(dicionario)

new_dici = {}
for designation, description in dici.items():
    new_dici[designation] = {
                            "des": description,
                            "en" : dicionario.get(designation, "Não encontrado")}
    
file_out = open ("dicionario_traduzido.json", "w", encoding="utf-8")
json.dump(new_dici, file_out, ensure_ascii=False, indent=4)
file_out.close()