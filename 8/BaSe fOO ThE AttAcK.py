code = input("code: ")
code = code.split()
codes = []
for word in reversed(code):         
  if word[0].isupper():           
    codes.append(word.lower()) 
codes = " ".join(codes)
print("says:", codes)