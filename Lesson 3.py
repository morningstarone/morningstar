# class Car():
#     pass
# a=Car()
# b=Car()

# a.modelname='city'
# a.yearm=2024
# a.price=1000

# b.modelname='sedan'
# b.yearm=2023
# b.price=10

# print(a.yearm)
# print(b.yearm)
# print(a.modelname)
# print(b.modelname)

# class Car():
#     def __init__(self,modelname,year,price):
#         self.modename=modelname
#         self.year=year
#         self.price=price
        
# h=Car('jhsabd',2021,123)
# g=Car('jased0bkd',2022,23)
# print(h.price)


# class Car1():
#     def __init__(self,modelname,year,price):
#         self.modename=modelname
#         self.year=year
#         self.price=price
        
# h=Car1('jhsabd',2021,123)
# g=Car1('jased0bkd',2022,23)
# h.cc=6548
# print(h.__dict__)
# print(g.__dict__)

# class Car1():
#     def __init__(self,modelname,year,price):
#         self.modename=modelname
#         self.year=year
#         self.price=price
    
#     def price_inc(self):
#         self.price=(self.price*1.5)
#         return self.price
        
# h=Car1('jhsabd',2021,123)
# g=Car1('jased0bkd',2022,23)
# h.cc=6548
# print(h.__dict__)
# print(g.__dict__)
# h.price_inc()
# print(h.price_inc())
# print(h.price)

# class Stock():
#     def __init__(self,sy,c_name,curr_pr,shares_av):
#         self.sy=sy
#         self.c_name=c_name
#         self.curr_pr=curr_pr
#         self.shares_av=shares_av
#     def addi(self,market_sec,div_yield):
#         self.market_sec=market_sec    
#         self.div_yield=div_yield
    
#     def total_p(self):
#         self.tot=self.curr_pr * self.shares_av
#         return self.tot

# h=Stock('jhsabd','tesla',123,4)
# h.addi('sdf0',9)

# print(h.total_p())
# print(h.__dict__)

# from datetime import datetime

# class Library():
#     def __init__(self,title,author,pub_yr,isbn):
#         self.title=title
#         self.author=author
#         self.pub_yr=pub_yr
#         self.isbn=isbn
    
#     def addi(self,genre,av):
#         self.genre=genre    
#         self.av=av
    
#     def age_of_book_year(self):
#         self.age=datetime.now().year-self.pub_yr.year
#         return self.age
#     def age_of_book(self):
#         self.ag=datetime.now()-self.pub_yr
#         return self.ag

# h=Library('black bull','stin',datetime(2023,6,27),876784)
# h.addi('comedy','Available')

# print(h.age_of_book())
# print(h.age_of_book_year())
# print(h.__dict__)

# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# x=Person('jon','doe')
# x.printname()

# class Student(Person):
#     pass

# x=Student('mike','olsen')
# x.printname()

# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
    
#     def printname(self):
#         print(self.fname,self.lname)

# class Student(Person):
#     def __init__(self, fname, lname,year):
#         super().__init__(fname, lname)
#         self.graduationyear=year
    
#     def welcome(self):
#         print('Welcome', self.fname,self.lname,'')

# import datetime

# class Employee:
#     def __init__(self,fname,lname,emp_id,dept,age,address,start_yr):
#         self.fname=fname
#         self.lname=lname
#         self.emp_id=emp_id
#         self.dept=dept
#         self.age=age
#         self.address=address
#         self.start_yr=start_yr
    
# class Manager(Employee):
#     def __init__(self, fname, lname, emp_id, dept, age, address,project_team,team_name,start_yr):
#         super().__init__(fname, lname, emp_id, dept, age, address,start_yr)
#         self.pt=project_team
#         self.tn=team_name
    
#     def employee_det(self):
#         print(self.fname,self.lname)
#         print(self.pt,self.tn)
#         print(datetime.datetime.now().year-self.start_yr)

# e=Employee('aa','bb',213,'datalake',29,'hdgfh',2020)
# m=Manager('aa','bb',213,'datalake',29,'hdgfh','t1','teams',2020)
# m.employee_det()

# class Animal:
#     def make_sound(self):
#         return "some sound"
 
# class Dog(Animal):
#     def make_sound(self):
#         return "bark"
   
 
# doggy = Dog()
 
# print(doggy.make_sound())


