#! /usr/bin/env python3

import spacy
import re

document = """A hipótese de Cristiano Ronaldo voltar ao futebol inglês pode não estar totalmente afastada, com o portal 'Football London' a associar o português ao Chelsea. Os rumores sobre a vontade de CR7 deixar o Al Nassr já no próximo verão têm subido de tom nas últimas semanas e, se em Espanha se especula sobre uma remota chance de voltar ao Real Madrid, em Inglaterra são os blues apontados como principais interessados."""

nlp = spacy.load('pt_core_news_md')

av = nlp(document) # Get document tree

# .sents -> get sentences (retorna a frase)
# .ents -> get entities (retorna um tuplo das entidades, se só houver 1 é um tuplo na mesma)

dic = {}

for s in av.sents:
    print(f'# {s}')
    for ent in s.ents:
        print(f'@ {ent}  | ent_type: {ent[0].ent_type_}') #temos de ver a pos 0 pq apesar de ser só 1, é um tuplo
    
    for w in s:
        # print(f'word: {w.text} | lema: {w.lemma_} | POS: {w.pos_} | tag: {w.tag_} | dep: {w.dep_}')
        if w.pos_ == 'VERB':
            if w.lemma_ not in dic:
                dic[w.lemma_] = 1
            else:
                dic[w.lemma_] += 1
    
for key in dic:
    print(f'verb: {key} | count: {dic[key]}')