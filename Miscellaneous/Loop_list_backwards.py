myl = [5, '*', 40, '-', '(', 72, '/', '(', 40, '-', 22, ')', '+', 60, ')']

i_bracket_open = 0
j_bracket_end = 0
for element in myl:
    if element == '(':
        i_bracket_open += 1
    elif element == ')':
        j_bracket_end += 1
    else:
        continue

print(i_bracket_open)
print(j_bracket_end)

if i_bracket_open == j_bracket_end:
    print(f"There are {i_bracket_open} bracket terms. Everything OK.")


