for _ in range(1, 11):
    N = int(input())
    S = input()
    stack = []
    result = -1

    for i in S:
        if i == "{" or i == "[" or i == "(" or i == "<":
            stack.append(i)
        elif i == "}":
            if len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            else:
                stack.append("}")
                break

        elif i == "]":
            if len(stack) != 0 and  stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]") 
                break   

        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")  
                break 

        elif i == ">":
            if len(stack) != 0 and stack[-1] == "<":
                stack.pop()
            else:
                stack.append(">")   
                break
    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print("#{} {}".format(_, result))