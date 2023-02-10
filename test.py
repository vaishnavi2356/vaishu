class car:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        

    def myfunc(self):
        print(f"car name is {self.name}and colour is {self.colour}")


    def __str__(self):
        return  "Name: "+self.name +",colour:"+str(self.colour)
    

p1 = car("shift",black)
p1.myfunc()
print(p1)






























    
   

  
    

    

    

    


    

    















