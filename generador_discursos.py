#!/bin/python3
import random
import itertools

palabras = ['blockchain', 'cuántico', 'inteligencia artificial', 'big data', 'revolución', 'futuro', 'descentralizado','centralizado', 'oportunidad']
discursos = list()

for permutation in itertools.permutations(list(set(palabras)),3):
    discursos.append(permutation)

random.shuffle(discursos)

for d in discursos: 
    for p in d: print(p, end =" "),
    print()