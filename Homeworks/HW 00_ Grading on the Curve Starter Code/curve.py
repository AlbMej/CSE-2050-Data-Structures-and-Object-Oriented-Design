import sys
from grader import average, droplowest, assigngrade

# Read in a collection of scores.
# Each line should be the grades for one student.
rawscores = []
for line in sys.stdin:
    # Split the line of numbers into a list of strings.
    scores_as_strings = line.split()
    # Convert the scores to floats.
    scores = [float(x) for x in scores_as_strings]
    rawscores.append(scores)

def variance(L):
    avg = average(L)
    return average([(x - avg) ** 2 for x in L])

def stddev(L):
    return variance(L) ** 0.5

if __name__ == '__main__':
    # Put your code here.
    student_avgs  = []
    for i in rawscores:
        droplowest(i)
        droplowest(i)
        student_avgs.append(average(i))
    sdev = stddev(student_avgs)
    avg = average(student_avgs)
    for i in student_avgs:
        A = avg + sdev
        B = avg
        C = avg - sdev
        D = avg - 2*sdev
        if i >= A: print('A')
        if i < A and i >= B: print('B')
        if i < B and i >= C: print('C')
        if i < C and i >= D: print('D')
        if i < D: print('F')