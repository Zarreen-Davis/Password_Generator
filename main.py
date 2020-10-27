#enter and reenter password to ensure they match
password= input ("Please create a password: ")
password_2 = input ("Please re-enter you password: ")

#if passwords don't match an invalid message is displayed
if password != password_2: 
  print("Invalid! These passwords don't match.")

#checks password length is valid. Must be more than 6 characters but less than 20 characters
if len(password_2) <6:
    print("Invalid! Password must be more than 6 characters.")
elif len(password_2) >20:
    print("Invalid! Password must be less than 20 characters.")

#weak password contains just lower and/or uppercase characters
#medium strength password contains lowercase, uppercase and numbers
#strong password contains uppercase and lowercase characters, number and symbols

lowercase_found = 0
uppercase_found = 0
digit_found = 0
SpecialSym_found = 0

for char in password_2:
  if char.islower():
    lowercase_found = 1
  if char.isupper():
    uppercase_found = 1
  if char.isdigit():
    digit_found = 1
  if char=='$'or char=='#' or char=='%' or char=="!":
    SpecialSym_found = 1

  if lowercase_found and uppercase_found and digit_found and SpecialSym_found:
    break

password_strength = lowercase_found + uppercase_found + digit_found + SpecialSym_found

if password_strength == 1:
  print("You have entered a weak password!")
elif password_strength ==2:
  print("You have entered a weak password!")
elif password_strength ==3:
  print("You have entered a medium strength password.")

else:
  print("You have entered a strong password.")