class Node:
    def __init__(s, new, next=None):
        s.val=new
        s.next=next
class LinkedList:
    def __init__(s, head=None):
        s.head = head
d=Node(1)
c=Node(3, d)
b = Node(-111312,c)
a = Node(3,b)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# best solution

def insertionSortList(head):
    dummy = ListNode(0)          # start of the sorted list
    cur = head
    while cur:
        nxt = cur.next           # save the rest of the old list
        prev = dummy
        while prev.next and prev.next.val < cur.val:
            prev = prev.next     # find where cur belongs
        cur.next = prev.next     # insert cur after prev
        prev.next = cur
        cur = nxt
    return dummy.next


linkedlist=LinkedList(a)
def sortLinkedList(head):
    i = head.head
    res = Node(None)
    while i:
        nxt = i.next 
        j = res
        while j.next and j.next.val<=i.val:
            j=j.next
        i.next = j.next
        j.next = i

        i = nxt
    link=LinkedList(res.next)
    t = link.head
    while t:
        print(t.val)
        t = t.next
    return link

sortLinkedList(linkedlist)
    