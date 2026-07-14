from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base # Giả định Base đã được khai báo từ hệ thống

class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String(255))
    
    # Khóa ngoại liên kết 1-1 với Student
    student_id = Column(Integer, ForeignKey("students.id"), unique=True)
    student = relationship("Student", back_populates="profile")