 ############ CMS: Customer Managements System #############

 #  BLL Start

class Customer:
    custlist=[]
    def __init__(self):
        self.id =0
        self.name=0
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
            elif (e.name ==self.name):
                self.id=e.id
                self.age=e.age
                self.mob=e.mob
            elif (e.mob ==self.mob):
                self.id=e.id
                self.name=e.name
                self.age=e.age
               

### Delete function
    def Delete():
        for e in Customer.custlist:
            if( e.id==id):
                Customer.custlist.remove(e)
                return
            elif( e.name==name):
                Customer.custlist.remove(e)
                return
            elif( e.mob==mob):
                Customer.custlist.remove(e)
                return

### Modify Function
    def Modify(self):
        for e in Customer.custlist:
            if  (e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
            elif  (e.name==self.name):
                e.id=self.id
                e.age=self.age
                e.mob=self.mob
            elif  (e.mob==self.mob):
                e.name= self.name
                e.age= self.age
                e.id= self.id

## Show Customer Function
    def showCustomer(obj):
       
        print("cust.id",obj.id,"cust.name",obj.name,"cust.age",obj.age,"cust.mob",obj.mob)
## BLL End

#   pL  Start
print("\n")
print("WELCOM TO DHEERAJ'S CMS USING PYTHON BANCKEND")
print("")
while True:
    try:
            choice=input(""" Press 1 for add /
    2 for serach / 3 for modify / 
    4 for delete / 5 for View All /
    6 for Exit /Enter your choice: """)

            #  Add  PL
            if choice=="1":
                obj=Customer()
                obj.id= int(input("Enter id: "))
                obj.name= input("Enter name: ")   
                obj.age= int(input("Enter age: "))
                obj.mob= int(input("Enter mob: "))
                obj.add()
                print("Customer Added successfully")

                ### SErach PL
            elif choice=="2":
                obj=Customer()
                chyn= input("Search On Basis of id/name/mob:   ")
                if chyn=="Id" or chyn=="id":
                    obj.id= int(input("Enter id: "))
                elif chyn=="Name" or chyn=="name":
                    obj.name = input("Enter Your name: ")
                elif chyn=="mob" or chyn=="Mob":
                    obj.mob= int(input("Enter Your Mobile: "))
                obj.Search()
                Customer.showCustomer(obj)

            ## Delete pL
            elif choice=="3":
                chyn= input("Search On Basis of id/name/mob:   ")
                if chyn=="Id" or chyn=="id":
                    obj.id= int(input("Enter id: "))
                elif chyn=="Name" or chyn=="name":
                    name = input("Enter Your name: ")
                elif chyn=="mob" or chyn=="Mob":
                    mob= int(input("Enter Your Mobile: "))
                Customer.Delete()
                print("Customer Delete Successfully")

                ##Modify PL
            elif choice=="4":
                obj=Customer()
                chyn= input("Search On Basis of id/name/mob:   ")
                if chyn=="Id" or chyn=="id":
                    obj.id= int(input("Enter id: "))
                    obj.name=input("Enter your Updated name: ")
                    obj.age=int(input("Enter your Updated age: "))
                    obj.mob=int(input("Enter your Updated mob: "))
                elif chyn=="Name" or chyn=="name":
                    obj.id= int(input("Enter id: "))
                    obj.name=input("Enter your Updated name: ")
                    obj.age=int(input("Enter your Updated age: "))
                    obj.mob=int(input("Enter your Updated mob: "))
                elif chyn=="Mob" or chyn=="mob":
                    obj.id= int(input("Enter id: "))
                    obj.name=input("Enter your Updated Name: ")
                    obj.age=int(input("Enter your Updated age: "))
                    obj.mob=int(input("Enter your Updated mob: "))
                    obj.Modify()
                    print("Customer Modify Successfully")
        # View All Customer List
            elif choice=="5":
                for  e in Customer.custlist:
                    Customer.showCustomer(e)

            else:
                print("incorrect Choice! please Enter given Squence")
            chyn= input("Do you want Contionue Y/N: ")
            if chyn=="N" or chyn=="n":
                print("Thank you Using My CMS ! Have a Nice Day")
                break
    except Exception as err:
        print("Error are !",err)

        # PL End

