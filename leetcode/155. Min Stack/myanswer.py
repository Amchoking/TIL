class MinStack:

    def __init__(self):
        self.mins=[]
        self.nums=[]
        self.min=None

    def push(self, val: int) -> None:
        self.nums.append(val)
        if(self.min!=None):
            self.min = min(self.min,val)
        else:
            self.min=val
        self.mins.append(self.min)

    def pop(self) -> None:
        self.nums.pop()
        self.mins.pop()
        if(self.mins):
            self.min=self.mins[-1]
        else:
            self.min=None

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min
