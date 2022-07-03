#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def areBracketsBalanced(expr):
    stack = []
 
    for char in expr:
        if char in ["(", "{", "["]:
 
            stack.append(char)
        else:
 
            if not stack:
                return False
                
            last_open_bracket = stack.pop()
            if last_open_bracket == '(':
                if char != ")":
                    return False
            if last_open_bracket == '{':
                if char != "}":
                    return False
            if last_open_bracket == '[':
                if char != "]":
                    return False
 
    if stack:
        return False
    return True
 
expr = "{()}[]"

if areBracketsBalanced(expr):
    print("Balanced")
else:
    print("Not Balanced")