from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="sample-api")


class Item(BaseModel):
    id: int
    name: str
    price: float


class ItemCreate(BaseModel):
    name: str
    price: float


items: dict[int, Item] = {}
next_id: int = 1


def reset() -> None:
    global next_id
    items.clear()
    next_id = 1


@app.get("/items")
def list_items() -> list[Item]:
    return [items[item_id] for item_id in sorted(items)]


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items", status_code=201)
def create_item(payload: ItemCreate) -> Item:
    global next_id
    item = Item(id=next_id, name=payload.name, price=payload.price)
    items[item.id] = item
    next_id += 1
    return item
