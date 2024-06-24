class Solution:
   def __init__(self):
      self.entrada = input()
      self.vogais = "aeiou"

   def count_vowels_and_consonants(self):
      print(len([char for char in self.entrada if char in self.vogais ]))
      print(len([char for char in self.entrada if char not in self.vogais]))

solution = Solution()
solution.count_vowels_and_consonants()