steps = int(input("How many steps? "))
print("__")
for step in range(steps - 1):
  print('  '*(step + 1) + "|_")
print("__"*steps + "|")