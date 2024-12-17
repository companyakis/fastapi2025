years: [int]= []

def add_to_years(year: int):
    
    years.append(year) 
    
    print(years)

add_to_years(2012)
add_to_years(2014)
add_to_years(2016)
add_to_years(2021)
add_to_years(2024)

# [2012]
# [2012, 2014]
# [2012, 2014, 2016]
# [2012, 2014, 2016, 2021]
# [2012, 2014, 2016, 2021, 2024]

# let's create some lists

names: list[str] = ["Mustafa", "Hakan", "Aygün"]

decisions: list[bool] = [True, False, False, True]

divisions: list[float] = [2.45, 3.14, 87.4567]


