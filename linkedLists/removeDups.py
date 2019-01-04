class SinglyLinkedList:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
    def next(self):
        return self.next

def removeDups(ll):
    alreadyPresent = {}
    currNode = ll
    nextNode = ll.next()

    while currNode.next:
        if currNode.val in alreadyPresent:
