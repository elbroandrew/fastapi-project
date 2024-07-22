from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users

#  is for creating new users.
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)
#  is for retrieving user info to be used outside our application
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)
# is for retrieving user info to be used within our application
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)