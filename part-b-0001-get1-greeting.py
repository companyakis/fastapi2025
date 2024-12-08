from fastapi import FastAPI

app = FastAPI()

@app.get("/introduction")
async def first_fn():
    return {"message": "Let's learn FastAPI!"}
