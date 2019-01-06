class SinglyLinkedList:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self,new_next):
        self.next = new_next

def removeDups(ll):
    alreadyPresent = {}
    currNode = ll
    nextNode = ll.next()

    while currNode.get_next:
        if currNode.val in alreadyPresent:
