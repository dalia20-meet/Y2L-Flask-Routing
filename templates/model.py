from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product(Base):
   __tablename__ = 'Product'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
   Picture link = Column(String)
   Description = Column(String)
   