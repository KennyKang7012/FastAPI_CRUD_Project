from fastapi import FastAPI, HTTPException
from typing import List

from . import crud, models

app = FastAPI(
    title="FastAPI CRUD Project",
    description="A simple CRUD API with FastAPI.",
    version="1.0.0",
)

@app.post("/items/", response_model=models.Item)
def create_item(item: models.ItemCreate):
    return crud.create_item(item=item)

@app.get("/items/", response_model=List[models.Item])
def read_items():
    return crud.get_items()

@app.get("/items/{item_id}", response_model=models.Item)
def read_item(item_id: int):
    db_item = crud.get_item(item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=models.Item)
def update_item(item_id: int, item: models.ItemCreate):
    db_item = crud.update_item(item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", response_model=models.Item)
def delete_item(item_id: int):
    db_item = crud.delete_item(item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item