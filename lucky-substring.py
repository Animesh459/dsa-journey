s = input()
count4 = s.count('4')
count7 = s.count('7')

if count4 == 0 and count7 == 0:
  print(-1)
elif count4 >= count7:
  print(4)
else:
  print(7)