from typing import List, Dict, Optional
from . import models

# Use a simple in-memory dictionary as a database
fake_db: Dict[int, models.Item] = {
    1: models.Item(id=1, name="Foo", price=42.0, description="A lovely item"),
    2: models.Item(id=2, name="Bar", price=69.9, description="Another lovely item"),
}

def get_item(item_id: int) -> Optional[models.Item]:
    return fake_db.get(item_id)

def get_items() -> List[models.Item]:
    return list(fake_db.values())

def create_item(item: models.ItemCreate) -> models.Item:
    new_id = max(fake_db.keys()) + 1 if fake_db else 1
    db_item = models.Item(id=new_id, **item.model_dump())
    fake_db[new_id] = db_item
    return db_item

def update_item(item_id: int, item: models.ItemCreate) -> Optional[models.Item]:
    if item_id in fake_db:
        db_item = fake_db[item_id]
        update_data = item.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        return db_item
    return None

def delete_item(item_id: int) -> Optional[models.Item]:
    if item_id in fake_db:
        return fake_db.pop(item_id)
    return None
