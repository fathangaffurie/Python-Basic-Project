# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:12:24 2019

@author: acer
"""

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
#Initial Scores 
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98,97,85,88]
gradebook = zip(subjects,grades)

#Additional Scores
subjects.append('computer science')
grades.append(100)
subjects.append('visual arts')
grades.append(93)
gradebook = zip(subjects, grades)

#Add Gradebooks
full_gradebook = (last_semester_gradebook + (list(gradebook))) 
print(full_gradebook)