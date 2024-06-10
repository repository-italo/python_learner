
n = int(input())
values : list
if n != 0: 
   values = list((map(int, input().split())))
   stack = []
   for i in values:
      stack.append(i)
   var = stack.pop()
   print(var)
"""    print(values, stack)
   for i in range(0, n, 1):
      if(stack.pop() = popped popped != values[(n - 1) - i]):
         isOk = False
      else:
         isOk = True

print(isOk) """