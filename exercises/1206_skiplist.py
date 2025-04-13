
import random


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.parent=None

class Skiplist:

    def __init__(self):
        self.max_level = 3
        self.levels = []
    def print(self):
        for i,head in enumerate(self.levels):
            node = head
            res = []
            while node:
                res.append(str(node.val))
                node=node.next
            print(f"{i}: {' '.join(res)}")
    
    def search(self, target: int) -> bool:
        node = None
        for n in self.levels:
            if n:
                node = n
                break
        while node:
            if node.val==target:
                return True
            else:
                if not node.next or (node.next.val > target and node.val < target):
                    node=node.parent
                else:
                    node=node.next
        return False
    def add(self, num: int) -> None:
        prev=None
        for i in range(len(self.levels)-1,-1,-1):
            h,n = self.addInternal(self.levels[i],num)
            self.levels[i] = h
            if prev:
                n.parent = prev
            prev = n
            if random.randint(0, 1)==1:
                break
        print(f'add {num}')
        self.print()
        

    def addInternal(self,head, num: int) -> None:
        if not head:
            head = Node(num)
            return head,head
        elif num <= head.val:
            n = Node(num)
            n.next = head
            head = n
            return head,n
        node = head
        while node.next and node.next.val < num:
            node=node.next
        n = Node(num)
        n.next = node.next
        node.next = n
        return head,n

    def erase(self, num: int) -> bool:
        res = 0
        for i in range(len(self.levels)):
            r,head=self.eraseInternal(self.levels[i],num)
            if r:
                res+=1
            self.levels[i] = head
        print(f'erase {num}')
        self.print()
        return res>0

    def eraseInternal(self,head, num: int) -> bool:
        if not head:
            return False,head
        if head.val == num:
            head = head.next
            return True,head
        node = head
        while node.next:
            if node.next.val==num:
                node.next = node.next.next
                return True,head
            node=node.next
        return False,head