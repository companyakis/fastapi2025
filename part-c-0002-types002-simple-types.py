def age_calculator(name: str, current_year: int, birth_year: int) -> str:
    
    return f"{name.title()}, you are {current_year - birth_year} years old!"

result = age_calculator("aygün", 2025, 1997)

print(result) # Aygün, you are 28 years old!

# let's create some variables

pi: float = 22.0 / 7.0

print(pi) # 3.142857142857143

is_completed: bool

is_completed = False

