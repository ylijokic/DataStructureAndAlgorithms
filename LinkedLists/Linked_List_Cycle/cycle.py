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


def hasCycle(head: Node) -> bool:
    dummy = Node(0)
    dummy.next = head
    slow = dummy.next
    fast = dummy.next

    while(fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next

        if(fast == slow):
            return True

    return False


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1

print(hasCycle(n1))