#!/usr/bin/python
# -*- coding: utf-8 -*-
# Take 3 numbers from the user and display the largest and smallest among them

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

if n1 > n2 and n1 > n3:
    print ('Largest number is', n1)
    if n2 < n3:
        print ('Smallest number is', n2)
    else:
        print ('Smallest number is', n3)
elif n2 > n1 and n2 > n3:
    print ('Largest number is', n2)
    if n1 < n3:
        print ('Smallest number is', n1)
    else:
        print ('Smallest number is', n3)
else:
    print ('Largest number is', n3)
    if n1 < n2:
        print ('Smallest number is', n1)
    else:
        print ('Smallest number is', n2)
