class Queue: #FIFO = First in, First Our
    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def enqueue(self, x):
        if type(x) == list:
            self.queue.extend(x)
            self.len_queue += len(x)
        else:
            self.queue.append(x)
            self.len_queue+=1

    def dequeue(self): ## 1 pra sair da frente, 2 pra sair de trás
        if(self.len_queue>0):
            self.len_queue -=1
            return self.queue.pop(0)

    def front(self):
        print(self.queue[0])
    def show(self):
        if self.len_queue!=0:
            for i in self.queue:
                print(i,' ')
            print()


q = Queue()
q.enqueue('[')
q.enqueue('{')
q.enqueue('(')
q.enqueue('}')
q.enqueue(')')
q.front()