class marks():
    def total(self,value):
        return value.sum(axis=1)
    def Average(self,value):
        count = value.count(axis=1)
        Total = self.total(value)
        average = Total/count
        return average

def Grade(average):
       if(average>=90):
           return "A"
       elif(average>=75):
        return "B" 
       elif(average>=60):
           return "C" 
       elif(average>=50):
           return "D" 
   

    
