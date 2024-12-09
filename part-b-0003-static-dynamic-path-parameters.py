from fastapi import FastAPI

app = FastAPI()

DEPARTMENTS = [
    {"Name": "Fintech", "Head": "Mustafa Büyükdereli", "Number of Employees": 17},
    {"Name": "Sales", "Head": "Aybilge Bilir", "Number of Employees": 3},
    {"Name": "Operations", "Head": "Hakan Görür", "Number of Employees": 5},
    {"Name": "Finance", "Head": "Kutluk Çalışır", "Number of Employees": 3},
    {"Name": "Audit", "Head": "Aygün Arslan", "Number of Employees": 2},
    {"Name": "Marketing", "Head": "Bengü Satıcı", "Number of Employees": 2},  
]

# static

@app.get("/all-deps")
async def return_all_departments():
    return DEPARTMENTS

# dynamic

@app.get("/all-deps/{name}")
async def return_dep_by_name(name: str):
    for department in DEPARTMENTS:
        if department.get("Name").casefold() == name.casefold():
            return department
