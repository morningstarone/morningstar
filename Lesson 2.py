# try:
#     10/0
# except ZeroDivisionError:
#     print('cannot divide by 0')
    
# try:
#     result=10/int('string')
# except (ZeroDivisionError, ValueError) as e:
#     print(f'Error: {e}')

# def check_positive(no):
#     if no<=0:
#         raise ValueError("No not positive")
#     return no
# try:
#     check_positive(-10)
# except ValueError as e:
#     print(e)

# def leap_year(year):
#     if year%4!=0:
#         raise ValueError('Not leap year')
#     return year
# try:
#     a=int(input('enter year'))
#     leap_year(a)
# except ValueError as e:
#     print(e)

# class NegativeNoError(Exception):
#     def __init__(self,no,msg='no must be positive'):
#         self.no=no
#         self.msg=msg
#         super().__init__(self.msg)
# def divide(a,b):
#     try:
#         if a<0 or b<0:
#             raise NegativeNoError(a if a<0 else b)
#         result=a/b
#     except ZeroDivisionError:
#         print('Cannot divide by 0')
#     except NegativeNoError as ne:
#         print(f'error: {ne}')
#     except Exception as e:
#         print(f'unexpected error: {e}')
#     else:
#         print(f'result: {result}')
#     finally:
#         print('Execution done')
# divide(10,0)
# divide(-10,5)
# divide(10,2)



# def withdrawal(no,balance):
#     try: 
#         if no<0:
#             raise ValueError(no)
#         amt=balance-no
#         if amt<0:
#             raise ValueError(no)
    
#     except Exception as e1:
#         print(f'incorrect input: {e1}')
#     else:
#         print(f'result: {amt}')
    

# def deposit(no,balance):
#     try: 
#         if no<0:
#             raise ValueError('no less than 0')
#         amt=balance+no
#     except ValueError as e:
#         print(e)
#     except Exception as e1:
#         print(f'incorrect input: {e1}')
#     else:
#         print(f'balance: {amt}')
    
    

    
    
# a=int(input('enter choice: 1. withdrawal 2. deposit 3.check balance'))
# balance=10000
# total=0

# if a==1:
#     a1=int(input('Enter amt:'))
#     total=withdrawal(a1,balance)
# if a==2:
#     a2=int(input('Enter amt:'))
#     total=deposit(a2,balance)
d={'bat':4000,'ball':7000,'racket':8000, 'gloves':-10}

def add_item(arr,item,curr_total):
    arr.append(item)
    return arr

def remove_item(cart,item,curr_total):
    try:
        cart.remove(item)
        
    except ValueError:
        print('Not in cart')
    # else:
    #     curr_total-=cost
    
    return cart

def checkout(cart1):
    s=0
    for i in d:
        for j in cart1:
            if i==j:
                if d[i]<0:
                    raise ValueError('negative')
                s+=d[i]
    return s

type_of_items=[]

ch=0
while(True):
    a=int(input('1) bat 2)ball 3) gloves 4) racket 5) Press 0 to end'))
    b=input('A) Add, R) Remove, C) Checkout')
    if a==0:
        break
    
    if a==1:
        if b=='A':
            print(add_item(type_of_items,'bat',d['bat']))  
        elif b=='R':
            print(remove_item(type_of_items,'bat',d['bat']))
        elif b=='C':
            print(checkout(type_of_items))          
        else:
            raise ValueError('Wrong choice')
    elif a==2:
        if b=='A':
            print(add_item(type_of_items,'ball',d['ball']))  
        elif b=='R':
            print(remove_item(type_of_items,'ball',d['ball']))
        elif b=='C':
            print(checkout(type_of_items))   
        else:
            raise ValueError('Wrong choice')
    
    elif a==3:
        if b=='A':
            print(add_item(type_of_items,'gloves',d['gloves']))  
        elif b=='R':
            print(remove_item(type_of_items,'gloves',d['gloves']))
        elif b=='C':
            print(checkout(type_of_items))   
        else:
            raise ValueError('Wrong choice')
    elif a==4:            
        if b=='A':
            print(add_item(type_of_items,'racket',d['racket']))  
        elif b=='R':
            print(remove_item(type_of_items,'racket',d['racket']))
        elif b=='C':
            print(checkout(type_of_items))  
        else:
            raise ValueError('Wrong choice') 
   
        
        