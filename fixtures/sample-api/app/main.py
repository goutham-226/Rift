from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="sample-api")


# structured output - JSON validation
class Item(BaseModel):
    id: int
    name: str
    price: float

# Json validation
class ItemCreate(BaseModel):
    name: str
    price: float

# data structure instead of using databse model
items: dict[int, Item] = {} # list of Item BaseModel object
next_id: int = 1 # primary key tracker


def reset() -> None:
    global next_id
    items.clear()
    next_id = 1

# get endpoint lists all the items.
@app.get("/items")
def list_items() -> list[Item]:
    return [items[item_id] for item_id in sorted(items)]

# get endpoint lists item with given id
@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items", status_code=201)
def create_item(payload: ItemCreate) -> Item:
    global next_id
    item = Item(id=next_id, name=payload.name, price=payload.price) # Item is a BaseModel
    items[item.id] = item
    next_id += 1
    return item
