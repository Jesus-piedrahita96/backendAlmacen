from database.database import Base, timestamp
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    ForeignKey
)


class EquipmentType(Base):
    __tablename__ = "equipment_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    created_at = timestamp()
    updated_at = timestamp()
    equipments = relationship("Equipment", back_populates="equipment_type")


class HeaderEquipment(Base):
    __tablename__ = "header_equipment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(50), nullable=False)
    equipment_name = Column(String(50), nullable=False)
    description = Column(Text)
    quantity = Column(Integer, nullable=False)
    sn = Column(String(45), nullable=False)
    fixed_asset = Column(Boolean, nullable=False)
    supplier_id = Column(Integer, ForeignKey("supplier.id"))
    created_at = timestamp()
    updated_at = timestamp()
    supplier = relationship("Supplier")


class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(45), nullable=False)
    sn = Column(String(45), nullable=False)
    mac = Column(String(45), nullable=False)
    quantity_units = Column(Integer, nullable=False)
    equipment_type_id = Column(Integer, ForeignKey("equipment_types.id"))
    supplier_id = Column(Integer, ForeignKey("supplier.id"))
    created_at = timestamp()
    updated_at = timestamp()
    equipment_type = relationship("EquipmentType", back_populates="equipments")
    supplier = relationship("Supplier")


class BadEquipment(Base):
    __tablename__ = "bad_equipment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    reason = Column(Text)
    created_at = timestamp()
    updated_at = timestamp()
