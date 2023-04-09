from django.db import models
from common.models import BaseModel
from account.models import Users


class UserCredentials(BaseModel):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    hashed_password = models.TextField(null=False)
    verified = models.BooleanField(default=False)

    class Meta:
        db_table = "user_credentials"

    @staticmethod
    def create_user_credentials(hashed_password):
        user_credentials = UserCredentials.objects.create(
            hashed_password=hashed_password, verified=False
        )
        return user_credentials

    @staticmethod
    def mark_verify(user_id):
        user_credentials = UserCredentials.objects.filter(user_id=user_id).first()
        user_credentials.verified = True
        user_credentials.save()
        return user_credentials

    @staticmethod
    def get_user_credential_by_id(user_id):
        return UserCredentials.objects.filter(user_id=user_id).first()
