class Slk:  
   def inverter():
      codigo = int(input())
      i = 0
      saida = []
      while (i < codigo):
         saida.append(i)
         i = i + 1
      print(saida)
      
solucao = Slk()
solucao.inverter()