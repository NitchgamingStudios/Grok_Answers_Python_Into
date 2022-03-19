name = input("Enter your name: ")
if len(name) <= 3:
  print("Hi", name + ", you have a short name.")
elif 3 < len(name) < 9:
  print("Hi", name + ", nice to meet you.")
elif len(name) > 8:
  print("Hi", name + ", you have a long name.")