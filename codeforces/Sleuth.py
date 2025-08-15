question = input().strip()

# Remove trailing '?'
if question.endswith('?'):
    question = question[:-1]

# Strip spaces at the end and find the last letter
question = question.rstrip()
last_letter = ''
for ch in reversed(question):
    if ch.isalpha():
        last_letter = ch
        break

# Check if last letter is a vowel
vowels = set('AEIOUYaeiouy')
if last_letter in vowels:
    print("YES")
else:
    print("NO")
