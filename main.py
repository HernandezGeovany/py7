'''
1.1 Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!
'''
import random

i = [random.randint(1,10) 
   for i in range(5)]

print(sum(i))
