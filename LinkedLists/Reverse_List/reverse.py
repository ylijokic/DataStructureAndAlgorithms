class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(node: Node) -> None:
    curr = node
    while(curr != None):
        print(f'{curr.val} -> ', end="")
        curr = curr.next
    print("")


def reverseList(head: Node) -> Node:
    dummy = None
    curr = head

    while(curr):
        temp = curr.next
        curr.next = dummy
        dummy = curr
        curr = temp

    return dummy


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

printList(n4)
printList(n1)
reverseList(n1)
printList(n4)
