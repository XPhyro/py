#!/usr/bin/env python3

import re
from os import path

bibFile = input("Enter the relative path of the bibliography file\n> ")
texFile = input("Enter the relative path of the TeX file\n> ")

if bibFile == "":
    bibFile = "bibliography.bib"
if texFile == "":
    texFile = "main.tex"

if not path.exists(bibFile): 
    print(f"{bibfile} does not exist.")
    exit()

if not path.exists(texFile): 
    print(f"{texFile} does not exist.")
    exit()

with open(bibFile) as bibf, open(texFile) as texf:
    bib = bibf.read()
    tex = texf.read()

p = re.compile(r"@.*{.*,")
oldTags = [re.sub(r"@.*{", "", i)[:-1] for i in p.findall(bib)]

newTags = []
for i in oldTags:
    newTags.append(input(f"{i}\n\t\t"))

for i in range(len(oldTags)):
    oldTag = oldTags[i]
    newTag = newTags[i]
    print(f"{oldTag} -> {newTag}")
    newBib = re.sub(fr"{{{oldTag},", fr"{{{newTag}", bib)
    newTex = re.sub(fr"cite{{{oldTag}}}", fr"cite{{{newTag}}}", tex)

print(newBib)
print(newTex)

with open(bibFile, "w+") as bibf, open(texFile, "w+") as texf:
    bibf.write(newBib)
    texf.write(newTex)
