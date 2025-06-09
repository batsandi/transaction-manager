from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)


def get_db():
    """
    dependency generator to create  new db session
    for each api-db operation. this is injected under each route
    """
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    """
    This function creates all the database tables defined by our SQLModel models.
    It should be called once when the application starts up.
    """
    # This line tells the engine to create all tables that inherit from SQLModel.metadata.
    SQLModel.metadata.create_all(engine)

