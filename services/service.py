from models.models_restaurant import Menu, Submenu, Dishes
from sqlalchemy.orm import Session
from dto import dto_restaurant
from uuid import UUID

from sqlalchemy.exc import IntegrityError


class DbService:
    def __init__(self, model):
        self.model = model

    def create(
        self,
        db: Session,
        data: Menu | Submenu | Dishes,
        id: UUID = None,
        menu_id: UUID = None,
        submenu_id: UUID = None,
    ):
        data_dict = data.dict()
        if "price" in data_dict:
            data_dict["price"] = str(float(data_dict["price"]))
            print(f"====================={data_dict}=====")
        table = self.model(**data_dict)
        if id is not None:
            table.id = id
        if menu_id is not None:
            table.menu_id = menu_id
        if submenu_id is not None:
            table.submenu_id = submenu_id
        try:
            db.add(table)
            db.commit()
            db.refresh(table)
        except IntegrityError as e:
            print(e)
            return False
        # print(f"+++++++++++++++++++++++++++++++={table.price}{type(table.price)}")
        return table

    def get_value(self, db: Session, id: UUID = None):
        if id:
            result = db.query(self.model).filter(self.model.id == id).first()
            if self.model == Menu and result is not None:
                submenu_count = db.query(Submenu).filter(Submenu.menu_id == id).count()
                dish_count = (
                    db.query(Dishes)
                    .join(Submenu, Dishes.submenu_id == Submenu.id)
                    .filter(Submenu.menu_id == id)
                    .count()
                )
                result.submenu_count = submenu_count
                result.dish_count = dish_count
            elif self.model == Submenu and result is not None:
                dish_count = db.query(Dishes).filter(Dishes.submenu_id == id).count()
                result.dish_count = dish_count
            elif self.model == Dishes and result is not None:
                result.price = str(float(result.price))
            return result

    def get_all(self, db: Session, id: UUID = None):
        all_values = db.query(self.model).all()
        return all_values

    def update(
        self,
        db: Session,
        data: Menu | Submenu | Dishes,
        id: UUID = None,
    ):
        table = db.query(self.model).filter(self.model.id == id).first()
        for key, value in data.dict().items():
            setattr(table, key, value)
        db.add(table)
        db.commit()
        db.refresh(table)
        return table

    def remove(self, db, id):
        table = db.query(self.model).filter(self.model.id == id).delete()
        db.commit()
        return table
