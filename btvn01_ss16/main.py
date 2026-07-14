'''
Tổng hợp 3 lỗi:
Quan hệ	Lỗi	Cách sửa:
1-1	Thiếu uselist=False và unique=True	Thêm uselist=False, unique=True
1-N	back_populates="department_id" sai	Đổi thành back_populates="department"
N-N	Thiếu secondary=student_course	Thêm secondary=student_course ở cả hai phía
'''
from fastapi import FastAPI
import models
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def check_api():
    return {
        "API chạy ok"
    }





