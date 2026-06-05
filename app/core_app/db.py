"""
app/core_app/db.py
I will make the database session related code
i will use this outside
"""

from sqlmodel import Session, create_engine


from ..shared.config import config_settings

engine = create_engine(config_settings.db_url)


def get_session():
    with Session(engine) as session:
        yield session
