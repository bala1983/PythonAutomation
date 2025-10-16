from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from declarative_base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    student = relationship("Course", back_populates="course")
