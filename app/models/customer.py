from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime
from .model_utitlities import date_to_str


class Customer(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    postal_code: Mapped[str]
    phone: Mapped[str]
    register_at: Mapped[str]

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            postal_code=self.postal_code,
            phone=self.phone,
            register_at=self.register_at
        )
    
    def update(self, data):
        self.name=data["name"]
        self.postal_code=data["postal_code"]
        self.phone=data["phone"]
        self.register_at=data.get("register_at", date_to_str(datetime.now()))

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            postal_code=data["postal_code"],
            phone=data["phone"],
            register_at=data.get("register_at", date_to_str(datetime.now()))
        )
    

        
