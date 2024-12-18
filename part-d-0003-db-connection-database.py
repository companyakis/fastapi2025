from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ALCHEMY_DB_URL = 'sqlite:///./todoapp.db'

engine = create_engine(ALCHEMY_DB_URL, connect_args={'check_same_thread': False})

"""
    check_same_thread (bool) – If True (default), ProgrammingError will be raised 
    if the database connection is used by a thread other than the one that created it. 
    If False, the connection may be accessed in multiple threads; 
    write operations may need to be serialized by the user to avoid data corruption
"""

session_local = sessionmaker(autocommit= False, autoflush=False, bind=engine)

"""
MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0)
"""

Base = declarative_base()
