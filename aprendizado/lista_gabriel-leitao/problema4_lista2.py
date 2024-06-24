def invert(input : list):
   newlist = []
   for i in range(0, len(input)):
      last = input.pop()
      newlist.append(last)
   return newlist

class Solution:
   def listInvert(self):
      numbers = []
      while True:
        num = int(input())
        if num == 0:
            break
        numbers.append(num)
      print(numbers)
      print(invert(numbers))

solution = Solution()
solution.listInvert()
