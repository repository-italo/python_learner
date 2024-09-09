class ListNode(object):
   def __init__(self, val, next=None):
      self.val = val
      self.next = next
   
def createLinkedList(arr):
   if not arr:
      return None
   
   head = ListNode(arr[0])
   current = head

   for x in arr[1:]:
      current.next = ListNode(x)
      current = current.next
   return head

def addTwoNumbers(l1: ListNode, l2: ListNode):
   num1, num2 = [], []
   s1, s2 = "", ""
   #percorrendo lista1
   current = l1
   while current:
      num1.append(current.val)
      current = current.next

   #percorrendo lista2
   current2 = l2
   while current2:
      num2.append(current2.val)
      current2 = current2.next

   for i in reversed(num1):
      s1 = s1 + str(i)
   
   for i in reversed(num2):
      s2 = s2 + str(i)
   resposta = str(int(s1) + int(s2))
   listaResposta = [int(a) for a in resposta]
   return listaResposta[::-1]


if __name__ == "__main__":
   arr = [0]
   arr2 = [0]
   l1 = createLinkedList(arr)
   l2 = createLinkedList(arr2)
   print(addTwoNumbers(l1, l2))


      