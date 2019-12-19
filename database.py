from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(id,name,price,Picturelink,Description):
	Product_object=Product(
		id=id,	
		name=name , 
		price=price , 
		Picturelink=Picturelink , 
		Description=Description)
	session.add(Product_object)
	session.commit()

add_product(3,"Bag",99.9,"bag.jpeg","A white and black bag")	

def edit_product(name , Description ):
	Product_object=session.query(Product).filter_by(id=id).first()
	Product_object.name = name
	session.commit()
edit_product("something" , "be creative and describe it however you want")	

def delete_product(product_name):
	session.query(Product).filter_by(name=product_name).delete()
	session.commit()
#delete_product("something")

def query_all():
	Product = session.query(Product).all()
	return Product
#print(query_all())

def query_by_id(id):
	Product = session.query(Product).filter_by(id=id).first()
	return Product
#print (query_by_id("something"))


def Add_To_Cart(ProductID):
	Product_object = Cart(ProductID=ProductID
	   )
	session.add(product_object)
	session.commit()


			
