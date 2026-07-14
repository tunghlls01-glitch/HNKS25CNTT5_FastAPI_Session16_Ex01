from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base # Giả định Base đã được khai báo từ hệ thống

# 2. Khai báo các Model
class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    
    # Cấu hình liên kết đến Student
    students = relationship("Student", back_populates="department")