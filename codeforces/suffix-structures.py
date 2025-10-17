from collections import Counter

s = input().strip()
t = input().strip()

# Case 1: Check if t is a subsequence of s → only need automaton
i = j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        j += 1
    i += 1
if j == len(t):
    print("automaton")
    exit()

# Count characters
cs = Counter(s)
ct = Counter(t)

# Case 2: If t needs more of any character than s has → impossible
for ch in ct:
    if ct[ch] > cs.get(ch, 0):
        print("need tree")
        exit()

# Case 3: If lengths are equal and counts match → only swapping needed
if len(s) == len(t) and cs == ct:
    print("array")
else:
    # Case 4: t can be formed from s but not as a subsequence → need both
    print("both")
