from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product( Id , name , price , Picturelink , Description):
	Product_object=Product(
	Id=Id,	
	name=name , 
	price=price , 
	Picturelink=Picturelink , 
	Description=Description)
	session.add(Product_object)
	session.commit()

add_product(1,"Bag",99.9,"bag.jpeg","A white and black bag")	

def edit_product(name , Description ):
	Product_object=session.query(Product).filter_by(id=id).first()
	Product_object.name = name
	session.commit()
edit_product(1 , "something" , "be creative and describe it however you want")	

def delete_product(product_name):
	session.query(Product).filter_by(name=product_name).delete()
	session.commit()
delete_product("something")	
