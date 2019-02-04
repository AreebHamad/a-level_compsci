stack = ["" for i in range(0,10)]
topOfStackPointer = 0

def push(stack, topOfStackPointer):
    if len(stack) => topOfStackPointer:
       print("Stack is full")
    else:
        stack[topOfStackPointer+1] = input("data")
        topOfStackPointer += 1
    return stack, topOfStackPointer

def pop(stack, topOfStackPointer):
    if topOfStackPointer == 0:
        print("Stack is empty")
    else:
        stack[topOfStackPointer] = input("")
        topOfStackPointer -= 1
    return stack, topOfStackPointer

def main():
    while True:
        gui = int(input("[1] Create stack\n[2] Push\n[3] Pop\n-> "))
        if gui == 1:
        elif gui == 2:
        elif gui == 3:
        elif gui == 4:
            break
        else:
            print("Invalid input")
