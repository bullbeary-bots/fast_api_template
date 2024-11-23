from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLITE3
# SQL_DATABASE_URL = "sqlite:///todoapp.db"
# engine = create_engine(SQL_DATABASE_URL, connect_args={'check_same_thread': False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# POSTGRESQL
SQL_DATABASE_URL = 'postgresql://postgres:admin123@localhost/TodoApplicationDatabase'
engine = create_engine(SQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MYSQL
# SQL_DATABASE_URL = 'mysql+pymysql://root:cede924c@127.0.0.1:3306/TodoApplicationDatabase'
# engine = create_engine(SQL_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
