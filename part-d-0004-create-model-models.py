from sqlalchemy import Column, String, Integer, Boolean
from database import Base

# our table has 5 columns
# id, title, todo description, importance/priority and completions...

class Todos(Base):
    
    __tablename__ = "todos"
    
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    todo_description = Column(String)
    todo_importance = Column(Integer) 
    is_completed = Column(Boolean, default=False)
    
