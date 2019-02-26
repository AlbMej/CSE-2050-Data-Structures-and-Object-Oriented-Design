### Pascal triangle
### In this assignment, we use recursion and list comprehension to
### generate a line of Pascal triangle.
### For an input n, we generate the n-th line of the Pascal triangle.
### For your information, a Pascal triangle looks like the following.
###             1
###           1    1
###        1    2    1
###      1    3    3    1
###    1    4    6    4    1
### 1    5    10    10    5    1

def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n-1)
        print(p_line, n, len(p_line)-1)
        ### Add one line of code here
        line = [p_line[i] + p_line[i+1] for i in range(len(p_line)-1)]
        #print(line,"8")
        #print(p_line, n)
        line.insert(0,1)
        line.append(1)
    return line

print(pascal(5))


