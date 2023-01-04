class PDM:
    def __init__(self, range =1):
        self.error = 0
        assert(range>0)
        self.range = range

    def Tick(self, x):
        self.error += x

        if self.error > 0:
            y =1
        else:
            y =-1

        self.error += -y
        return(y)

    def Normalize(self,x):
        return(x/self.range)

    def Reset(self):
        self.error = 0

