n = int(input())

while n > 0:
   a = int(input())
   divisor = 0
   for i in range(1, a + 1, 1):
      if(a % i == 0):
         divisor = divisor + 1
   
   if(divisor <= 2):
      print(f"{a} eh primo")
   else:
      print(f"{a} nao eh primo")
   n = n - 1