# class Base:
#     def __init__(self):
#         # protected member
#         self._a=2
        
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('Calling protected member of base class ',self._a)
        
#         self._a=3
#         print('Calling modified protected member outside class: ', self._a)

# obj1=Derived()
# obj2=Base()

# print(obj1._a)
# print(obj2._a)

# class Room:
#     def __init__(self,room_number, price_per_night):
#         self.room_number=room_number
#         self.price_per_night=price_per_night
#         self._availability=0
#         self.arr=[]
        
#     def get_av(self):
        
#         return self._availability 
    
#     def set_av(self):
#         self._availability=1
#         return self._availability
    
#     def rating(self,r):
#         self.r=r
#         self.arr.append(self.r)
#         return self.r
    
#     def avg_rat(self):
#         avg=sum(self.arr)/len(self.arr)
#         return avg 
    
#     def book(self):
#         if self._availability==0:
#             self._availability=1
#             return 'booked'
#         elif self._availability==1:
#             return 'Room already booked'
        
# class StandardRoom(Room):
#     def __init__(self, room_number, price_per_night):
#         super().__init__(room_number, price_per_night)
    
#         self.bed=1
#         self.tv=1

# class DeluxeRoom(Room):
#     def __init__(self, room_number, price_per_night):
#         super().__init__(room_number, price_per_night)
    
#         self.bar=1
#         self.pool=1
        

# class SuiteRoom(Room):
#     def __init__(self, room_number, price_per_night):
#         super().__init__(room_number, price_per_night)
    
#         self.personal_butler_service =1
#         self.park=1

    
# st=StandardRoom(4,200)
# st.rating(1)
# st.rating(2)
# print(st.avg_rat())
# print(st.get_av())
# print(st.set_av())
# print(st.book())
# print(st.__dict__)

# de=DeluxeRoom(5,400)
# de.rating(3)
# de.rating(5)
# print(de.avg_rat())
# print(de.get_av())
# # print(de.set_av())
# print(de.__dict__)
# print(de.book())
# print(de.__dict__)

# st1=SuiteRoom(6,500)
# st1.rating(4)
# st1.rating(7)
# print(st1.avg_rat())
# print(st1.get_av())
# print(st1.set_av())
# print(st1.book())
# print(st1.__dict__)

# import csv

# data=[['Name','Age','City'],['John','30','New York'],['Anna',28,'London'],['Mike','32','Chicago']]

# with open('data.csv','w',newline='') as csv_file:
#     writer=csv.writer(csv_file)
#     writer.writerows(data)
    
# with open('data.csv') as csv_file:
#     reader=csv.reader(csv_file)
#     for row in reader:
#         print(row)

import csv
#no of seasons, season has max no of matches, which team won by max runs, which team won by closest marging by runs, which team is most successful
seasons=set()
arr,arr1=[],[]
with open('matches.csv') as c:
    reader=csv.reader(c)
    for row in reader:
        if row[1]!='season':
            seasons.add(row[1])
            arr.append(row[1])
# print(seasons)
print(len(seasons))
print(arr)

d={}

for i in arr:
    if i in d:
        d[i]+=1
    elif i not in d:
        d[i]=1
print(d)
for i in d:
   if d[i]== max(d.values()):
       print(i)         

with open('matches.csv') as c:
    reader=csv.reader(c)
    for row in reader:
        if row[11]!='win_by_runs':
            arr1.append(int(row[11]))
print(max(arr1))

with open('matches.csv') as c:
    reader=csv.reader(c)
    for row in reader:
        if row[11]==str(max(arr1)):
            print(row[10])
arr2=[]
for i in arr1:
    if i!=0:
        arr2.append(i)
# print(arr2)
print(min(arr2))
s1=set()
with open('matches.csv') as c:
    reader=csv.reader(c)
    for row in reader:
        if row[11]==str(min(arr2)):
            s1.add(row[10])
print(s1)
arr3=[]
with open('matches.csv') as c:
    reader=csv.reader(c)
    
    for row in reader:
        for i in arr2:
            if row[11]!='win_by_runs':
                if int(row[11])==i:
                    arr3.append(row[10])
d1={}
for i in arr3:
    if i in d1:
        d1[i]+=1
    elif i not in d1:
        d1[i]=1
        
print(max(d1.values()))

for i in d1:
    if d1[i]==max(d1.values()):
        print(i)