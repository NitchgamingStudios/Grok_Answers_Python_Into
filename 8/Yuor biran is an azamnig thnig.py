a,b = input('Enter words: ').split()
if sorted(a) == sorted(b) and a[0] == b[0] and a[-1] == b[-1]:
  print('Super Anagram!')
else:
  print('Huh?')