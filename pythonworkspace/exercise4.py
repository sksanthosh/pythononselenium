#!/usr/bin/python
# -*- coding: utf-8 -*-
# Take a number from user and check its divisble
"""
if divisible by 5 and 11 both, print divisible by both
if divisible only by 5, print divisible by 5 Only
if divisible by 11 only, print divisible by 11 Only
if not divisible by 5 and 11 both, print Not divisible
"""
n=int(input("Enter the number to check its divisible of 5 or 11 combinations: "))

if (n%5)==0 and (n%11)==0:
     print("Divisible by Both")
elif (n%5)==0 and (n%11)!=0:
     print("Divisible by 5 Only")
elif (n%5)!=0 and (n%11)==0:
     print("Divisible by 11 Only")
else:
     print("Not divisible by Both")
