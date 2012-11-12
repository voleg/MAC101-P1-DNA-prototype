# coding=utf-8
__author__ = 'voleg'
from Cell import Cell
DNACell1 = Cell()
DNACell2 = Cell()
h = Cell().hammingDistance(DNACell2)
distance = h
print("Hamming Distance = %s" % distance)

DNACell11 = DNACell1.mutate(4)
DNACell22 = DNACell2.mutate(4)



print("Hamming Distance = %s " % Cell().hammingDistance(DNACell11))