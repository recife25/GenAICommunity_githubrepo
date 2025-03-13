#what is a string - sequence of characters and enclosed quotes 
'''
text = 'hello world'    
print(text)

# string index - 0 based index, you can access individual characters in a string using index
text = "python is cool"
print(text[0]) # p
print (text[1]) # y 
print(text[2]) # t  
print(text[-1]) # l
print('####################') # h                  
for i in range(len(text)):
    print(text[i])
    
'''    


'''    
# string slicing - you can access a range of characters in a string using slicing
text = "python is cool"
print(text[0:6]) # python
print(text[1:4]) #yth
print(text[:3]) # pyt   
print(text[:6]) # python
print(text[:7]) # python
print(text[:10]) # python is
print(text[::-1]) # looc si nohtyp
'''


'''
text = "HELLO WORLD"    
print(text.lower())
print(text.upper()) 
print(text.capitalize())
print(text.strip('w' 'o' )) #HELLO WRLD
print(text.replace('WORLD','PYTHON')) #HELLO PYTHON
print(type(text.split(' '))) #['HELLO', 'WORLD']
print(text.join(' ')) #HELLO WORLD   
print(text.split(' ')) #['HELLO', 'WORLD']  
'''

'''
s = 'milk+bread+tea+water'
print(s.split('+')) #['milk', 'bread', 'tea', 'water']

l = ['felipe', 'python', 'computer', 'genai']
print('*'.join(l)) #felipe python computer genai

text = 'banana'
print(text.find('a'))
print(text.count('a'))  #3
print(text.count('b'))

name = 'felipe'
age = 61
# f-string method commit to memory most used form in coding 
print (f'my name is {name} and I am {age} years old')
# format method
print('my name is {} and I am {} years old'.format(name, age))
# % operator
print('my name is %s and I am %d years old' % (name, age))

'''


'''
#write a function that takes a list of words as input and returns the loongest word in a list
# create a list of words 
# use a for loop to find the longest word 
# return the longest word from the list 
# 
# #
      

list_of_words = ['python', 'java', 'elementes', 'cd', 'sets']
for word in list_of_words:
    if len(word) > len(list_of_words[0]):
        longest_word = word
        print(longest_word) # elements  
'''        
   
'''   
# write a function that takes a list of words as input and returns the loongest word in a list

def longest_word(words):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest      

list_of_words = ['python', 'java', 'elementes', 'cd', 'sets']   
print(longest_word(list_of_words)) # elements
'''
   
#write a program to reverse a string 

def reverse_string(s):
    return s[::-1]          
print(reverse_string('write a program to reverse a string')) #gnirts a esrever ot margorp a etirw   
   
#write a program that counts vowels and consonants in a string 

def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for char in s:
        if char in 'aeiou':
            vowels += 1
        elif char.isalpha():
            consonants += 1
    return vowels, consonants

print(count_vowels_consonants('write a program that counts vowels and consonants in a string')) #(15, 30)

       
        


