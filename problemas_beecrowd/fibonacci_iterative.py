fantes = f = 1
fantesantes = 1
n = int(input())
print(fantesantes, fantes, sep="\n")
for i in range (2, n+1):
   fantesantes, fantes = fantes, f
   f = fantesantes + fantes
   print(f)