#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# #Password letters
# pass_letters = ""
# for letter in range(0, len(letters)):
#   letter = random.randint(0,len(letters))
#   count_letters = len(pass_letters)
#   if count_letters <= (nr_letters - 1):
#     pass_letters += letters[letter]

# #Password symbols
# pass_symbols = ""
# for symb in range(0, len(symbols)):
#   symb = random.randint(0, len(symbols))
#   count_symbols = len(pass_symbols)
#   if count_symbols <= (nr_symbols - 1):
#     pass_symbols += symbols[symb-1]

# #Password numbers
# pass_numbers = ""
# for num in range(0, len(numbers)):
#   num = random.randint(0, len(numbers))
#   count_numbers = len(pass_numbers)
#   if count_numbers <= (nr_numbers - 1):
#     pass_numbers += numbers[num-1]


# result = list(pass_letters + pass_symbols + pass_numbers)

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# random.shuffle(result)
# pass_result = ''.join(result)

# print(f"Your custom password is: {pass_result}")


#Angela Solution
# password = ""
# for ltr in range(0,nr_letters):#range(nr_letters)
#   password += random.choice(letters)

# for symb in range(0,nr_symbols):
#   password += random.choice(symbols)

# for num in range (nr_numbers):
#   password += random.choice(numbers)

# print (password)

#Randominize password
password = [] #make variable a list

for ltr in range(nr_letters):
  password.append(random.choice(letters))

for symb in range(nr_symbols):
  password += random.choice(symbols)

for num in range(nr_numbers):
  password += random.choice(numbers)

random.shuffle(password)
print (''.join(password))

