from itertools import permutations

def norm(s: str) -> str:
    # remove signs and lowercase
    return ''.join(ch.lower() for ch in s if ch not in "-;_")

# read initial strings
s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()

# normalize initial strings
n1 = norm(s1)
n2 = norm(s2)
n3 = norm(s3)

# create all 6 valid concatenations
valid = set(''.join(p) for p in permutations([n1, n2, n3], 3))

# read number of students
n = int(input())

for _ in range(n):
    ans = input().rstrip()
    nans = norm(ans)
    print("ACC" if nans in valid else "WA")
