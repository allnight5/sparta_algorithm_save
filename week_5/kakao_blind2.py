from collections import deque

balanced_parentheses_string = ")()))((()("
def is_correct_parenthesis(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)

        elif stack:
            stack.pop()

    return len(stack) == 0

def reverse_parenthsis(string):
    reverse_string = ""

    for char in string :
        if char == "(":
            reverse_string += ")"
        else :
            reverse_string += "("

    return reverse_string

def separate_u_v(string):
    queue= deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u+= char
        if char == "(":
            left += 1
        else :
            right +=1

        if right == left:
            break

    v = ''.join(list(queue))
    return u,v

def change_to_correct_parenthsis(string):
    if string == "":
        return ""
    u, v = separate_u_v(string)
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthsis(v)
    else :
        return "(" + change_to_correct_parenthsis(v) +")"+reverse_parenthsis(u[1:-1])



def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return is_correct_parenthesis
    else :
        return change_to_correct_parenthsis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!