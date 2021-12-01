class stack:
    def __init__(self):
        self.s = []
        self.min=None
    def push(self,x):
        if len(self.s)==0:
            self.s.insert(0,x)
            self.min=self.s
            print(self.s)
        elif len(self.s)!=0:
            for i in self.s:
                self.s.insert(0,x)
                print(self.s)
                if i<=x:
                    self.min=i
                else:
                    self.min=x
                break
    def pop(self):
        if len(self.s) != 0:
            self.s.pop(-1)
            if len(self.s)!=0:
                print(self.s)
            else:
                print("the stack is empty")
        elif self.s.pop(-1)==self.min and len(self.s)!=0:
            self.s.pop(-1)
        else:
            print("the stack is empty")
    def getMin(self):
            if len(self.s)!=0:
                print(self.min)
            elif len(self.s)==0:
                self.min=None
                print("the stack is empty")

x=stack()
x.push(89)
x.push(27)
x.push(67)
x.push(22)
x.pop()
x.pop()
x.getMin()
x.pop()
x.getMin()
x.pop()
