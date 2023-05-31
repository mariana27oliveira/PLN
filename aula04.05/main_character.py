#! /usr/bin/env python3

import spacy
import re
from collections import Counter
import sys

file = sys.argv[1]

file = open(file, 'r', encoding='utf8')
book = file.read()

nlp = spacy.load('pt_core_news_md')
nlp.max_length = 1300000
av = nlp(book)

names = []
locations = []
for s in av.sents:
    for ent in s.ents:
        if ent[0].ent_type_ == 'PER':
            names.append(ent.text)
        if ent[0].ent_type_ == 'LOC':
            locations.append(ent.text)

personagens = Counter(names)
localizacoes = Counter(locations)
print(f'Main Character: {personagens.most_common(10)}')
print(f'Main Places: {localizacoes.most_common(10)}')