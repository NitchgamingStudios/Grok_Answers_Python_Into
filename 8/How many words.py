words = []
word = input("Word: ")
while word != '':
  if word not in words:
    words.append(word)
    word = input("Word: ")
  else:
    word = input("Word: ")
print("You know", len(words), "unique word(s)!")