### Code for thought #4
### In this assignment, we randomly generate scores for 50 students and
### then convert these grades to letter grades.
### In the end, we use dictionary to count the number of students for each letter
### grade, and display the results using different ways.

import random
import operator

def lettergrades(scores):
    grades = []
    for score in scores:
        if score >= 93:
            grades.append('A')
        elif score >= 90:
            grades.append('A-')
        elif score >= 87:
            grades.append('B+')
        elif score >= 83:
            grades.append('B')
        elif score >= 80:
            grades.append('C+')
        elif score >= 73:
            grades.append('C')
        elif score >= 70:
            grades.append('C-')
        elif score >= 67:
            grades.append('D+')
        elif score >= 63:
            grades.append('D')
        elif score >= 60:
            grades.append('D-')
        else:
            grades.append('F')
    return grades

### Note the return value of the previous function is a list


### Randomly generate scores for 50 students
random.seed(155)
scores = []
for i in range(50):
    scores.append(random.randrange(60, 100)+1)

### Note how randrange is used here
    
l_grades = lettergrades(scores)

d = {}
### d = {} is how to get an empty dictionary
### to get an empty set, one needs to use set()

for grade in l_grades:
    if grade not in d:
        ### fill in one line of code here
        d[grade] = 1

    else:
        ### fill in one line of code here
        d[grade] += 1 

print("Grade distribution in no particular order:")
for key in d.keys():
    print(key, "\t", d[key])

sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse = True)

print("Grade distribution sorted according to number of students:")
for item in sorted_d:
    print(item[0], "\t", item[1])


sorted_d = sorted(d.items(), key=operator.itemgetter(0), reverse = False)

print("Grade distribution sorted according to letter grades:")
for item in sorted_d:
    print(item[0], "\t", item[1])

