from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime
# from .model_utitlities import date_to_str

class Video(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    release_date: Mapped[str]
    total_inventory: Mapped[int]

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            release_date=self.release_date,
            total_inventory=self.total_inventory
        )
    
    def update(self, data):
        self.title=data["title"]
        self.release_date=data["release_date"]
        self.total_inventory=data["total_inventory"]

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            release_date=data["release_date"],
            total_inventory=data["total_inventory"]
        )
    