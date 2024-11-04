birth_year: str = "1990"

user_input = input("Type current year info: ")

print(type(user_input)) # <class 'str'>

converted_birth_year = int(birth_year)

converted_user_input = int(user_input)

age = converted_user_input - converted_birth_year

print("User age: ", age) # User age:  34
      
      
