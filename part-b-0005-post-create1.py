from fastapi import FastAPI, Body

app = FastAPI()

DEPARTMENTS = [
    {"Name": "Fintech", "Head": "Mustafa Büyükdereli", "Number of Employees": 17, "Location": "Turkiye"},
    {"Name": "Sales", "Head": "Aybilge Bilir", "Number of Employees": 3, "Location": "Canada"},
    {"Name": "Operations", "Head": "Hakan Görür", "Number of Employees": 5, "Location": "Turkiye"},
    {"Name": "Finance", "Head": "Kutluk Çalışır", "Number of Employees": 3, "Location": "Turkiye"},
    {"Name": "Audit", "Head": "Aygün Arslan", "Number of Employees": 2, "Location": "Turkiye"},
    {"Name": "Marketing", "Head": "Bengü Satıcı", "Number of Employees": 2, "Location": "Canada"},
    {"Name": "HR", "Head": "Mustafa Büyükdereli", "Number of Employees": 2, "Location": "Turkiye"},
]


@app.post("/deps/create-dep")
async def create_department(new_dep = Body()):
    DEPARTMENTS.append(new_dep)


@app.get("/deps/")
async def return_all_departments():
    return DEPARTMENTS
