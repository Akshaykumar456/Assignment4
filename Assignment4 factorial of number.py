# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-oXDcBEEjcqW786IaaFyAztQeKrvuxnh
"""

#Factorial of number
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
fact(4)

