from fastapi import FastAPI, Body

app = FastAPI()

DEPARTMENTS = [
    {"Name": "Fintech", "Head": "Mustafa Büyükdereli", "Number of Employees": "17", "Location": "Turkiye"},
    {"Name": "Sales", "Head": "Aybilge Bilir", "Number of Employees": "3", "Location": "Canada"},
    {"Name": "Operations", "Head": "Hakan Görür", "Number of Employees": "5", "Location": "Turkiye"},
    {"Name": "Finance", "Head": "Kutluk Çalışır", "Number of Employees": "3", "Location": "Turkiye"},
    {"Name": "Audit", "Head": "Aygün Arslan", "Number of Employees": "2", "Location": "Turkiye"},
    {"Name": "Marketing", "Head": "Bengü Satıcı", "Number of Employees": "2", "Location": "Canada"},
    {"Name": "HR", "Head": "Yiğit Ünlü", "Number of Employees": "2", "Location": "Turkiye"},
]

@app.get("/deps")
async def return_all_departments():
    return DEPARTMENTS
           
@app.delete("/deps/delete_dep/{dep_name}")
async def delete_dep(dep_name: str):
    for i in range(len(DEPARTMENTS)):
        if DEPARTMENTS[i].get("Name").casefold() == dep_name.casefold():
            DEPARTMENTS.pop(i)
            break
