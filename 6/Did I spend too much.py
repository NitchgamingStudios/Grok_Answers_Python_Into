l = []
s = (input('Enter the expenses: '))
l = s.split()
new_list = []
for i in l:
  new_list.append(int(i))
s = sum(new_list)
t = str(s)
print("Total: $" + t)