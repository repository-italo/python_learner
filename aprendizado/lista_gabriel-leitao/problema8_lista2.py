def input_list():
   numbers = []
   for i in range(3):
      line = float(input())
      numbers.append(line)
   return numbers

def situacaoFinal(situacaoAluno, nomeDoAluno, mediaAluno):
   print("O(A) aluno(a) %s esta com situacao %s devido a media final de %.1f"
          % (nomeDoAluno, situacaoAluno, mediaAluno))


def situacaoDoAluno(nomeDoAluno : str, notas: list):
   mediaAluno = sum(notas) / len(notas)
   if(mediaAluno >= 6): situacaoAluno = "aprovado"
   elif (5 < mediaAluno < 6): situacaoAluno = "aprovado por recuperacao"
   else: situacaoAluno = "reprovado"
   situacaoFinal(situacaoAluno, nomeDoAluno, mediaAluno)



class Aluno:
   def __init__(self):
      self.nomeAluno = input()
      self.notas = input_list()


if __name__ == "__main__":
   aluno = Aluno()
   situacaoDoAluno(aluno.nomeAluno, aluno.notas)
   