from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from ..db import db

class Rental(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    video_id: Mapped[int] = mapped_column(ForeignKey("video.id"))
    