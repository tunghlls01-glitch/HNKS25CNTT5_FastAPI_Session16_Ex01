from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base # Giả định Base đã được khai báo từ hệ thống
from .student_course import student_course
class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    # Thiết lập khóa ngoại trỏ về Department
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="students")
    
    # Quan hệ 1 - 1 với Profile
    profile = relationship("Profile", back_populates="student", uselist=False)
    
    # Quan hệ N - N với Course
    courses = relationship("Course",secondary=student_course, back_populates="students")