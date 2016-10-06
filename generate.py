#!/usr/bin/env python3

import re

filter = re.compile(r'^[a-z]{4,8}$');

base = open('sources/3esl.txt')
exclude = open('sources/bad-words.txt')

exclusions = set(exclude.read().split('\n'))

out = open('words.txt', 'w')
count = 0
excluded = 0
for line in base:
    stripped = line.strip()
    if not stripped:
        continue
    if filter.match(stripped) is None:
        continue
    if stripped in exclusions:
        excluded += 1
        continue
    
    out.write(stripped + '\n')
    count += 1

print('Generated', count, 'words; excluded', excluded)