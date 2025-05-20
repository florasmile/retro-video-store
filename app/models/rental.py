from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from ..db import db
from datetime import datetime, timedelta
from sqlalchemy import DateTime  # SQLAlchemy column type


class Rental(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    video_id: Mapped[int] = mapped_column(ForeignKey("video.id"))
    due_date: Mapped[datetime| None] = mapped_column(DateTime, nullable=True)
    status: Mapped[str]

    # def to_dict(self):
    #     return dict(
    #         id=self.id,
    #         name=self.name,
    #         postal_code=self.postal_code,
    #         phone=self.phone,
    #         register_at=self.register_at
    #     )
    
    # def update(self, data):
    #     self.name=data["name"]
    #     self.postal_code=data["postal_code"]
    #     self.phone=data["phone"]
    #     self.register_at=data.get("register_at", date_to_str(datetime.now()))

    @classmethod
    def from_dict(cls, data):
        return cls(
            customer_id=data["customer_id"],
            video_id=data["video_id"],
            due_date=datetime.now() + timedelta(days=7),
            status="RENTED"
        )
    

    