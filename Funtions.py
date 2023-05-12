'''

def say_my_name():
    print ('Tasdeeque')
    print('John')
    print('Kara')
    print('Sam')        
#say_my_name()

def say_my_name_2(name):
    print(name)
    
#say_my_name_2('Tasdeeque')

def greeting(name, greet):
    
    ***Documentation is important***
    If we give a value to a variable  the in the def it is taken as default
    
    greeting takes 2 arguments, greet and name
    and it greets the user
    
    code >>> greeting('Aloha!', 'Tasdeeque')
    output >>> Aloha! Tasdeeque
    
    
    print(f'👋😎👋 {greet} {name}')
greeting( 'Tasdeeque', 'Aloha')  



def sum(a,b):
    result = a+b
    return(result)

def sub(a,b):
    result = a-b
    return(result)

def mul(a,b):
    result = a*b
    return(result)

def div(a,b):
    result = a/b
    return(result)
sumResult = sum(6,10)
print(sumResult)
print(mul(4,2))
print(mul(6,2))
print(mul(5,2))
'''

def sum (a,b):
    result = a + b
    return (result)

def sub (a,b):
    result = a - b
    return (result)

def mul(a,b):
    result = a * b
    return (result)
    
def div(a,b):
    result = a / b
    return (result)
    
a = int(input('Enter the First Number: '))
b = int(input('Enter the Second Number: '))

print ('The Addition of the Two Numbers', sum(a,b))
print ('The Substraction of the Two Numbers', sub(a,b))
print ('The Multiplication of the Two Numbers', mul(a,b))
print ('The Division of the Two Numbers', div(a,b))    