def xor_sum(a: int, b: int):
      result = a ^ b
      return result


while True:
   try:
      a, b = map(int, input().split())
      print(xor_sum(a, b))
   except EOFError: 
      break