from fastapi import FastAPI

app = FastAPI()

DEPARTMENTS = [
    {"Name": "Fintech", "Head": "Mustafa Büyükdereli", "Number of Employees": 17, "Location": "Turkiye"},
    {"Name": "Sales", "Head": "Aybilge Bilir", "Number of Employees": 3, "Location": "Canada"},
    {"Name": "Operations", "Head": "Hakan Görür", "Number of Employees": 5, "Location": "Turkiye"},
    {"Name": "Finance", "Head": "Kutluk Çalışır", "Number of Employees": 3, "Location": "Turkiye"},
    {"Name": "Audit", "Head": "Aygün Arslan", "Number of Employees": 2, "Location": "Turkiye"},
    {"Name": "Marketing", "Head": "Bengü Satıcı", "Number of Employees": 2, "Location": "Canada"},
    
]

@app.get("/deps/")
async def get_location_by_query(location: str):
    l = []
    for department in DEPARTMENTS:
        if department.get('Location').casefold() == location.casefold():
            l.append(department)
    return l
