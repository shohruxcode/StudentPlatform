from datetime import datetime
from typing import List

from sqlalchemy import (
    String, Integer, Boolean, DateTime, Enum, Text, ForeignKey, func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from typing import Optional

import enum


class StudentLevel(enum.Enum):
    Beginner = "Beginner"
    Intermediate = "Intermediate"
    Advanced = "Advanced"


class Student(Base):
    __tablename__ = "students"

    # CORE
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    full_name: Mapped[Optional[str]] = mapped_column(String(255))
    avatar_url: Mapped[Optional[str]] = mapped_column(String(512))
    bio: Mapped[Optional[str]] = mapped_column(Text)
    # ACADEMIC
    enrollment_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    current_level: Mapped[StudentLevel] = mapped_column(
        Enum(StudentLevel), default=StudentLevel.Beginner
    )

    total_points: Mapped[int] = mapped_column(Integer, default=0)
    global_rank: Mapped[Optional[str]] = mapped_column(Integer)

    # STATUS
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    # RELATIONSHIP
    projects: Mapped[List["Project"]] = relationship(
        back_populates="student", cascade="all, delete-orphan"
    )
    achievements: Mapped[list["StudentAchievement"]] = relationship("StudentAchievement", back_populates="student")
    degrees: Mapped[List["StudentDegree"]] = relationship("StudentDegree", back_populates="student")

    achievements: Mapped[List["StudentAchievement"]] = relationship(
        back_populates="student", cascade="all, delete-orphan"
    )

    degrees: Mapped[List["StudentDegree"]] = relationship(
        back_populates="student", cascade="all, delete-orphan"
    )

    # METADATA
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
