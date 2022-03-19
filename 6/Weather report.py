rainy = input('Which days had rain? ') 
rain = rainy.split()
print('Number of days without rain:', 7 - len(rain))