from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(),unique=True,nullable=False)
    password=db.Column(db.String(15),nullable=False)
    
    
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True) #-primary key
    name=db.Column(db.String(20),unique=True,nullable=False)
    products=db.relationship("Product",backref="Category",lazy=True,cascade="all,delete-orphan")
    
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(20),unique=True,nullable=False)
    price=db.Column(db.Integer,nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey("category.id"),nullable=False)
    
     
#cat=Category.query.first()
#cat.products--


#pro=Product.query.first()
#pro.category--



