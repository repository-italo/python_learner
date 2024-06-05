n = int(input())

n1 = 0
n2 = 1
next = n2
print(n1, n2, end="")
while n > 3:
   print('', next, end="")
   n = n - 1
   n1, n2 = n2, next
   next = n1 + n2
print("\n", end="")
