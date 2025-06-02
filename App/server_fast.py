from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola, mundo!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

