"""
app/features/identity/utils.py
Here i will keep some needed important staff to use in this domain
like i will have some constants to use
"""

from pydantic import BaseModel


class UserRoles(BaseModel):
    CUSTOMER: str = "customer"
    BUSINESS: str = "business"
    STAFF: str = "staff"
    MANAGER: str = "manager"
    OWNER: str = "owner"
    DEVELOPER: str = "developer"


user_roles = UserRoles()
