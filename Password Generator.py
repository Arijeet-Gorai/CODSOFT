import random


alphaNumeric_data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',]
symbol_data = ['@','#','$','*','+','&']

def divide (n_length): # It is a function for divide the passwoord length for selection the minimal number of symbols in the program
    a=int(n_length//4)
    b=0
    for i in range (a+1,n_length+1):
        i+=1
        b+=1
    return a,b


password_list=[] # this is empty list for contain all character geting from 2 loops
password="" # this is empty string for contain the shuffeled final password

print("Welcome to Password Generator!")
n_length=int(input("Enter the LENGTH of password: "))

a,b=divide(n_length)


for i in range (1,b+1):
    password_list.append(random.choice(alphaNumeric_data)) # in this loop it store ALPHANUMERIC character

for i in range (1,a+1):
    password_list.append(random.choice(symbol_data)) # in this loop it store minimal number of SYMBOLS character

random.shuffle(password_list)

for char in password_list:
    password += char # in this loop it store the shuffeled password_list's in password variable

print("Your Unique Password : ",password)
print("Thank you Visit Again.")