from database.database import Base, timestamp
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    created_at = timestamp()
    updated_at = timestamp()
    users = relationship("User", back_populates="role")
    permissions = relationship(
        "Permission", secondary="role_permissions", back_populates="roles")


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    created_at = timestamp()
    updated_at = timestamp()
    roles = relationship("Role", secondary="role_permissions",
                         back_populates="permissions")


class RolePermission(Base):
    __tablename__ = "role_permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey(
        "permissions.id"), primary_key=True)
