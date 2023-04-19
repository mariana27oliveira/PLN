import json

with open('principal.json', 'r', encoding="UTF-8") as f:
    principal = json.load(f)


with open('dicio_pt_en.json', 'r', encoding="UTF-8") as f:
    dicio_pt_en = json.load(f)


for key in dicio_pt_en:
    if key not in principal:
        principal[key] = {'en': dicio_pt_en[key]}


with open('traduzido.json', 'r', encoding="UTF-8") as f:
    pt_es = json.load(f)

for key in pt_es:
    if key not in principal:
        principal[key] = {'es': pt_es[key]}


with open('definicoes1.json', 'r', encoding="UTF-8") as f:
    definicoes1 = json.load(f)

for key in definicoes1:
    if key not in principal:
        principal[key] = {'definição': definicoes1[key]}
    else:
        principal[key]['definição'] = definicoes1[key]


with open('definicoes2.json', 'r', encoding="UTF-8") as f:
    definicoes2 = json.load(f)

for key in definicoes2:
    if key not in principal:
        principal[key] = {'definição': definicoes2[key]}



with open('pop.json', 'r', encoding="UTF-8") as f:
    pop = json.load(f)

for key in pop:
    if key not in principal:
        principal[key] = {'expressão popular': pop[key]}
    else:
        principal[key]['expressão popular'] = pop[key]
    

out = open ("final.json", "w", encoding="utf-8")
json.dump(principal, out, ensure_ascii=False, indent=4)
out.close()
