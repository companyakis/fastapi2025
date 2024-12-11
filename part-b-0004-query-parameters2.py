from fastapi import FastAPI

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


@app.get("/deps/{head}/")
async def get_head_department_by_query(head: str, name: str):
    result = []
    for dep in DEPARTMENTS:
        if dep.get("Head").casefold() == head.casefold() and \
                dep.get("Name").casefold() == name.casefold():
            result.append(dep)
    return result


# @app.get("/deps/")
# async def get_location_by_query(location: str):
#     l = []
#     for department in DEPARTMENTS:
#         if department.get('Location').casefold() == location.casefold():
#             l.append(department)
#     return l


# # static

@app.get("/deps/")
async def return_all_departments():
    return DEPARTMENTS

# # dynamic

# @app.get("/deps/{name}")
# async def return_dep_by_name(name: str):
#     for department in DEPARTMENTS:
#         if department.get("Name").casefold() == name.casefold():
#             return department
        
