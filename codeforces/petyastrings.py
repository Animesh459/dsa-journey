
string1 = input()
string2 = input()

normalized_string1 = string1.lower()
normalized_string2 = string2.lower()

if normalized_string1 < normalized_string2:
    print("-1")

elif normalized_string2 < normalized_string1:
    print("1")

else:
    print("0")

