from django.db import models
from common.models import BaseModel


class Users(BaseModel):
    user_id = models.CharField(primary_key=True, max_length=255)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.EmailField(unique=True, null=False)

    class Meta:
        db_table = "users"

    @staticmethod
    def create_user(user_id, first_name, last_name, email):
        user = Users.objects.create(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        return user

    @staticmethod
    def get_users():
        users = Users.objects.all()
        return users
