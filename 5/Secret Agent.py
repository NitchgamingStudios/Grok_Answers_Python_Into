code = input ('Message? ') [0::3]
msg = ""
for i in code: 
  msg += " " + i
print(msg [1:])