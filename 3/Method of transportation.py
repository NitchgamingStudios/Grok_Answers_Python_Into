weather = input("Is it currently raining? ")
if weather == "Yes":
  print("You should take the bus.")
elif weather == "No":
  n = input("How far in km do you need to travel? ")
  d = int(n)
  if d < 2:
    print("You should walk.")
  elif 1 < d < 11:
    print("You should ride your bike.")
  elif d > 10:
    print("You should take the bus.")