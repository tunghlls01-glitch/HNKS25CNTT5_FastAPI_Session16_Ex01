from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base # Giả định Base đã được khai báo từ hệ thống
from .student_course import student_course
class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    
    # Quan hệ N - N với Student
    students = relationship("Student",secondary=student_course, back_populates="courses")