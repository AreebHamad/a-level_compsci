class Node():
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer
        
lengthOfList = int(input("Length of list: "))
linkedList = [Node("", i+1) for i in range(0, lengthOfList)]
freePointer = 0
linkedList[lengthOfList].pointer = None

def addLinkedList(linkedList, freePointer):
    if freePointer == None:
        print("List is empty")
    else:
        linkedList[freePointer].data = input("Input data into linked list: ")
        freePointer = linkedList[freePointer].pointer
    return linkedList, freePointer
