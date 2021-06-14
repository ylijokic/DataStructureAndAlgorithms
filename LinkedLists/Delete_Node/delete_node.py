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


def deleteNode(node: Node) -> None:
    node.val = node.next.val
    node.next = node.next.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

printList(n1)
deleteNode(n3)
printList(n1)
