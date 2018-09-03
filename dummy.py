import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///data.db', echo=True)
 

Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","admin","wth444164@gmail.com","Admin")
session.add(user)
 
user = User("test","test","554288973@qq.com","User")
session.add(user)

session.commit()