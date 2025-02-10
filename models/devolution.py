from database.database import Base, timestamp
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)


class Return(Base):
    __tablename__ = "return"

    id = Column(Integer, primary_key=True, autoincrement=True)
    return_date = Column(DateTime, nullable=False)
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    material_id = Column(Integer, ForeignKey("material.id"))
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = timestamp()
    updated_at = timestamp()


class Revision(Base):
    __tablename__ = "revision"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(45), nullable=False)
    destination = Column(String(45), nullable=False)
    equipment_type_id = Column(Integer, ForeignKey("equipment_types.id"))
    material_id = Column(Integer, ForeignKey("material.id"))
    bad_material_id = Column(Integer, ForeignKey("bad_material.id"))
    bad_equipment_id = Column(Integer, ForeignKey("bad_equipment.id"))
    created_at = timestamp()
    updated_at = timestamp()
