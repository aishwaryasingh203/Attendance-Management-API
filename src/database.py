from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Apne MySQL credentials yahan dalo
# Format: mysql+pymysql://username:password@localhost:3306/skillbridge_db
DATABASE_URL = "mysql+pymysql://root:database@localhost:3306/skillbridge_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()