from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []


@app.get("/")
def home():
    return {"message" : "Hello from FastAPI!"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code = 404, detail=f"item {item_id} not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if 0 <= item_id < len(items):
        items[item_id] = item
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        deleted_item = items.pop(item_id)
        return {"message": "Item deleted", "item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")
    

