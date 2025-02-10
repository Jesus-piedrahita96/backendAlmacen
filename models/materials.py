from database.database import Base, timestamp
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime
)


class Material(Base):
    __tablename__ = "material"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    description = Column(Text)
    supplier_id = Column(Integer, ForeignKey("supplier.id"))
    created_at = timestamp()
    updated_at = timestamp()
    supplier = relationship("Supplier")


class Supplier(Base):
    __tablename__ = "supplier"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    contact_info = Column(Text)
    created_at = timestamp()
    updated_at = timestamp()


class Dispatch(Base):
    __tablename__ = "dispatch"

    id = Column(Integer, primary_key=True, autoincrement=True)
    identification = Column(String(45), nullable=False)
    quantity = Column(Integer, nullable=False)
    dispatch_date = Column(DateTime, nullable=False)
    delivered_by = Column(Integer, ForeignKey("users.id"))
    office_id = Column(Integer, ForeignKey("office.id"))
    equipment_type_id = Column(Integer, ForeignKey("equipment_types.id"))
    observations = Column(Text)
    created_at = timestamp()
    updated_at = timestamp()


class BadMaterial(Base):
    __tablename__ = "bad_material"

    id = Column(Integer, primary_key=True, autoincrement=True)
    material_id = Column(Integer, ForeignKey("material.id"))
    reason = Column(Text)
    created_at = timestamp()
    updated_at = timestamp()
