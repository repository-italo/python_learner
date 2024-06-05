def fibonacci(n: int):
   if n < 0:
      print("Incorret input")
   elif n == 0:
      return 0
   elif n == 1 or n == 2:
      return 1
   
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(0, end=" ")
for i in range(1, n, 1):
   print(fibonacci(i), end=" ")