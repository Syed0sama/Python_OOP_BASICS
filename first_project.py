class person:
    number_of_employees =0
    number_of_managers =0
    total_persons = 0

    def __init__(self,name,age,id,salary):
        self.name= name
        self.age=age
        self.id=id
        self.salary=salary
        person.total_persons +=1
    
    def show(self):
        return self.name , self.age, self.id, self.salary
    
    def get_total_people(self):
        return self.total_persons 
    

class manager(person):

    def __init__(self,name,age,id,salary,role):
        super().__init__(name,age,id,salary)
        self.role = role
        person.number_of_managers +=1

    def show(self):
        return self.name , self.age, self.id, self.salary,self.role
    
    def get_number_of_managers (self):
        return self.number_of_managers

class employee(person):
    def __init__(self,name,age,id,salary,role):
        super().__init__(name,age,id,salary)
        self.role=role
        person.number_of_employees+=1
    
    def show(self):
        return self.name , self.age, self.id, self.salary,self.role
    
    def get_number_of_employees(self):
        return self.number_of_employees



p = person('osama',22,'e1456',499990)
p1 = person('sad',22,'e1456',499990)

print(p.show())
print(p1.show())
m=manager('nouman',33,'e123',4555,'Mnager')
m2=manager('nouman',33,'e123',4555,'Mnager')
print(m.show())
e=employee('hassan',45,'r543645',678768,'employee')
print(e.show())

print(p.get_total_people())
print(m.get_number_of_managers())
print(e.get_number_of_employees())

