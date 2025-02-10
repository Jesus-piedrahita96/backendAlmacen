from database.database import Base, timestamp
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(45), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    office_id = Column(Integer, ForeignKey("office.id"))
    created_at = timestamp()
    updated_at = timestamp()
    role = relationship("Role", back_populates="users")
    office = relationship("Office", back_populates="users")


class Office(Base):
    __tablename__ = "office"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    location = Column(String(45))
    created_at = timestamp()
    updated_at = timestamp()
    users = relationship("User", back_populates="office")
