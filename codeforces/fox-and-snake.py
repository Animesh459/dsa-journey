n, m = map(int, input().split())

for i in range(n):
    if i % 2 == 0:
        # Odd-numbered row (1-based): full line of #
        print('#' * m)
    elif i % 4 == 1:
        # Even-numbered row after right-moving line: # is at the end
        print('.' * (m - 1) + '#')
    else:
        # Even-numbered row after left-moving line: # is at the start
        print('#' + '.' * (m - 1))



# Input
# 3 3
#
# Output
# ###
# ..#
# ###
#
# Input
# 3 4
#
# Output
# ####
# ...#
# ####
#
# Input
# 5 3
#
# Output
# ###
# ..#
# ###
# #..
# ###