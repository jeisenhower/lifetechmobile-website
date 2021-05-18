from models import Base
from config import SQLALCHEMY_DATABASE_URI, PRODUCTION_SQL_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(PRODUCTION_SQL_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def recreate_datatbase():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    recreate_datatbase()

