### Code for thought #10
### You are given a string of parentheses (“(“, “)”), braces(“{“, “}”)
### and brackets(“[“, “]”). You need to check whether each “(”, “{”, or “[”
### is paired with a matching “)”, “}”, or “[”.
###  For example, “( )(( )){([( )])}” and “()( )(( )){([( )])}” are matched
### correctly. While “)(( )){([( )])}”, “({[ 
### ])}” and “(“ are not matched
### correctly. Write code to test whether such a string is matched correctly.
### Complete the code for the 
#method def match(exp). 

class ListStack:
    def __init__(self):
        self._L = []
        
    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()

    def peek(self):
        return self._L[-1]

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0

#Am I allowed to do it my own way?  
def match(exp):
    #d = {'(':')', '{':'}', '[':']'}
    L = list(exp)
    stack = ListStack()
    for c in exp:
        if c == " ": continue
        if c == ")":
            if stack.isempty() or stack.pop() != "(": return False
            continue
        if c == "}":
            if stack.isempty() or stack.pop() != "{": return False
            continue
        if c == "]":
            if stack.isempty() or stack.pop() != "[": return False
            continue
        stack.push(c)
    return stack.isempty()


def match(exp):
    d = {'(':')', '{':'}', '[':']'}
    L = list(exp)
    stack = ListStack()
    for c in L:
        if c == ' ': continue
        if c in d:
            stack.push(c)
        else:
            if stack.isempty() or d[stack.pop()] != c:
                return False
    return stack.isempty()




exp = '( )(( )){([( )])}'
print(exp)
print(match(exp))

exp = '( )(( )){([( )])})'
print(exp)
print(match(exp))

exp = '( [)(( )){([( )])})'
print(exp)
print(match(exp))

exp = ''
print(exp)
print(match(exp))