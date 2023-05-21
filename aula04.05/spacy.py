#! /usr/bin/env python3

import spacy
import re

document = """A hipótese de Cristiano Ronaldo voltar ao futebol inglês pode não estar totalmente afastada, com o portal 'Football London' a associar o português ao Chelsea. Os rumores sobre a vontade de CR7 deixar o Al Nassr já no próximo verão têm subido de tom nas últimas semanas e, se em Espanha se especula sobre uma remota chance de voltar ao Real Madrid, em Inglaterra são os blues apontados como principais interessados."""

nlp = spacy.load('pt_core_news_md') 
av = nlp(document) #get document tree

#.sents-> buscar frases
#.ents-> buscar entidades
#by default he gets the tokens
#cada um destes elementos (sentence, entity etc) tem varios atributos como a própia word(por defeito), o tipo de palavra(verbo etc), part of speech

contagem={}
for s in av.sents:
    print(f'#{s}')
    for ent in s.ents:
        print(f'@ {ent} ; Tipo: {ent.ent_type_}')
    for w in s:
        if w.pos_ == "VERB":
            if w.lemma_ in contagem.keys:
                contagem[w.lemma_]=contagem[w.lemma_]+1
            else:
                contagem[w.lemma_]=1
for key in contagem:
    print(f'Verbo: {key} ; Contagem: {contagem[key]}')