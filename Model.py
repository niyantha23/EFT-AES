class User:
    def __init__(self, name,dob,email,amount):
         self.name = name
         self.dob = dob
         self.email=email
         self.amount=amount
    
    def getData(self):
        return User(self.name,self.dob,self.email,self.amount)


#d=User("jj",23,"toki",900)
#y=d.getData()
#print(y.amount)

