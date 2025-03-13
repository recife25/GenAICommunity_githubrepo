'''
# write a function to add and subtract a number 
def add(a,b):
    return a + b

def subtract(a,b):
    return a-b 
add(2,3)
subtract(3,4)

print (add (2,3))
print (subtract(3,4))
'''
'''
write a function that returns a factorial of a given number
def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input('enter the number to check if that is a factorial:'))
if factorial(num) == num:
    print(f'{num} is a factorial of another number')
else:
     print(f'{num} is not a factorial of another number')  
'''

'''
#write a function to check if a given string is a palindrome
def is_palindrome(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    return s == s[::-1]

#print(is_palindrome('madam'))
pal = str(input('enter a word to check for palindrome'))
if is_palindrome(pal):
    print(f'{pal} is a palindrome:   ') 
else:
    print(f'{pal} is not a palindrome:  ')
    
'''

'''
#write a function that takes a number and returns a square

def square(n):
    return n*n

#print(square(6))

num = int(input('enter number to square the number:'))
print(f'The square of {num} is: {square(num)}')
'''''

'''
#write a function that returns True if a number is prime and else False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
num = int(input('enter a number:'))
if is_prime(num):
    print(f'{num} is a prime number')
else:    
    print(f'{num} is not a prime number')
'''


'''
#write a function that raises a number to a power

def power(n,p):
    return n**p
    
num = int(input('enter a number:'))
pow = int(input('enter the power:'))
print(f'{num} raised to the power {pow} is: {power(num,pow)}')
'''

'''
#write a recursive function to comput the nth fibonacci number

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
num = int(input('enter a number:'))
print(f'the {num}th fibonacci number is: {fibonacci(num)}')
'''

'''
#def func(a, b=5, c=10):
    return a + b * c
    
print(func(2, c=4))   

'''

       

#intro to data structures

'''
#list
# ordered, mutable, allows duplicate elements
#list uses square brackets
number1 = [1,2,3,4,5,6,7,8,9,10]    
number2 = []

for i in range(1,11):
    number2.append(i)

number1.remove(10)
number1.remove(number1[-1])
number1.append('Python')
print(number1)
    
'''

#tuple
# ordered, immutable, allows duplicate elements
#tuple uses parenthesis

#my_tuple = (10,20, 'hello', 30, 40, 50) 

'''
data = ('Felipe', 61, 'New York')
for i in data:
    print(i)
'''


#dictionary
#unordered, mutable, indexed, no duplicate elements
#dictionary uses curly brackets

'''
animal = {
    'animal': 'chuffie', 
    'breed': 'turtle', 
    'age': 2, 
    
}

print(animal)
print(animal['animal'])
print(animal.get('breed'))
print(animal.keys())    
print(animal.values())
print(animal.items())
print(animal.pop('age'))


for i in animal:
    print(i ,':', animal[i])
    
for i in animal.items():
    print(i)
    print(i[0],':', i[1])
    print(i[0], ' is ', i[1])    
    
   ''' 

'''    
animals = [
    {'animal': 'chuffie', 'breed': 'turtle', 'age': 2},
    {'animal': 'jerry', 'breed': 'dog', 'age': 3},
    {'animal': 'felipe', 'breed': 'cat', 'age': 4}
    
]   
 

c = 1
for i in animals:
    print(f'Data of Animal {c}')
    for j in i:
        print(j, ':', i[j])                         
    c += 1
    print('---------------------------------')
    
    
    '''
    
'''    
person = {
    
    'name ': 'Felipe',
    'age': 61,
    'city': 'New York',
    
}    
    
person['country'] = 'USA'
person['age'] = 62
person['age'] += 1
person.update({'city': 'Great Neck', 'state': 'NY'})
#person.pop('city')
print(person)

'''

'''
When to use what 

List - when you need an ordered collection that be changed or updated or modified 

tuple - when you need a fixed ordered collection - eg coordinates

Sets - when yu need unique elements and set operations

dict - when you need fast key-value lookups



'''

'''
my_list = [1,2,3]
my_list.append([4, 5])
my_list.append(6,7)
print(my_list)
'''


my_tuple = (10,20,30)
print