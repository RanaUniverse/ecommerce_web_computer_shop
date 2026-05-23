"""
services/database/controllers/user.py
Here i will write the functions related to
the USER Table all the CRUD i will write here
"""

from sqlmodel import Session, select


from ..core import engine

from ..models import UserModel


from utils.custom_logger import logger


def add_new_user_row(user_obj: UserModel) -> UserModel | None:
    """
    it will try to insert the user if not success return none
    """
    with Session(engine) as session:
        try:
            session.add(user_obj)
            session.commit()
            session.refresh(user_obj)
            return user_obj

        except Exception as e:
            logger.error(f"Faild to make new user, {e}")
            return None


def get_user_row_by_user_id(user_id: str) -> UserModel | None:
    """
    it will return the userobj from the user_id
    """
    with Session(engine) as session:
        user_obj = session.get(UserModel, user_id)
        return user_obj


def get_user_row_by_phone_no(phone_no: str) -> UserModel | None:
    """
    it will search with the phone number column
    and then it will try to send the userrow
    """
    with Session(engine) as session:
        statement = select(UserModel).where(UserModel.phone_no == phone_no)
        result = session.exec(statement=statement)
        user_obj = result.first()
        return user_obj


def get_user_row_by_email_id(email_id: str) -> UserModel | None:
    """
    it will search with the Email id column
    and then it will try to send the user row
    """
    with Session(engine) as session:
        statement = select(UserModel).where(UserModel.email_id == email_id)
        result = session.exec(statement=statement)
        user_obj = result.first()
        return user_obj


def get_user_row_by_username(username: str) -> UserModel | None:
    """
    it will search with the username  column
    and then it will try to send the user row
    """
    with Session(engine) as session:
        statement = select(UserModel).where(UserModel.username == username)
        result = session.exec(statement=statement)
        user_obj = result.first()
        return user_obj
