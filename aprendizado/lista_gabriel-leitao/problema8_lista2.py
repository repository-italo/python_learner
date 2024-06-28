def input_list():
   numbers = []
   for i in range(3):
      line = float(input())
      numbers.append(line)
   return numbers

def situacaoFinal(nomeDoAluno, mediaAluno,situacaoAluno):
   print("O(A) aluno(a) %s esta com situacao %s devido a media final de" % (nomeDoAluno, situacaoAluno), round(mediaAluno, 1))


def situacaoDoAluno(nomeDoAluno, n1 : float, n2 : float, n3 : float):
	notas = [n1, n2, n3]
	mediaAluno = sum(notas) / len(notas)
	if( 6 <= mediaAluno <= 10): situacaoAluno = "Aprovado"
	elif (5 <= mediaAluno < 6): situacaoAluno = "Aprovado por recuperacao"
	elif (mediaAluno < 5): situacaoAluno = "Reprovado"
	situacaoFinal(nomeDoAluno, mediaAluno, situacaoAluno)



class Aluno:
   def __init__(self):
      self.nomeAluno = input()
      self.notas = input_list()


if __name__ == "__main__":
   aluno = Aluno()
   situacaoDoAluno(aluno.nomeAluno, aluno.notas[0], aluno.notas[1], aluno.notas[2])
   