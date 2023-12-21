class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
    num1 = 0
    num2 = 0
    con1 = 1

    while l1:
        num1 = num1 + (l1.val * con1)
        con1 = con1 * 10
        l1 = l1.next

    con1 = 1

    while l2:
        num2 = num2 + (l2.val * con1)
        con1 = con1 * 10
        l2 = l2.next

    suma = num1 + num2

    # Convertir el resultado en una lista enlazada con los dígitos en orden inverso
    prev = None
    for digit in str(suma):
        node = ListNode(int(digit), prev)
        prev = node

    # 'prev' ahora es la cabeza de la lista enlazada resultante
    return prev

# Ejemplo de uso:
l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(1, ListNode(2, ListNode(7)))

result = addTwoNumbers(l1, l2)

print(result)