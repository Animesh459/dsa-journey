
n = input()

expression = [int(x.strip()) for x in n.split('+')]

sorted_number = sorted(expression)

result = '+'.join(str(x) for x in sorted_number)

print(result)