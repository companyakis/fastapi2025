def create_person_salary_info(name: str, salary: int) -> dict[str, int]:
    
    return {name: salary}

person_ayhan = create_person_salary_info("Ayhan", 82_000)

person_mustafa = create_person_salary_info("Mustafa", 95_000)

print(person_ayhan) # {'Ayhan': 82000}

