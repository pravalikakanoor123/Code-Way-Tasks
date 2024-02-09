import random 
letters =  ['Á','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!''@''#''$''%''&''?''+']
print("Welcome to the Password Generator!")
num_letters = eval(input("How many letters would do you like in your password:"))
num_numbers = eval(input("How many numbers would do you like in your password:"))
num_symbols = eval(input("How many symbols would do you like in your password:"))

password_list = []
for i in range(1,num_letters + 1):
    password_list.append(random.choice(letters))
for i in range(1,num_numbers+ 1):
    password_list.append(random.choice(numbers))
for i in range(1,num_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ""
for i in password_list:
    password += i
    print(i, i)

pwd = ''.join(password_list)
print(f"your Random Password is:{pwd}")
    
