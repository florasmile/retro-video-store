from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime

class Video(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    release_date: Mapped[datetime]
    inventory: Mapped[int]