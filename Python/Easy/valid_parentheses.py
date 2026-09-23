def isValid(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    for i in s:
        if i in "([{":
            stack.append(i)
        elif i == ")":
            if not stack or stack.pop() != "(":
                return False
        elif i == "]":
            if not stack or stack.pop() != "[":
                return False
        elif i == "}":
            if not stack or stack.pop() != "{":
                return False
    if stack:
        return False
    return True   

s= "(("
print(isValid(s))