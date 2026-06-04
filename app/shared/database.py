"""
app/shared/database.py
Here database initialize and db sesion related engine will make so that everywher ei can import
this and it will work
"""

from sqlmodel import (
    create_engine,
    SQLModel,
)

from .config import config_settings

engine = create_engine(
    url=config_settings.db_url,
)


# the below fun will need to run in main.py if i want to make
# the database from main.py mostly for sqlite.
# But mostly i will use alembic to make the database and table
# and then the main.py will run to do the operaions not making db
def create_db_and_engine():
    SQLModel.metadata.create_all(bind=engine)
