from django.db import models
from common.models import BaseModel


class Users(BaseModel):
    user_id = models.TextField(primary_key=True)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    dob = models.DateField(null=False)
    email = models.EmailField(unique=True, null=False)

    class Meta:
        db_table = "users"

    @staticmethod
    def create_user(user_id, first_name, last_name, dob, email):
        user = Users.objects.create(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            email=email,
        )
        return user
