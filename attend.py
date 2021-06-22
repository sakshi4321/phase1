import sqlalchemy as db
import pandas as pd
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('sqlite:///test.sqlite') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()
course='ic'
emp = db.Table(course, metadata,
              db.Column('Id', db.Integer(),primary_key=True),
              db.Column('name', db.String(255), nullable=False),
              db.Column('date', db.DateTime),
              
              
              db.Column('attendance', db.Boolean(), default=True)
              )

metadata.create_all(engine) #Creates the table

query = db.insert(emp).values(Id=199, name='nwee', date=datetime(2015, 6, 5, 8, 10, 10, 10), attendance=True) 
ResultProxy = connection.execute(query)


query = db.insert(emp) 

values_list = [{'Id':'167', 'name':'rahh', 'date':datetime(2015, 6, 5, 8, 10, 10, 10), 'attendance':False},
               {'Id':'131', 'name':'raeshu', 'date':datetime(2015, 6, 5, 8, 10, 10, 10), 'attendance':True}]
ResultProxy = connection.execute(query,values_list)




results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df.head(10))

