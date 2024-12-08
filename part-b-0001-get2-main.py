from fastapi import FastAPI

app = FastAPI()

DEPARTMENTS = [
    {"Name": "Fintech", "Head": "Mustafa Büyükdereli", "Number of Employees": 7},
    {"Name": "Sales", "Head": "Aybilge Bilir", "Number of Employees": 3},
    {"Name": "Operations", "Head": "Hakan Görür", "Number of Employees": 5}
]

@app.get("/")
async def give_info():
    return DEPARTMENTS
