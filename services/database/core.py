"""
services/database/core.py
Here i will write the code related to the database
making and so on
"""

from sqlmodel import (
    create_engine,
    SQLModel,
)


from utils.config import DATABASE_URL

engine = create_engine(url=DATABASE_URL)


# the below fun will need to run in main.py if i want to make
# the database from main.py mostly for sqlite
# mostly i will use alembic to make the database and table
# and then the main.py will run to do the operaions not making db
def create_db_and_engine():
    SQLModel.metadata.create_all(bind=engine)
