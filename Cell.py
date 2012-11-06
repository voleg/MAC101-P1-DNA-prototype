# coding=utf-8
__author__ = 'voleg'
import random

class Cell(object):
    """
    Класс порождающий цепочки ДНК
    DNA макромолекула, состаящая из молекул (нуклеотидов)
    аденина (adenine), цитозин (cytosine), гуанин (guanine) и тимин (thymine),
    что соответствует list = ['A', 'C', 'G', 'T']
    """
    DNA = []
    list = ['A', 'C', 'G', 'T']
    def __init__(self):
        self.genDNA()

    def genDNA(self, length = 100):
        newDNA = self.DNA = []
        list = self.list
        iters = 0
        while iters <= length-1:
            iters += 1
            newDNA.append(list[self.rndMol()])
        return newDNA

    def rndMol(self):
        return random.randrange(start=0, stop=len(self.list))

    def hammingDistance(self, argDNA):
        hd, iters1 = 0, 0
        while iters1 <= len(self.DNA)-2:
            iters1 += 1
            if self.DNA[iters1] != argDNA.DNA[iters1]:
                hd += 1
        return hd

    def mutate(self, x):
        """
        Мутатор, принимает int Х в качестве процента мутирующих
        """
        num = round(len(self.DNA)*x/100)
#        newmols = self.genDNA(num)

        for i, v in enumerate(self.rndIndexes(x)):
            self.DNA[v] = self.rndMol()
#        return list(self.rndIndexes(x))
        return self

    def rndIndexes(self, x):
        places = set([])
        while len(places) <= x-1:
            places.add(random.randrange(start=0,stop=len(self.DNA)))
        return places