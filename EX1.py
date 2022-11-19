class node:
    def __init__(self,num):
        self.num = num
        self.back = None
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,num):
        new = node(num)

        if self.head == None:
            self.head = new
        else:
            last = self.head
            while (1):
                if last.next == None:
                    break
                else:
                    last = last.next
            last.next = new
            new.back = last

main = linkedlist()
main.append(1)
main.append(2)
main.append(3)
main.append(4)