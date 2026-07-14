from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base # Giả định Base đã được khai báo từ hệ thống

# 1. Bảng trung gian cho quan hệ Nhiều - Nhiều (Student - Course)
student_course = Table(
    "student_course", 
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True)
)
