# -*- coding: utf-8 -*-
"""HW 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12vG3yfifroY386YUPfPIvL5OOeLL85Up
"""

yeni_liste = [1,2,3,4,5,6,7,8]
yeni_1 = yeni_liste[4:8:1]
yeni_2 = yeni_liste[0:4:1]
print(yeni_1)
print(yeni_2)
yeni_1.extend(yeni_2)
print(yeni_1)

n = int(input("please enter a value of 'n' = "))

for i in range(0,n+2,2):
  if i > n:
    break
  else:
    print(i)