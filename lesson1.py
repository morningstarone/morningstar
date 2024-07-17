d={'bat':4000,'ball':7000,'racket':8000, 'gloves':10}
arr=[]
amt=0
a=int(input('enter no of items:'))
for i in range(a):
    a1=input('enter product')
    arr.append(a1)
for i in arr:
    for j in d:
        if i==j:
            amt+=d[j]
print(amt)
if amt>=10000:
    amt=amt-(amt*0.05)
    print(amt)
elif amt>=3000 and amt<10000:
    amt=amt-(amt*0.1)
    print(amt)

d={'bat':4000,'ball':7000,'racket':8000, 'gloves':10}
arr=[]
amt=0
a=int(input('enter no of items:'))
for i in range(a):
    a1=input('enter product')
    arr.append(a1)
for i in arr:
    for j in d:
        if i==j:
            amt=amt+d[j]
print(amt)
if amt>=10000:
    amt=amt-(amt*0.05)
    print(amt)
elif amt>=3000 and amt<10000:
    amt=amt-(amt*0.1)
    print(amt)

l=['physics','chem','biology']

s1=l[1]+l[0][:3]+l[2][:3]
print(s1)

import random
greet=['hi','hola','hello']
age=['7','17','27']
g1=['how are u?','are u good?']
g2=['great','nice']
a=random.choice(greet)
s=1
a1=1
while(s!=0):
    s=input('say something')
    if s.lower() in greet:
        print(a)
    elif s in age:
        if int(s)>=13 and int(s)<=19:
            print('teen')
        elif int(s)<13:
            print('child')
        else:
            print('adult')
    elif s.lower() in  g1:
        print(random.choice(g1))
    elif s.lower=='0':
        break

d={'a':1,'b':2,'c':3}
d1={}
for i in d:
    d1[d[i]]=i
print(d1)

d2={k:v for v,k in d.items()}
print(d2)

st={'Alice':{'age':25,'grade':'A'},'bob':{'age':22,'grade':'B'}}
for i in st:
    if i=='Alice':
        print(st[i]['grade']) 

c=0
a=int(input('enter no'))
if a%2==0:
    print('even')
if a%2!=0:
    print('odd')
if (a>2 and a%2==0) or a==1:
          print('not prime')
elif a>2:
    for i in range(2,a):
        if a%i==0:
            print('not prime')
            c+=1
            break
    if c==0:
        print('prime')
elif a==2:
    print('prime')

import random

play = 'yes'
i=1
while play.lower()== "yes":
    questions_dictionary = [
        {"question": "What is the capital of India?", "answer": "New Delhi"},
        {"question": "What is the largest continent?", "answer": "Asia"},
        {"question": "How many planets in solar system?", "answer": "8"},
        {"question": "What is the most famous bridge?", "answer": "Golden gate bridge"}
    ]

    attempts = 2

    print("Welcome to the Simple Quiz Game!\n")

    for question in questions_dictionary:
        print(question["question"])
       
        for attempt in range(attempts):
            answer = input("Enter your answer: ")

            if answer.lower() == question["answer"].lower():
                print("Correct!\n")
                break
            else:
                print("Incorrect! Try again.\n")

        else:
            print(f"Sorry, you've run out of attempts. The correct answer is: {question['answer']}\n")
            
    play=input('Do you want to play again? Type(yes or no)')
    
print('Thnaks for playing game')

def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
a=list(map(int,input().split()))
inp=int(input('enter operation: 1. add 2. multiply 3. subtract 4. divide'))
if inp==1:
    print(add(a[0],a[1]))
elif inp==2:
    print(multiply(a[0],a[1]))
elif inp==3:
    print(subtract(a[0],a[1]))
elif inp==4:
    print(divide(a[0],a[1]))    

