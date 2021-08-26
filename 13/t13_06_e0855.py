def gen(n, count, stack, ans):
    if count == n // 2 and not stack:
        print(ans, file=file)
    if count < n // 2:
        gen(n, count + 1, stack + '(', ans + '(')
        gen(n, count + 1, stack + '[', ans + '[')
    if stack:
        if stack[-1] == '(':
            gen(n, count, stack[:-1], ans + ')')
        if stack[-1] == '[':
            gen(n, count, stack[:-1], ans + ']')


n = int(open('input.txt').read())
with open('output.txt', 'w') as file:
    gen(n, 0, '', '')