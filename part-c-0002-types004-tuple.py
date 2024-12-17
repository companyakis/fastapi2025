def create_person_info(name: str, id: str, salary: int) -> tuple[str, str, int]:
    
    return (name, id, salary)

person_ayhan = create_person_info("Ayhan Bilir", "4296", 75_000)

print(type(person_ayhan))

print(person_ayhan)

print(person_ayhan[0])
print(person_ayhan[1])
print(person_ayhan[2])

# <class 'tuple'>
# ('Ayhan Bilir', '4296', 75000)
# Ayhan Bilir
# 4296
# 75000
