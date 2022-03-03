S = str(input())
 
stack = []
 
for i in range(len(S)):
    if len(stack) == 0:
        stack.append(S[i])
    elif stack[-1] != S[i]:
        stack.pop()
    else:
        stack.append(S[i])
ans = len(S) - len(stack)
print(ans)