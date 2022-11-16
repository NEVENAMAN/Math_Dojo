class MathDojo:
    def __init__(self):
        self.result = 0
    # --------------------------------------
    def add(self,num1,*nums):
        self.result +=num1
        for value in nums:
            self.result += value
        return self
    # --------------------------------------
    def subtract(self,num1,*nums):
        self.result -=num1
        for value in nums:
            self.result -=value
        return self
        
operation = MathDojo()  
x = operation.add(1,3,4,5,10).subtract(1,2,5).result
print(x)