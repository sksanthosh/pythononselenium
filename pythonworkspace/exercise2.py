# Script to take marks from user and print percentage 
"""
Take name of the User Take Marks of Maths, Science and English from User Find percentage of given marks, Display,

User name is <NAME>, Scored <PERCENTAGE>  % in exams"""

name=input("Enter your name: ")
mathsmarks=int(input("Enter the Math marks: "))
sciencemarks=int(input("Enter the Science marks: "))
englishmarks=int(input("Enter the English marks: "))
total=mathsmarks+sciencemarks+englishmarks
percentage=(total/3)
print("User name is",name,",Scored",percentage,"% in exams")
