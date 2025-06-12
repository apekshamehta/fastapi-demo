import sqlmodel
from sqlmodel import SQLModel,Session
from .config import DATABASE_URL


if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL need to be set")


engine = sqlmodel.create_engine(DATABASE_URL)


def init_db():
    
    print("database is ready")
    SQLModel.metadata.create_all(engine)
    
    
def get_session():
    with Session(engine) as session:
        yield session