from fastapi import fastapi

app = fastapi()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todos")
async def get_todos():

    return[
        {"id": 1, "detail": "first todos"},
        {"id": 2, "detail": "seconds todos"}
    ]

couter = 0 
@app.get("/couter")
async def get_couter():
    global couter
    couter += 1
    return {"message" : f"couter = {couter}"}
