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


# update-put

# let's update department head

@app.put("/deps/update-dep")
async def update_head(updated_dep = Body()):
    for i in range(len(DEPARTMENTS)):
        if DEPARTMENTS[i].get("Head").casefold() == updated_dep.get("Head").casefold():
            DEPARTMENTS[i] = updated_dep

@app.post("/deps/create-dep")
async def create_department(new_dep = Body()):
    DEPARTMENTS.append(new_dep)


@app.get("/deps/")
async def return_all_departments():
    return DEPARTMENTS
