 ############ CMS: Customer Managements System #############

 #BLL
class Customer:
    custlist=[]
    def __init__(self):
        self.id =0
        self.name=" "
        self.age=0
        self.mob=0

    #  ADD Function
    def add(self):
        Customer.custlist.append(self)
##      Search Function
    def Search(self):
       for e in Customer.custlist:
           if (e.id ==self.id):
               self.name=e.name
               self.age=e.age
               self.mob=e.mob
### Delete function
    def Delete():
        for e in Customer.custlist:
            if( e.id==id):
                Customer.custlist.remove(e)
                return

### Modify Function
    def Modify(self):
        for e in Customer.custlist:
            if  (e.id==self.id):
                e.name= self.name
                e.age= self.age
                e.mob= self.mob
   


#pLL

def showCustomer(obj):
        print(obj.id,obj.name,obj.age,obj.mob)
while True:
    choice=input(""" Press1 for add /
    2 for serach / 3 for modify / 
    4 for delete / 5 for View All /
    6 for Exit Enter your choice: """)
    #  Add  PL
    if choice=="1":
        obj=Customer()
        obj.id= input("Enter id: ")
        obj.name= input("Enter name: ")
        obj.age= input("Enter age: ")
        obj.mob= input("Enter mob: ")
        obj.add()
        print("Customer Added successfully")
        ### SErach PL
    elif choice=="2":
        obj=Customer()
        obj.id = input("Enter Your id: ")
        obj.Search()
        showCustomer(obj)
    ## Delete pL
    elif choice=="3":
        id = input("Enter Your id: ")
        Customer.Delete()
        ##Modify PL
    elif choice=="4":
        obj=Customer()
        obj.id=input("Enter your id: ")
        obj.name=input("Enter your Updated name: ")
        obj.age=input("Enter your Updated age: ")
        obj.mob=input("Enter your Updated mob: ")
        obj.Modify()

    elif choice=="5":
        for  e in Customer.custlist:
            showCustomer(e)

    else:
        print("incorrect Choice")
    chyn= input("Do you want Contionue Y/N: ")
    if chyn=="N" or chyn=="n":
        print("pass")
        break

        

