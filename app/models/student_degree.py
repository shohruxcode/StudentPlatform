# app/models/student_degree.py
from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class StudentDegree(Base):
    __tablename__ = "student_degrees"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    degree_id: Mapped[int] = mapped_column(ForeignKey("degrees.id"), nullable=False)

    earned_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    certificate_url: Mapped[str] = mapped_column(String(255), nullable=True)
    verification_code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # Relationships
    student: Mapped["Student"] = relationship("Student", back_populates="degrees")
    degree: Mapped["Degree"] = relationship("Degree", back_populates="students")
